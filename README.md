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

In the following section I present for each figure (identified in first column) the links to:
- the figure (before final editing) (second column)
- the main README, and the repositories to the code and the data (third column)
- the code for each panel(s)
- the figures of the individual panels

|Figure Number|Preview|How to produce the figure|Panels to code|Individual panels|
|---|---|---|---|---|
|12.4|<img src="https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/figs/global_figure_12.4/figure_12.4.png" alt="alt text" title="image Title" height="150"/>|[README](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/scripts/global_figure_12.4/README_figure_12.4)<br>[Code repository](https://github.com/IPCC-WG1/Chapter-12/tree/main/Figures/scripts/global_figure_12.4)<br>[Data repository](https://github.com/IPCC-WG1/Chapter-12/tree/main/Figures/data/Figure_12.4)|[tx35: panels a, b, c](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/scripts/global_figure_12.4/tx35_individual_figures.ipynb)<br>[HI41: panels d, e, f](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/scripts/global_figure_12.4/HI_NOAA_individual_figures.ipynb)<br>[DF6: panels g, h, i](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/scripts/global_figure_12.4/DF6_individual_figures.ipynb)<br>[SoilM: panels j, k, l](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/scripts/global_figure_12.4/SoilMoisture_individual_figures.ipynb)<br>[wind: panels m, n, o](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/scripts/global_figure_12.4/wind_perc-baseline_individual_figures.ipynb)<br>[ESL: panels p, q, r](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/scripts/global_figure_12.4/ETWL_individual_figures.ipynb)|[a](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/figs/global_figure_12.4/panel_a_tx35_ssp126_2081-2100_80perc-agreement.png), [b](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/figs/global_figure_12.4/panel_b_tx35_ssp585_2041-2060_80perc-agreement.png), [c](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/figs/global_figure_12.4/panel_c_tx35_ssp585_2081-2100_80perc-agreement.png)<br>[d](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/figs/global_figure_12.4/panel_d_HI41_ssp126_2081-2100_80perc-agreement.png), [e](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/figs/global_figure_12.4/panel_e_HI41_ssp585_2041-2060_80perc-agreement.png), [f](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/figs/global_figure_12.4/panel_f_HI41_ssp585_2081-2100_80perc-agreement.png)<br>[g](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/figs/global_figure_12.4/panel_g_DF6_ssp126_farch_80perc-agreement.png), [h](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/figs/global_figure_12.4/panel_h_DF6_ssp585_midch_80perc-agreement.png), [i](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/figs/global_figure_12.4/panel_i_DF6_ssp585_farch_80perc-agreement.png)<br>[j](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/figs/global_figure_12.4/panel_j_mrso_ssp126_2081-2100_80perc-agreement.png), [k](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/figs/global_figure_12.4/panel_k_mrso_ssp585_2041-2060_80perc-agreement.png), [l](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/figs/global_figure_12.4/panel_l_mrso_ssp585_2081-2100_80perc-agreement.png)<br>[m](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/figs/global_figure_12.4/panel_m_wind_ssp126_2081-2100_80perc-agreement.png), [n](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/figs/global_figure_12.4/panel_n_wind_ssp585_2041-2060_80perc-agreement.png), [o](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/figs/global_figure_12.4/panel_o_wind_ssp585_2081-2100_80perc-agreement.png)<br>[p](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/figs/global_figure_12.4/panel_p_ESL_2100_RCP45-final.png), [q](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/figs/global_figure_12.4/panel_q_ESL_2050_RCP85-final.png), [r](https://github.com/IPCC-WG1/Chapter-12/blob/main/Figures/figs/global_figure_12.4/panel_r_ESL_2100_RCP85-final.png)
| | | | | |
