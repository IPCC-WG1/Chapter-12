import os
import glob

datadir = '/home/jservon/Chapter12_IPCC/data/'

lof = glob.glob(datadir+'Figure_12.*/*divdra*.nc')

for wfile in lof:
    wfilename = os.path.basename(wfile)
    wdir = os.path.dirname(wfile)
    dum = wdir.split('/')
    tmpfigure = dum[len(dum)-1]
    if not 'Q100_map_panel_a' in wfile:
        targetfile = wdir+'/Q100_map_panel_a_'+wfilename
        cmd = 'mv '+wfile+' '+targetfile
        print cmd
        os.system(cmd)
    else:
        targetfile = wfile
    cmd = 'ncatted -O -a comment,global,o,c,"This file is used for panel a of '+tmpfigure+' of IPCC AR6 Chapter 12 ; provided by Fabio Di Sante, ICTP (fdi_sant at ictp.it)" '+targetfile
    print cmd
    os.system(cmd)
