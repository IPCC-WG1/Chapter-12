import regionmask
import xarray as xr
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np
import json
import glob

from climaf.api import *



pattern = '/data/jservon/IPCC/tx35/bias_corrected/individual_models/CMIP6_${experiment}_${variable}_${period}_${member}.nc'
cproject('tx_individual_models_cmip6_ch12','experiment','period','member',('variable','tx35isimip'), ensemble=['member'], separator='%')
dataloc(project='tx_individual_models_cmip6_ch12', url=pattern)    


exp_dict_list = dict(
    baseline = dict(experiment='historical',
         period='1995-2014'
        ),
    ssp126_mid = dict(experiment='ssp126',
         period='2041-2060'
        ),
    ssp126_far = dict(experiment='ssp126',
         period='2081-2100'
        ),
    ssp585_mid = dict(experiment='ssp585',
         period='2041-2060'
        ),
    ssp585_far = dict(experiment='ssp585',
         period='2081-2100'
        )  
)

# -- Make the ensembles per experiments
ens_exp_dict = dict()
lom_per_exp = dict()
for exp in exp_dict_list:
    
    experiment = exp_dict_list[exp]['experiment']
    period = exp_dict_list[exp]['period']

    req = ds(experiment=experiment,
             period=period,
             member='*',
             project='tx_individual_models_cmip6_ch12')

    ens_exp = req.explore('ensemble')
    #
    if 'EC-Earth3-Veg_r1i1p1f1' in ens_exp:
        ens_exp.pop('EC-Earth3-Veg_r1i1p1f1')

    # -- Climatologies
    clim_exp      = clim_average(ccdo(ens_exp, operator='yearsum'), 'ANM')

    # -- Changes = Scenario minus baselines
    ens_exp_dict[exp] = clim_exp
    lom_per_exp[exp] = clim_exp.keys()

req_dict = dict(project='tx_individual_models_cmip6_ch12')


# -- Get the GWL info
import csv
GWL_csv = '/home/jservon/Chapter12_IPCC/scripts/ATLAS/warming-levels/CMIP6_Atlas_WarmingLevels.csv'

GWL_dict = dict()
i = 0
with open(GWL_csv) as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')#, quotechar='|')
    for row in spamreader:
        print row
        model = row[0]#.split('_')[0]
        print model
        GWL_dict[model] = dict()
        if i==0:
            colnames = row
        j = 1
        for elt in row[1:len(row)]:
            print elt
            GWL_dict[model][colnames[j]] = row[j]
            j = j + 1
        i = i + 1
        
# -- Retrieve the GWL in the models
ens_dict_per_GWL = dict()
list_of_GWLs = ['1.5','2','3','4']
for GWL in list_of_GWLs:
    ens_dict_per_GWL[GWL] = dict()


for scenario in ['26','85']:
    
    if scenario=='26': req_scenario = 'ssp126'
    if scenario=='85': req_scenario = 'ssp585'
    list_of_models = ens_exp_dict[req_scenario+'_far'].keys()
    for wmodel_realization in list_of_models:
        wmodel = wmodel_realization #.split('_')[0]
        if wmodel in GWL_dict:
            print 'We have : ', wmodel
            print GWL_dict[wmodel]
            for GWL in list_of_GWLs:
                if scenario=='26': GWL_scenario = GWL+'_ssp126'
                if scenario=='85': GWL_scenario = GWL+'_ssp585'

                # --> file nc
                # --> period
                central_year = GWL_dict[wmodel][GWL_scenario]
                if central_year not in ['NA','9999'] and float(central_year)>=2024:
                    start_year = str( int(central_year)-9 )
                    end_year = str( int(central_year)+10 )
                    
                    dat = ds(member = wmodel_realization,
                             experiment = req_scenario,
                             period=start_year+'-'+end_year,
                             **req_dict
                             )
                    ens_dict_per_GWL[GWL][wmodel+'_'+scenario] = clim_average(ccdo(dat, operator='yearsum'), 'ANM')
                    print cfile(ens_dict_per_GWL[GWL][wmodel+'_'+scenario])
        else:
            print 'We dont have GWL info for ',wmodel,' in GWL_dict = ',GWL_dict.keys()

# -- Functions to compute the regional averages
def weighted_mean(da, weights, dim):
    """Reduce da by a weighted mean along some dimension(s).

    Parameters
    ----------
    da : DataArray
        Object over which the weighted reduction operation is applied.    
    weights : DataArray
        An array of weights associated with the values in this Dataset.
    dim : str or sequence of str, optional
        Dimension(s) over which to apply the weighted `mean`.
        
    Returns
    -------
    weighted_mean : DataArray
        New DataArray with weighted mean applied to its data and
        the indicated dimension(s) removed.
    """

    weighted_sum = (da * weights).sum(dim=dim, skipna=True)
    # need to mask weights where data is not valid
    masked_weights = weights.where(da.notnull())
    sum_of_weights = masked_weights.sum(dim=dim, skipna=True)
    valid_weights = sum_of_weights != 0
    sum_of_weights = sum_of_weights.where(valid_weights)

    return weighted_sum / sum_of_weights

def average_over_AR6_region(filename, variable, region_name):

    # -- AR6 regions
    #ar6_all = regionmask.defined_regions.ar6.all
    # -- Get the regions
    ar6_land = regionmask.defined_regions.ar6.land

    #ax = ar6_all.plot()
    # -- Get land/sea mask (generic)
    land_110 = regionmask.defined_regions.natural_earth.land_110

    # -- Get data
    ds = xr.open_dataset(filename, decode_times=False)
    dat = ds[variable]
    dat.values = np.array(dat.values, dtype=np.float32)

    # -- Mask the data
    mask_3D = ar6_land.mask_3D(dat) # AR6 mask
    land_mask = land_110.mask_3D(dat) # Land sea mask
    mask_lsm = mask_3D * land_mask.squeeze(drop=True) # Combine the two

    weights = np.cos(np.deg2rad(dat.lat))
    
    if region_name=='all':
        return weighted_mean(dat, mask_3D * weights, ("lon", "lat"))
    else:
        if isinstance(region_name, list):
            res = list()
            for region in region_name:
                region_mask = mask_lsm.isel(region=list(mask_3D.abbrevs).index(region))
                dat_region = dat.where(region_mask)
                weights_region = weights.where(region_mask)
                res.append( weighted_mean(dat_region, region_mask*weights_region, ("lon","lat")) )
            return res
        else:
            region_mask = mask_lsm.isel(region=list(mask_3D.abbrevs).index(region_name))
            dat_region = dat.where(region_mask)
            weights_region = weights.where(region_mask)            
            return weighted_mean(dat_region, region_mask*weights_region, ("lon","lat"))
    
def regions_contained(lon, lat, regions):

    # determine if the longitude needs to be wrapped
    regions_is_180 = regions.lon_180
    grid_is_180 = regionmask.core.utils._is_180(lon.min(), lon.max())

    wrap_lon = not regions_is_180 == grid_is_180

    lon_orig = lon.copy()
    if wrap_lon:
        lon = regionmask.core.utils._wrapAngle(lon, wrap_lon)

    lon = np.asarray(lon).squeeze()
    lat = np.asarray(lat).squeeze()

    if lon.ndim == 1 and lat.ndim == 1:
        poly = shapely.geometry.box(lon.min(), lat.min(), lon.max(), lat.max())

    # convex_hull is not really what we need
    # https://gist.github.com/dwyerk/10561690
    #     elif lon.ndim == 2 and lat.ndim == 2:
    #         # get the convex hull from all points
    #         lonlat = np.stack([lon.ravel(), lat.ravel()], axis=1)
    #         multipoint = shapely.geometry.MultiPoint(lonlat)
    #         poly = multipoint.convex_hull
    else:
        raise ValueError("Cannot currently handle 2D coordinates")

    fully_contained = list()
    for region_poly in regions.polygons:
        res = poly.contains(region_poly)

        fully_contained.append(res)

    return xr.DataArray(
        fully_contained, dims=["region"], coords=dict(region=regions.numbers)
    )

# -- Compute regional averages for time periods
regional_averages = dict()

# -- Loop on experiments / horizons
for ens_exp in ens_exp_dict:
    print ens_exp
    regional_averages[ens_exp] = dict()
    # -- Loop on the members of each ensemble
    for mem in ens_exp_dict[ens_exp]:
        print mem
        # -- Compute the averages for each AR6 region thanks to regionmask
        tmp = average_over_AR6_region(cfile(ens_exp_dict[ens_exp][mem]), 'tx35isimip', 'all')
        region_names = tmp.abbrevs
        for tmp_region_name in region_names:
            region_name = str(tmp_region_name.values)
            print region_name
            region_value = float(tmp.sel(region=list(tmp.abbrevs).index(region_name)).values)
            if region_name not in regional_averages[ens_exp]:
                regional_averages[ens_exp][region_name] = [region_value]
            else:
                regional_averages[ens_exp][region_name].append(region_value)

# -- Compute differences against baseline
regional_averages_diff = dict()

# -- Loop on experiments / horizons
#wind_ens_clim_exp_dict[exp]
for ens_exp in ens_exp_dict:
    if ens_exp not in ['baseline','baseline_ext']:
        print ens_exp
        regional_averages_diff[ens_exp] = dict()
        # -- Loop on the members of each ensemble
        for mem in ens_exp_dict[ens_exp]:
            if mem in ens_exp_dict['baseline']:
                print mem
                # -- Compute the averages for each AR6 region thanks to regionmask
                #print cfile(ens_exp_dict[ens_exp][mem])
                #cmd = 'ncrename -v .uas,wind -v .vas,wind -v .sfcWind,wind '+cfile(ens_exp_dict[ens_exp][mem])
                #os.system(cmd)
                tmp = average_over_AR6_region(cfile(ens_exp_dict[ens_exp][mem]), 'tx35isimip', 'all')
                tmp_baseline = average_over_AR6_region(cfile(ens_exp_dict['baseline'][mem]), 'tx35isimip', 'all')
                region_names = tmp.abbrevs
                for tmp_region_name in region_names:
                    region_name = str(tmp_region_name.values)
                    region_value = float(tmp.sel(region=list(tmp.abbrevs).index(region_name)).values)
                    region_value_baseline = float(tmp_baseline.sel(region=list(tmp.abbrevs).index(region_name)).values)
                    if region_name not in regional_averages_diff[ens_exp]:
                        regional_averages_diff[ens_exp][region_name] = [region_value - region_value_baseline]
                    else:
                        regional_averages_diff[ens_exp][region_name].append(region_value - region_value_baseline)
        #

# -- regional averages for the GWL
for GWL in ens_dict_per_GWL:
    print GWL
    regional_averages[GWL] = dict()
    # -- Loop on the members of each ensemble
    for mem in ens_dict_per_GWL[GWL]:
        print mem
        # -- Compute the averages for each AR6 region thanks to regionmask
        tmp = average_over_AR6_region(cfile(ens_dict_per_GWL[GWL][mem]), 'tx35isimip', 'all')
        region_names = tmp.abbrevs
        for tmp_region_name in region_names:
            region_name = str(tmp_region_name.values)
            print region_name
            region_value = float(tmp.sel(region=list(tmp.abbrevs).index(region_name)).values)
            if region_name not in regional_averages[GWL]:
                regional_averages[GWL][region_name] = [region_value]
            else:
                regional_averages[GWL][region_name].append(region_value)

# -- Differences with baseline for GWL
# -- Loop on experiments / horizons
for GWL in ens_dict_per_GWL:
    print GWL
    regional_averages_diff[GWL] = dict()
    # -- Loop on the members of each ensemble
    for mem in ens_dict_per_GWL[GWL]:
        wmem = mem.replace('_85','').replace('_26','')
        #if mem.replace('_85','').replace('_26','') in ens_exp_dict['historical_1995-2014']:
        if wmem in ens_exp_dict['baseline']:
            print wmem
            # -- Compute the averages for each AR6 region thanks to regionmask
            tmp = average_over_AR6_region(cfile(ens_dict_per_GWL[GWL][mem]), 'tx35isimip', 'all')
            tmp_baseline = average_over_AR6_region(cfile(ens_exp_dict['baseline'][wmem]), 'tx35isimip', 'all')
            region_names = tmp.abbrevs
            for tmp_region_name in region_names:
                region_name = str(tmp_region_name.values)
                #print region_name
                region_value = float(tmp.sel(region=list(tmp.abbrevs).index(region_name)).values)
                region_value_baseline = float(tmp_baseline.sel(region=list(tmp_baseline.abbrevs).index(region_name)).values)
                if region_name not in regional_averages_diff[GWL]:
                    regional_averages_diff[GWL][region_name] = [region_value - region_value_baseline]
                else:
                    regional_averages_diff[GWL][region_name].append(region_value - region_value_baseline)

# -- Compute quantiles and save in json
quantiles_dict = dict()
for clim_period in regional_averages:
    quantiles_dict[clim_period] = dict()
    for region_name in regional_averages[clim_period]:
        print clim_period, region_name
        quantiles_dict[clim_period][region_name] = dict()
        dat = np.array(regional_averages[clim_period][region_name])
        q10 = np.quantile(dat, 0.1)
        q50 = np.quantile(dat, 0.5)
        q90 = np.quantile(dat, 0.9)
        quantiles_dict[clim_period][region_name] = [q10, q50, q90]

import json

ensemble = 'CMIP6'
outfilename = '/home/jservon/Chapter12_IPCC/data/tx35_satellites/'+ensemble+'_tx35isimip_AR6_regional_averages.json'
#print outfilename
with open(outfilename, 'w') as fp:
    json.dump(quantiles_dict, fp, sort_keys=True, indent=4)
    
quantiles_dict = dict()
for clim_period in regional_averages_diff:
    quantiles_dict[clim_period] = dict()
    for region_name in regional_averages_diff[clim_period]:
        print clim_period, region_name
        quantiles_dict[clim_period][region_name] = dict()
        dat = np.array(regional_averages_diff[clim_period][region_name])
        q10 = np.quantile(dat, 0.1)
        q50 = np.quantile(dat, 0.5)
        q90 = np.quantile(dat, 0.9)
        quantiles_dict[clim_period][region_name] = [q10, q50, q90]

import json

ensemble = 'CMIP6'
outfilename = '/home/jservon/Chapter12_IPCC/data/tx35_satellites/'+ensemble+'_tx35isimip_diff_AR6_regional_averages.json'
#print outfilename
with open(outfilename, 'w') as fp:
    json.dump(quantiles_dict, fp, sort_keys=True, indent=4)
