import os


for ensemble in ['CMIP5', 'CMIP6', 'CORDEX-core']:
    #for figure in ['5', '6', '7', '8', '9', '10']:
    for figure in ['10']:
        outdir = '/home/jservon/Chapter12_IPCC/data/Figure_12.'+figure+'/Q100_'+ensemble
        if not os.path.isdir(outdir):
           os.makedirs(outdir)
        if figure=='5':
           CORDEX_domains = ['AFR']
        if figure=='6':
           CORDEX_domains = ['EAS','WAS','SEA']
        if figure=='7':
           CORDEX_domains = ['AUS']
        if figure=='8':
           CORDEX_domains = ['SAM','CAM']
        if figure=='9':
           CORDEX_domains = ['EUR']
        if figure=='10':
           CORDEX_domains = ['NAM','CAM']
        for CORDEX_domain in CORDEX_domains:
            cmd = 'cp /data/jservon/IPCC/Q100/20210309/percentiles_'+ensemble+'/*'+CORDEX_domain+'.txt /home/jservon/Chapter12_IPCC/data/Figure_12.'+figure+'/Q100_'+ensemble
            print cmd
            os.system(cmd)

#"/data/jservon/IPCC/Q100/20210309/percentiles_CORDEX-core/"
#/home/jservon/Chapter12_IPCC/data/

