import xesmf as xe
import xarray as xr
import numpy as np


ds_out = xr.Dataset({'lat': (['lat'], np.arange(0, 75, 0.1)),
                     'lon': (['lon'], np.arange(20, 180, 0.1)),
                    }
                   )

regridder = xe.Regridder(ds, ds_out, 'bilinear')
#regridder = xe.Regridder(ds, ds_out, 'nearest_s2d')
dr = ds['mask']  # get a DataArray
dr_out = regridder(dr)
dr_out.to_netcdf('esmf01_test.nc') #regridder.clean_weight_file()




