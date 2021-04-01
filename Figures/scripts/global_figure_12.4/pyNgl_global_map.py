import Ngl, Nio
import os, numpy, csv, json
from IPython.display import Image
from shapely.geometry import Polygon, Point
import geopandas
import regionmask


from optparse import OptionParser
parser = OptionParser("")
parser.set_usage("")
parser.add_option("--dat_file",
                  help="Input netcdf file",
                  action="store", default=None)
parser.add_option("--hatching_file",
                  help="Input netcdf file for hatching",
                  action="store", default=None)
parser.add_option("--variable",
                  help="Variable",
                  action="store", default=None)
parser.add_option("--color",
                  help="color palette",
                  action="store", default=None)
parser.add_option("--colors",
                  help="Color levels",
                  action="store", default=None)
parser.add_option("--title",
                  help="Title",
                  action="store", default=' ')
parser.add_option("--scenario",
                  help="socio economic scenario",
                  action="store", default='scenario')
parser.add_option("--horizon",
                  help="period / horizon",
                  action="store", default='horizon')
parser.add_option("--gsnCenterString",
                  help="Subtitle",
                  action="store", default=' ')
parser.add_option("--is_3D",
                  help="set to 'False' if there is no time dimension in dat_file",
                  action="store", default='True')
parser.add_option("--variable_name",
                  help="name of the variable to be used in the output netcdf file (if different from the variable)",
                  action="store", default=None)
parser.add_option("--perc_agreement_hatching",
                  help="percentage of model agreement used",
                  action="store", default=None)
parser.add_option("--figname",
                  help="Name of the final figure",
                  action="store", default=None)


(opts, args) = parser.parse_args()

dat_file = opts.dat_file
hatching_file = opts.hatching_file
variable = opts.variable
color = opts.color
color_levels = opts.colors
title = opts.title
scenario = opts.scenario
horizon = opts.horizon
gsnCenterString = opts.gsnCenterString
is_3D = opts.is_3D
variable_name = opts.variable_name
if not variable_name:
    variable_name = variable
perc_agreement_hatching = opts.perc_agreement_hatching
trim_figure = opts.figname




# -- Creating the map with the colors and grey shading over the oceans
def create_map(wks, dat_file, variable, color_levels, is_3D='True'):
    
    f    = Nio.open_file(dat_file)
    if is_3D=='True':
        dat  = f.variables[variable][0,:,:]
    else:
        dat  = f.variables[variable][:,:]
    lat  = f.variables["lat"][:]
    lon  = f.variables["lon"][:]
    

    cnres                 = Ngl.Resources()
    cnres.nglDraw  = False
    cnres.nglFrame = False
    cnres.nglMaximize = False

    # Contour resources
    cnres.cnFillOn        = True
    cnres.cnLevelSelectionMode = "ExplicitLevels"
    # -- values for the explicit levels
    levels = []
    for elt in color_levels.split(' '):
        levels.append(float(elt))
    cnres.cnLevels    = levels
    #
    # -- Create IPPC colorpalettes 
    misc_div_21_raw = [
        [8, 29, 88],
        [31, 47, 136],
        [35, 77, 160],
        [31, 114, 177],
        [36, 152, 192],
        [65, 182, 195],
        [115, 200, 188],
        [170, 222, 182],
        [214, 239, 178],
        [240, 249, 185],
        [254, 254, 209],
        [255, 240, 169],
        [254, 225, 135],
        [254, 201, 101],
        [253, 170, 72],
        [253, 141, 60],
        [252, 90, 45],
        [237, 47, 33],
        [211, 15, 31],
        [176, 0, 38],
        [128, 0, 38]]

    wind_colormap = [
        [.169, .098, .298],
        [.165, .169, .369],
        [.161, .243, .443],
        [.176, .322, .518],
        [.239, .408, .584],
        [.333, .490, .647],
        [.239, .408, .584],
        [.333, .490, .647],
        [.443, .576, .706],
        [.553, .659, .765],
        [.667, .745, .824],
        [.776, .831, .878],
        [.855, .898, .898],
        [.812, .886, .824],
        [.718, .831, .725],
        [.616, .773, .627],
        [.514, .714, .533],
        [.416, .655, .435],
        [.322, .588, .329],
        [.263, .502, .224],
        [.251, .424, .137],
        [.255, .357, .071],
        [.259, .298, .008]
    ]
    test = []
    for elt in wind_colormap:
        tmp = []
        for eelt in elt:
            tmp.append(eelt)
        tmp.append(1.)
        test.append(tmp)
    wind_palette = numpy.array(test)
    if color=='wind':
        colorpalette = wind_palette
    else:
        colorpalette = color
    cnres.cnFillPalette   = colorpalette      # New in PyNGL 1.5.0
    cnres.cnLinesOn       = True
    cnres.cnLineLabelsOn  = False
    #cnres.cnFillMode             = "RasterFill"
    cnres.cnRasterSmoothingOn = False

    # Labelbar resource
    cnres.lbOrientation   = "horizontal"
    cnres.lbBoxEndCapStyle= "TriangleBothEnds"
    cnres.lbLabelFontHeightF = 0.014
    cnres.pmLabelBarOrthogonalPosF = 0.02
    cnres.pmLabelBarWidthF = 0.6
    cnres.pmLabelBarHeightF = 0.15
    

    # Scalar field resources
    cnres.sfXArray        = lon
    cnres.sfYArray        = lat

    cnres.mpOutlineOn     = False
    cnres.mpGridAndLimbOn = True
    cnres.mpGridLineColor = -1
    cnres.mpFillOn               = True
    cnres.mpFillDrawOrder        = "PostDraw"
    cnres.mpLandFillColor        = "Transparent"
    cnres.mpOceanFillColor       = "grey"
    cnres.mpInlandWaterFillColor = "grey"
    # Remove box around plot
    cnres.pmTickMarkDisplayMode = "Never"

    cnres.mpProjection = 'Robinson'
    cnres.mpCenterLonF = 0
    cnres.lbLabelBarOn = True

    # Remove Lon/lat ticks
    cnres.tmXBOn = False
    cnres.tmYLOn = False
    cnres.tmXTOn = False
    cnres.tmYROn = False

    # Titles
    cnres.tiMainString = ' '
    
    return Ngl.contour_map(wks,dat,cnres), cnres, dat


# -- Create the layer with the shading/hatching
def create_shading_layer(wks, hatching_file, variable, is_3D='True'):
    
    # -- Get the hatching data
    f = Nio.open_file(hatching_file)
    lat  = f.variables["lat"][:]
    lon  = f.variables["lon"][:]
    
    # -- Make a mask to mask hatching over the oceans
    mask = regionmask.defined_regions.natural_earth.land_110.mask(lon, lat) + 1

    import xarray as xr
    test = xr.where(mask==1, 0, 1)
    if is_3D=='True':
        dat  = f.variables[variable][0,:,:] + test
    else:
        dat  = f.variables[variable][:,:] + test
    lat  = f.variables["lat"][:]
    lon  = f.variables["lon"][:]

    cnres                 = Ngl.Resources()
    cnres.nglDraw  = False
    cnres.nglFrame = False
    cnres.nglMaximize = False
    #
    # Remove box around plot
    cnres.pmTickMarkDisplayMode = "Never"

    # Contour resources
    cnres.cnFillOn        = True
    cnres.cnMonoFillPattern = False
    cnres.cnFillPatterns = [3,-1]  # --> Pattern 3 is the diagonal shading
    cnres.cnLevelSelectionMode='ExplicitLevels'
    cnres.cnLevels = [0.9]  # --> Here you pass the value of the threshold below which you want to shade
    cnres.cnLinesOn       = False 
    cnres.cnLineLabelsOn  = False
    cnres.cnFillColors      = [ 1, 1] # --> Only the first value is important, and 1 means black
    cnres.cnFillScales      = [ 0.5, 1] # --> This is the spacing between the lines; default is 1

    # Scalar field resources
    cnres.sfXArray        = lon
    cnres.sfYArray        = lat

    # Map resources
    cnres.mpFillOn               = False
    cnres.mpGridAndLimbOn      =  False                  #-- don't draw grid lines
    
    cnres.mpProjection = 'Robinson'
    cnres.mpCenterLonF = 0
    cnres.mpLimitMode = "LatLon"
    # Remove box around plot
    cnres.pmTickMarkDisplayMode = "Never"
    cnres.lbLabelBarOn = False

    # Remove Lon/lat ticks
    cnres.tmXBOn = False
    cnres.tmYLOn = False
    cnres.tmXTOn = False
    cnres.tmYROn = False

    # Titles
    cnres.tiMainString = ' '
    
    return Ngl.contour_map(wks,dat,cnres)



# -- Now let's build the plot
# -----------------------------------------------------------

# -- name of the tmp file
outfilename = '/data/jservon/tmp'

# -- Open device
wks_type = "png"
wks = Ngl.open_wks(wks_type, outfilename)

# -- Create color map
wmap, cnres, dat = create_map(wks, dat_file, variable, color_levels, is_3D=is_3D)

# -- Create hatching map
hatching_map = create_shading_layer(wks, hatching_file, variable, is_3D=is_3D)

# -- Overlay map and hatching and draw maps
Ngl.overlay(wmap, hatching_map)
Ngl.draw(wmap)
Ngl.draw(hatching_map)


# -- Add subtitle
txres                       = Ngl.Resources()  
txres.txFontHeightF         = 0.025
Ngl.text_ndc(wks,gsnCenterString,0.5,0.68,txres)

# -- Add title
tmainxres                       = Ngl.Resources()  
tmainxres.txFontHeightF         = 0.027
tmainxres.txFont         = 22
Ngl.text_ndc(wks,title,0.5,0.72,tmainxres)

Ngl.frame(wks)
Ngl.end()


# -- Trim the figure and extract the colorbar
# -----------------------------------------------
from PIL import Image as PILImage

def extract_plot(figure_file,trim_figure) :
    im = PILImage.open(figure_file)
    #box=(left, upper, right, lower).
    im_crop = im.crop((204, 261, 820, 667))
    im_crop.save(trim_figure, quality=95)

extract_plot(outfilename+'.png',trim_figure)
