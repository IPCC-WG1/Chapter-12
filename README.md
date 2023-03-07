# Chapter 12

**!!! the repository will be updated on the 1st of March (the latest) ; it is currently cleaned (removing unnecessary files) and some notebooks are re-structured to be more understandable**

## Presentation of the repository
This repository contains the code that has been used for a subset of Chapter 12 figures.

The folder **Figures** contains the **data** and **scripts** in the eponym subfolders, and the associated figures in the **fig** subfolder for:
- figures 12.4 to 12.10
- and S12.1 to S12.6

The files in the folder **HIcalculation** contain the scripts that were used to calculate NOAA heat index (HI), perform bias correction, and obtain the yearly number of days on which HI exceeds a value of 41 deg Celsius. HI exceedances are shown shown in IPCC Figure 12.4 and Figure SM 12.2.

The folder **snow** contains the code to compute SWE100 snow index.

### Description of the content of the Figures folder
Author: Jerome Servonnat

In this section I describe for each figure the scripts and data used to produce it.

#### Figure 12.4
**panels a, b, c**
- script: https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/scripts/global_figure_12.4/tx35_individual_figures.ipynb
- final plotted data in directory: https://github.com/IPCC-WG1/Chapter-12/tree/main/Figures/data/Figure_12.4/tx35
- figures in directory: https://github.com/IPCC-WG1/Chapter-12/tree/main/Figures/figs/global_figure_12.4
- panel a: 
  - data:
   - ensemble median: tx35_panel_a_ssp126_2081-2100_minus_baseline.nc
   - model agreement: mask_80perc-agreement_tx35_panel_a_ssp126_2081-2100_minus_baseline.nc
  - figure: panel_a_tx35_ssp126_2081-2100_80perc-agreement.[png/pdf]
- panel b: 
  - data:
   - ensemble median: tx35_panel_b_ssp585_2041-2060_minus_baseline.nc
   - model agreement: mask_80perc-agreement_tx35_panel_b_ssp585_2041-2060_minus_baseline.nc
  - figure: panel_b_tx35_ssp585_2041-2060_80perc-agreement.[png/pdf]
- panel c: 
  - data:
   - ensemble median: tx35_panel_c_ssp585_2081-2100_minus_baseline.nc
   - model agreement: mask_80perc-agreement_tx35_panel_c_ssp585_2081-2100_minus_baseline.nc
  - figure: panel_c_tx35_ssp585_2081-2100_80perc-agreement.[png/pdf]
- colorbar: tx35_colorbar.[png/pdf]

**panels d, e, f**
- script: https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/scripts/global_figure_12.4/HI_NOAA_individual_figures.ipynb
- final plotted data in directory: https://github.com/IPCC-WG1/Chapter-12/tree/main/Figures/data/Figure_12.4/HI41
- figures in directory: https://github.com/IPCC-WG1/Chapter-12/tree/main/Figures/figs/global_figure_12.4
- panel d: 
  - data:
   - ensemble median: HI41_panel_d_ssp126_2081-2100_minus_baseline.nc
   - model agreement: mask_80perc-agreement_HI41_panel_d_ssp126_2081-2100_minus_baseline.nc
  - figure: panel_d_HI41_ssp126_2081-2100_80perc-agreement.[png/pdf]
- panel e: 
  - data:
   - ensemble median: HI41_panel_e_ssp585_2041-2060_minus_baseline.nc
   - model agreement: mask_80perc-agreement_HI41_panel_e_ssp585_2041-2060_minus_baseline.nc
  - figure: panel_e_HI41_ssp585_2041-2060_80perc-agreement.[png/pdf]
- panel f: 
  - data:
   - ensemble median: tx35_panel_c_ssp585_2081-2100_minus_baseline.nc
   - model agreement: mask_80perc-agreement_HI41_panel_f_ssp585_2081-2100_minus_baseline.nc
  - figure: panel_f_HI41_ssp585_2081-2100_80perc-agreement.[png/pdf]
- colorbar: HI41_colorbar.[png/pdf]

**panels g, h, i**
- script: https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/scripts/global_figure_12.4/DF6_individual_figures.ipynb
- final plotted data in directory: https://github.com/IPCC-WG1/Chapter-12/tree/main/Figures/data/Figure_12.4/DF6
- figures in directory: https://github.com/IPCC-WG1/Chapter-12/tree/main/Figures/figs/global_figure_12.4
- panel g: 
  - data: 
   - ensemble median: DF6_panel_g_ssp126_farch_minus_baseline.nc
   - model agreement: mask_80perc-agreement_DF6_panel_g_ssp126_farch_minus_baseline.nc
  - figure: panel_g_DF6_ssp126_farch_80perc-agreement.[png/pdf]
- panel h: 
  - data: 
   - ensemble median: DF6_panel_h_ssp585_midch_minus_baseline.nc
   - model agreement: mask_80perc-agreement_DF6_panel_h_ssp585_midch_minus_baseline.nc
  - figure: panel_h_DF6_ssp585_midch_80perc-agreement.[png/pdf]
- panel i: 
  - data:
   - ensemble median: DF6_panel_i_ssp585_farch_minus_baseline.nc
   - model agreement: mask_80perc-agreement_DF6_panel_i_ssp585_farch_minus_baseline.nc
  - figure: panel_i_DF6_ssp585_farch_80perc-agreement.[png/pdf]
- colorbar: DF6_colorbar.[png/pdf]

**panels j, k, l**
- script: https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/scripts/global_figure_12.4/SoilMoisture_individual_figures.ipynb
- final plotted data in directory: https://github.com/IPCC-WG1/Chapter-12/tree/main/Figures/data/Figure_12.4/SM
- figures in directory: https://github.com/IPCC-WG1/Chapter-12/tree/main/Figures/figs/global_figure_12.4
- panel j: 
  - data: 
   - ensemble median: SM_panel_j_ssp126_2081-2100_minus_baseline.nc
   - model agreement: mask_80perc-agreement_SM_panel_j_ssp126_2081-2100_minus_baseline.nc
  - figure: panel_j_mrso_ssp126_2081-2100_80perc-agreement.[png/pdf]
- panel k: 
  - data: 
   - ensemble median: SM_panel_k_ssp585_2041-2060_minus_baseline.nc
   - model agreement: mask_80perc-agreement_SM_panel_k_ssp585_2041-2060_minus_baseline.nc
  - figure: panel_k_mrso_ssp585_2041-2060_80perc-agreement.[png/pdf]
- panel l: 
  - data:
   - ensemble median: SM_panel_l_ssp585_2081-2100_minus_baseline.nc
   - model agreement: mask_80perc-agreement_SM_panel_l_ssp585_2081-2100_minus_baseline.nc
  - figure: panel_l_mrso_ssp585_2081-2100_80perc-agreement.[png/pdf]
- colorbar: SM_colorbar.[png/pdf]

**panels m, n, o**
- script: https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/scripts/global_figure_12.4/wind_perc-baseline_individual_figures.ipynb
- final plotted data in directory: https://github.com/IPCC-WG1/Chapter-12/tree/main/Figures/data/Figure_12.4/sfcWind
- figures in directory: https://github.com/IPCC-WG1/Chapter-12/tree/main/Figures/figs/global_figure_12.4
- panel m: 
  - data: 
   - ensemble median: sfcWind_panel_m_ssp126_2081-2100_minus_baseline.nc
   - model agreement: mask_80perc-agreement_sfcWind_panel_m_ssp126_2081-2100_minus_baseline.nc
  - figure: panel_m_wind_ssp126_2081-2100_80perc-agreement.[png/pdf]
- panel n: 
  - data: 
   - ensemble median: sfcWind_panel_n_ssp585_2041-2060_minus_baseline.nc
   - model agreement: mask_80perc-agreement_sfcWind_panel_n_ssp585_2041-2060_minus_baseline.nc
  - figure: panel_n_wind_ssp585_2041-2060_80perc-agreement.[png/pdf]
- panel o: 
  - data:
   - ensemble median: sfcWind_panel_o_ssp585_2081-2100_minus_baseline.nc
   - model agreement: mask_80perc-agreement_sfcWind_panel_o_ssp585_2081-2100_minus_baseline.nc
  - figure: panel_o_wind_ssp585_2081-2100_80perc-agreement.[png/pdf]
- colorbar: wind_perc-baseline_colorbar.[png/pdf]

**panels p, q, r**
- script: https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/scripts/global_figure_12.4/ETWL_individual_figures.ipynb
- final plotted data in directory: https://github.com/IPCC-WG1/Chapter-12/tree/main/Figures/data/Figure_12.4/ETWL
- figures in directory: https://github.com/IPCC-WG1/Chapter-12/tree/main/Figures/figs/global_figure_12.4
- panel p: 
  - data: globalTWL_baseline.nc, globalTWL_RCP45.nc
  - figure: panel_p_ESL_2100_RCP45-final.[png/pdf]
- panel q: 
  - data: globalTWL_baseline.nc, globalTWL_RCP85.nc
  - figure: panel_q_ESL_2050_RCP85-final.[png/pdf]
- panel r: 
  - data: globalTWL_baseline.nc, globalTWL_RCP85.nc
  - figure: panel_r_ESL_2100_RCP85-final.[png/pdf]
- colorbar: ESL_colorbar.[png/pdf]


|Figure Number|Preview|How to produce the figure|Code|panels|
|---|---|---|---|---|
|12.4|<img src="https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/figs/global_figure_12.4/figure_12.4.png" alt="alt text" title="image Title" height="150"/>|[README](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/scripts/global_figure_12.4/README_figure_12.4)|[tx35: panels a, b, c](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/scripts/global_figure_12.4/tx35_individual_figures.ipynb)  [HI41: panels d, e, f](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/scripts/global_figure_12.4/DF6_individual_figures.ipynb)|[panel a](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/figs/global_figure_12.4/panel_a_tx35_ssp126_2081-2100_80perc-agreement.png)

[panel b](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/figs/global_figure_12.4/panel_b_tx35_ssp585_2041-2060_80perc-agreement.png)
| | | | | |
