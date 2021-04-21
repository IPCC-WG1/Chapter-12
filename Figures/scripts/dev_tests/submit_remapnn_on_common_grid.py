import os

lof = [
#'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/WAS_maskout.nc',
#'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/WAS_SAS_data.nc',
#'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/EAS_maskout.nc',
#'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/EAS_SAS_data.nc',
#'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/EAS_WCA_maskout.nc',
#'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/SEA_SEA_data.nc'

#'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/WAS_Q100_ensmedian.nc',
#'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/EAS_Q100_ensmedian.nc'
'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/EAS/EAS_rcp85_late_change_model3.nc',
'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/EAS/EAS_rcp85_late_change_model2.nc',
'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/EAS/EAS_rcp85_late_change_model1.nc',
'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/EAS/EAS_rcp85_late_change_model0.nc',
'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/EAS/EAS_rcp85_late_change_model5.nc',
'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/EAS/EAS_rcp85_late_change_model4.nc',
'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/WAS/WAS_rcp85_late_change_model3.nc',
'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/WAS/WAS_rcp85_late_change_model2.nc',
'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/WAS/WAS_rcp85_late_change_model1.nc',
'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/WAS/WAS_rcp85_late_change_model0.nc',
'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/WAS/WAS_rcp85_late_change_model5.nc',
'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/WAS/WAS_rcp85_late_change_model4.nc',
'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/SEA/SEA_rcp85_late_change_model3.nc',
'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/SEA/SEA_rcp85_late_change_model2.nc',
'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/SEA/SEA_rcp85_late_change_model1.nc',
'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/SEA/SEA_rcp85_late_change_model0.nc',
'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/SEA/SEA_rcp85_late_change_model5.nc',
'/home/jservon/Chapter12_IPCC/data/ASIA_map_fig_Q100/SEA/SEA_rcp85_late_change_model4.nc',

]

for wfile in lof:
    cmd = 'qsub -q std -v in='+wfile.replace('.nc','')+' -j eo remapnn_job.sh'
    print cmd
    os.system(cmd)

