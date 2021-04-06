# Chapter 12

The files in this repository contain the scripts that were used to calculate NOAA heat index (HI), which is shown in IPCC Figure 12.4 and Figure SM 12.2.

The files are structured as follows:
1) EXE0_create_model_overview.ipynb: This file creates the model lists which are subsequently used by the main scripts (scripts starting with EXE1 and EXE2). The model lists are stored as txt-files in the subfolder "Model_lists"
2) EXE1_...: These are the main scripts to calculate HI for CMIP5, CMIP6, and CORDEX data. First, HI is calculated and bias adjustment is performed using the QDM method with WFDE5 as reference dataset. Subsequently, the yearly number of exceedances above 27 degC, 32 degC, and 41 degC is computed.
3) EXE2_Prepare_data_for_IPCC.ipynb: This file prepares the final files containing the threshold exceedances above 27 degC, 32 degC, and 41 degC for CMIP5, CMIP6, and the CORDEX regions to be used for plotting Figure 12.4 and Figure SM 12.2 in IPCC AR6 WG1. A single NetCDF file is produced For every model, every time period, every scenario, and every threshold.

The functions that are used be the different scripts can be found in the subfolder "functions"