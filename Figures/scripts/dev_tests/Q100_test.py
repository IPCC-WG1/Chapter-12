import Ngl, Nio
import os, numpy, csv, json
from IPython.display import Image
from shapely.geometry import Polygon, Point
import geopandas

ncfile = '/data/jservon/climafcache/92/ed9d29785b60901846e62246d3b317b1bce46db336321048b5f8e9.nc'

mask_file1 = '/data/jservon/climafcache/39/dc7a83cfcf10113cad1f29305494174fd0222bc0e1227a2ae55bcb.nc'
mask_file = '/data/jservon/climafcache/0e/a88dee508ad9f21b76992506a38e4ad5f63fbfe3a12894c3e45f10.nc'

#----------------------------------------------------------------------
#  Add the trajectory lines.
#----------------------------------------------------------------------
def retrieve_AR6regions_for_region(region_name):

    regions_filename='/home/jservon/Chapter12_IPCC/scripts/ATLAS/reference-regions/IPCC-WGI-reference-regions-v4_coordinates.csv'

    # -- Store the informations by region in the 'regions' dictionary
    regions = dict()
    with open(regions_filename) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')#, quotechar='|')
        for row in spamreader:
            #if row[0]==region_name:
            if region_name in row[0]:
                region_dict = dict()
                lats_vect = []
                lons_vect = []
                tmp_polygon_vertices = []
                for vertice in row[4:-1]:
                    if vertice:
                        dum = vertice.split('|')
                        lons_vect.append(float(dum[0]))
                        lats_vect.append(float(dum[1]))
                        tmp_polygon_vertices.append( (float(dum[0]), float(dum[1])) )
                region_dict['polygon'] = Polygon(tmp_polygon_vertices)
                region_dict['lons_vect'] = lons_vect
                region_dict['lats_vect'] = lats_vect
                #
                regions[row[3]] = region_dict
    #
    return regions


#
def add_AR6regions(wks, base_map, regions):
    #
    txres                       = Ngl.Resources()  
    txres.txFontHeightF         = 0.018
    
    gsres                   = Ngl.Resources()
    # Polyline resources.
    gsres.gsLineColor       = "Black"
    gsres.gsLineThicknessF  = 3.0      # thrice thickness

    for subregion in regions:
        if subregion not in ['RAR','WSB','TIB','ECA', 'ESB']:
            #if regions[subregion]['region']==region_name:
            lons_vect = regions[subregion]['lons_vect']
            lats_vect = regions[subregion]['lats_vect']
            # Draw a text string labeling the marker
            Ngl.add_text(wks,base_map, subregion, numpy.mean(lons_vect), numpy.mean(lats_vect), txres)

            # -- Close the polygon
            lons_vect.append(lons_vect[0])
            lats_vect.append(lats_vect[0])
            poly1 = Ngl.add_polyline(wks,base_map,lons_vect,lats_vect,gsres)

    return


#07 68 30 45 75

def create_Q100_map(wks, ncfile, region_dict, title):
    
    f    = Nio.open_file(ncfile)
    dat  = f.variables["Q100"][:,:]
    lat  = f.variables["lat"][:]
    lon  = f.variables["lon"][:]

    cnres                 = Ngl.Resources()
    cnres.nglDraw  = False
    cnres.nglFrame = False
    cnres.nglMaximize = False

    # Contour resources
    cnres.cnFillOn        = True
    cnres.cnLevelSelectionMode = "ManualLevels"
    cnres.cnLevelSpacingF      = 0.1
    cnres.cnMinLevelValF       = -1
    cnres.cnMaxLevelValF       = 1

    cnres.cnFillPalette   = "MPL_BrBG"      # New in PyNGL 1.5.0
    cnres.cnLinesOn       = False
    cnres.cnLineLabelsOn  = False
    cnres.cnFillMode             = "RasterFill"
    cnres.cnRasterSmoothingOn = False
    #cnres.cnLevels = inc

    # Labelbar resource
    cnres.lbOrientation   = "horizontal"
    cnres.lbBoxEndCapStyle= "TriangleBothEnds"
    cnres.lbLabelFontHeightF = 0.018
    cnres.pmLabelBarOrthogonalPosF = 0.02
    cnres.pmLabelBarWidthF = 0.6
    cnres.pmLabelBarHeightF = 0.1
    #pmLabelBarWidthF
    

    # Scalar field resources
    cnres.sfXArray        = lon
    cnres.sfYArray        = lat

    # Map resources
    cnres.mpFillOn               = True
    cnres.mpFillDrawOrder        = "PostDraw"
    cnres.mpLandFillColor        = "Transparent"
    cnres.mpOceanFillColor       = "Gray"
    cnres.mpInlandWaterFillColor = "Transparent"
    cnres.mpGridAndLimbOn      =  False                  #-- don't draw grid lines
    cnres.mpLimitMode = "LatLon"
    #res.mpGridLineColor = -1
    cnres.mpMaxLatF   = region_dict['latmax']           # select subregion
    cnres.mpMinLatF   = region_dict['latmin']
    cnres.mpMinLonF   = region_dict['lonmin']
    cnres.mpMaxLonF   = region_dict['lonmax']
    # Remove box around plot
    #cnres.pmTickMarkDisplayMode = "Never"
    cnres.lbLabelBarOn = True

    # Remove Lon/lat ticks
    cnres.tmXBOn = False
    cnres.tmYLOn = False
    cnres.tmXTOn = False
    cnres.tmYROn = False
    #cnres.gsnPanelBottom = 0.2
    #cnres.gsnPanelYWhiteSpacePercent = 20

    # Titles
    cnres.tiMainString = title
    
    return Ngl.contour_map(wks,dat,cnres), cnres, dat


def create_shading_layer(wks, mask_file, region_dict, title):
    
    f    = Nio.open_file(mask_file)
    dat  = f.variables["Q100"][:,:]
    lat  = f.variables["lat"][:]
    lon  = f.variables["lon"][:]

    cnres                 = Ngl.Resources()
    cnres.nglDraw  = False
    cnres.nglFrame = False
    cnres.nglMaximize = False
    #
    #cnres.gsnShadeFillType = "pattern"
    #cnres.gsnShadeHigh     = 1

    # Contour resources
    cnres.cnFillOn        = True
    
    cnres.cnMonoFillPattern = True
    cnres.cnFillPattern = 3
    cnres.cnMinLevelValF = 1
    #cnres.cnMaxLevelValF = 1
    
    #cnres.cnMonoFillPattern = False
    #cnres.cnFillPatterns = [-1,-1]
    cnres.cnFillColors      = 1
    #cnres.cnFillPatterns = [3,-1,-1]
    #cnres.cnMinLevelValF = 0.9
    #cnres.cnMaxLevelValF = 0.9
    
    cnres.cnLinesOn       = False
    cnres.cnLineLabelsOn  = False
        
    #cnres.cnFillMode             = "RasterFill"
    #cnres.cnRasterSmoothingOn = False

    # Scalar field resources
    cnres.sfXArray        = lon
    cnres.sfYArray        = lat

    # Map resources
    cnres.mpFillOn               = False
    #cnres.mpFillDrawOrder        = "PostDraw"
    #cnres.mpLandFillColor        = "Transparent"
    #cnres.mpOceanFillColor       = "Gray"
    #cnres.mpInlandWaterFillColor = "Transparent"
    cnres.mpGridAndLimbOn      =  False                  #-- don't draw grid lines
    
    cnres.mpLimitMode = "LatLon"
    #res.mpGridLineColor = -1
    cnres.mpMaxLatF   = region_dict['latmax']           # select subregion
    cnres.mpMinLatF   = region_dict['latmin']
    cnres.mpMinLonF   = region_dict['lonmin']
    cnres.mpMaxLonF   = region_dict['lonmax']
    # Remove box around plot
    cnres.pmTickMarkDisplayMode = "Never"
    cnres.lbLabelBarOn = False

    # Remove Lon/lat ticks
    cnres.tmXBOn = False
    cnres.tmYLOn = False
    cnres.tmXTOn = False
    cnres.tmYROn = False
    #cnres.gsnPanelBottom = 0.2
    #cnres.gsnPanelYWhiteSpacePercent = 20

    # Titles
    cnres.tiMainString = title
    
    #plot(1) = gsn_contour_shade(plot(1), 0, 15.5, cnres)
    #return Ngl.contour_map(wks,dat,cnres)
    return Ngl.contour_map(wks,dat,cnres)
    #Ngl.contour_shade(wks, dat, 


def layer_AR6_regions(wks, cnres):
    cnres2                 = cnres
    # Contour resources
    cnres2.cnFillOn        = False

    # Map resources
    cnres2.mpFillOn               = False
    return Ngl.map(wks,cnres2)
    #return Ngl.contour_map(wks, dat, cnres2)
    


inc = [-100, -80, -60, -40, -20, -10, 0, 10, 20, 40, 60, 80, 100]


title = 'Q100 discharge'
title = 'Q100 discharge'
scenario = 'RCP85'
horizon = '2100'
region_dict = dict(name='AFRICA',
                    lonmin = -25,
                    lonmax = 60,
                    latmin = -40,
                    latmax = 47
                   )

outfilename='Q100_test'

#do_map = True
#do_colorbar = True
wks_type = "png"

#if do_map:
wks = Ngl.open_wks(wks_type, outfilename)

#wmap, cnres, dat = create_Q100_map(wks, ncfile, region_dict, ' ')
wmap, cnres, dat = create_Q100_map(wks, mask_file1, region_dict, ' ')
shading_map = create_shading_layer(wks, mask_file, region_dict, ' ')

wmap_empty = layer_AR6_regions(wks, cnres)
# -- Add the AR6 regions
# -- Extract the subregions of the region
regions = retrieve_AR6regions_for_region(region_dict['name'])

#add_AR6regions(wks, wmap_empty, regions)
add_AR6regions(wks, shading_map, regions)

Ngl.overlay(wmap, shading_map)#, wmap_empty) 

Ngl.draw(wmap)
Ngl.draw(shading_map)
#Ngl.draw(wmap_empty)

txres                       = Ngl.Resources()  
txres.txFontHeightF         = 0.025

# Draw a text string labeling the marker
Ngl.text_ndc(wks,'Q100 discharge - RCP85 2100',0.5,0.83,txres)
#Ngl.text_ndc(wks,'',0.5,0.83,txres)
Ngl.text_ndc(wks,"(a)",0.22,0.83,txres)




Ngl.frame(wks)

Ngl.end()

#Image(outfilename+'.png')