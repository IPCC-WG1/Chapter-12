#!/bin/bash

cd ~/Chapter12_IPCC/scripts/dev_tests
echo ${in}
cdo remapnn,ASIA_raw_common_grid.nc ${in}.nc ${in}_common_grid.nc

