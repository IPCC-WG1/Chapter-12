# Calculation of the snow index (SWE100)

SWE100 is the mean number of days per year with snow depth greater than 100 ml (100 kg per m^2) snow water equivalent over the northern hemisphere snow season (November to March)

It is shown in Figures 12.9 and 12.10.

The following scripts calculate SWE100 for the standard 20-year IPCC periods (1995-2014, 2041-2060 and 2081-2100) for CMIP5,CMIP6 or North America CORDEX.
- snow_CMIP5.sh
- snow_CMIP6.sh
- snow_NA_CORDEX.sh

The required inputs for the above scripts are
- 'snw' data for CMIP5/6/North America CORDEX for historical and rcp2.6 and 8.5 (or SSP5-8.5 or SSP1-2.6 for CMIP6)
- land area fraction files (sftlf)
- remapperR_v2.cdo ((only for CMIP5/6) available in this repository, conservatively remaps land and ocean data separately and then interpolates between the two)
- destination_mask_1.nc4 (for CMIP6) and destination_mask_2.nc4 (CMIP5) (available in this repository, these are the destination grids used by remappeR_v2.cdo.sh. The first is 1 degree regular lat-lon and the second is 2 degree)


The following scripts calculate SWE100 for the 20 year periods corresponding to the following global warming levels: 1.5, 2, 3 and 4 degrees Celsuis
- Snow_CMIP5_GWLs.ipynb
- Snow_CMIP6_GWLs.ipynb
- Snow_NA_CORDEX_GWLs.ipynb

The required inputs are:
- yearly files outputted by the above scripts (filenames are like this: MPI-ESM-MR_26_snw100seas_1980-2100.2deg.nc)
- CMIP5_Atlas_WarmingLevels.csv or CMIP6_Atlas_WarmingLevels.csv (table of the central year of the 20-year periods corresponding to the global warming levels)



