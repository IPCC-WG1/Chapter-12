#!/bin/bash
######################
## CURIE   TGCC/CEA ##
######################
#MSUB -r C-ESM-EP_job
#MSUB -eo
#MSUB -n 1              # Reservation du processus
#MSUB -T 36000          # Limite de temps elapsed du job
#MSUB -q standard
##MSUB -Q normal
#MSUB -A devcmip6
set +x
# -------------------------------------------------------- >
# --
# -- Script to run a CliMAF atlas on Ciclad:
# --   - sets up the environment
# --   - specify the parameter file and the season
# --   - automatically sets up the CliMAF cache
# --   - and run the atlas
# --
# --
# --     Author: Jerome Servonnat
# --     Contact: jerome.servonnat__at__lsce.ipsl.fr
# --
# --
# -------------------------------------------------------- >
date


# -- On doit pouvoir le soumettre en batch, ou le soumettre en interactif dans le repertoire de la composante
# -> # -- On doit pouvoir le soumettre en batch, ou le soumettre en interactif dans le repertoire de la composante

# -> Separer le cas batch et le cas interactif : identifier les deux

# -- Setup the environment...
# -------------------------------------------------------- >
cd /home/jservon/Chapter12_IPCC/scripts/wind_satellites
python compute_regional_averages_CORDEX.py

