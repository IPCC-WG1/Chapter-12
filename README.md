# Chapter 12

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

