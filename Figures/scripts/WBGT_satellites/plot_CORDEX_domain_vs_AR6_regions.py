import Ngl, Nio
import os, numpy, csv, json
from IPython.display import Image
from shapely.geometry import Polygon, Point
import geopandas
import sys

CORDEX_domain = sys.argv[1]
ncfile = sys.argv[2]
trim_figure = sys.argv[3]

#ncfile = cfile(rgrd_dat)

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
            #if region_name in row[0]:
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
    txres.txFontHeightF         = 0.010
    
    gsres                   = Ngl.Resources()
    # Polyline resources.
    gsres.gsLineColor       = "Black"
    gsres.gsLineThicknessF  = 3.0      # thrice thickness

    for subregion in regions:
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


def create_Q100_map(wks, ncfile, region_dict, title):
    
    f    = Nio.open_file(ncfile)
    dat  = f.variables["WBGTindoor"][0,:,:]
    lat  = f.variables["lat"][:]
    lon  = f.variables["lon"][:]

    cnres                 = Ngl.Resources()
    cnres.nglDraw  = False
    cnres.nglFrame = False
    cnres.nglMaximize = False

    # Contour resources
    cnres.cnFillOn        = True
    cnres.cnLevelSelectionMode = "ManualLevels"
    cnres.cnLevelSpacingF      = 10
    cnres.cnMinLevelValF       = -100
    cnres.cnMaxLevelValF       = 100

    cnres.cnFillPalette   = "NCV_jet"      # New in PyNGL 1.5.0
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

    # Titles
    cnres.tiMainString = title
    
    return Ngl.contour_map(wks,dat,cnres), cnres, dat



def layer_AR6_regions(wks, cnres):
    cnres2                 = cnres
    # Contour resources
    cnres2.cnFillOn        = False

    # Map resources
    cnres2.mpFillOn               = False
    return Ngl.map(wks,cnres2)
    #return Ngl.contour_map(wks, dat, cnres2)
    


inc = [0, 10, 20, 40, 60, 80, 100, 200, 300]


region_dict = dict(name='World',
                    lonmin = -180,
                    lonmax = 180,
                    latmin = -90,
                    latmax = 90
                   )

outfilename=CORDEX_domain+'_vs_AR6_regions'

wks_type = "png"

wks = Ngl.open_wks(wks_type, outfilename)

wmap, cnres, dat = create_Q100_map(wks, ncfile, region_dict, ' ')

# -- Add the AR6 regions
regions = retrieve_AR6regions_for_region('all')
wmap_empty = layer_AR6_regions(wks, cnres)
add_AR6regions(wks, wmap_empty, regions)

Ngl.overlay(wmap, wmap_empty) 

Ngl.draw(wmap)
Ngl.draw(wmap_empty)

txres                       = Ngl.Resources()  
txres.txFontHeightF         = 0.025

# Draw a text string labeling the marker
Ngl.text_ndc(wks,CORDEX_domain,0.5,0.67,txres)
#Ngl.text_ndc(wks,'0.6',0.5,0.6,txres)


Ngl.frame(wks)

Ngl.end()

from PIL import Image as PILImage

def extract_plot(figure_file,trim_figure) :
    im = PILImage.open(figure_file)
    #box=(left, upper, right, lower).
    im_crop = im.crop((200, 300, 820, 725))
    im_crop.save(trim_figure, quality=95)
#
#trim_figure = '/home/jservon/Chapter12_IPCC/figs/CORDEX_domains_vs_AR6_regions/'+CORDEX_domain+'.png'
# -- Extract the colorbar
extract_plot(outfilename+'.png',trim_figure)
#Image(trim_figure)
#Image(outfilename+'.png')