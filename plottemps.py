#!/usr/bin/env python3
import matplotlib
matplotlib.use('Agg')
# --- Build Map ---
#import convert2dzi
import sys
import time
import os, shutil
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from subprocess import call
import pandas as pd
import numpy as np
import requests
from datetime import datetime
# --- Process Data ---
futureMax = datetime(2040,12,31,23,59) #really hope I'm not supporting this script after this date...
#map.drawmapscale(-119-6, 37-7.2, -119-6, 37-7.2, 500, barstyle='fancy', yoffset=20000)
try:
   stime = sys.argv[1]
except IndexError:
   stime = datetime.utcnow().timestamp()-3600 #go back an hour
try:
   etime = sys.argv[2]
except IndexError:
   etime =  datetime.utcnow().timestamp()
try:
   output_name = sys.argv[3]
except IndexError:
   output_name = 'rt_%s_%s.png' % (stime, etime)
# if sys.argv[1:]:
mins = 4
path = '/var/www/moped/http/us/roadtemp/MyDrive'
output_name = os.path.join(path, output_name)
#---------------------------------------------------------------------
#url = "http://ovation.gstwv.com/us/roadtemp/getRoadTemp.php?min=%s&start=%s&end=%s" % (mins, stime, etime); 
stimedt = datetime.fromtimestamp(int(stime))
etimedt = datetime.fromtimestamp(int(etime)) 
urlTimeFmt = '%Y-%m-%dT%H:%M:%S' #YYYY-MM-DDTHH:MM:SS
url = "http://sawi.gst.com/utilities/AttChecker/attCheckController.php?beginTimedate=%s&endTimedate=%s&attributes=3&format=json"
# 5min processing for 30min data
rjs = requests.get(url % (stimedt.strftime(urlTimeFmt),etimedt.strftime(urlTimeFmt)))
rjsJ = rjs.json()

#theurl = url % (stimedt.strftime(urlTimeFmt),etimedt.strftime(urlTimeFmt))
#print("URL: %s" % theurl );
#======================================================================
#local file for testing purposes
#import json
#filename = "RTTestJson.txt"
#with open(filename) as jfile:
#   rjsJ = json.load(jfile)
#======================================================================
df = pd.DataFrame(rjsJ, dtype=np.float32)
vplt = plt.figure(figsize=(10,8), edgecolor=None)
#ax1 = vplt.add_axes([0.05, 0.80, 0.9, 0.15])
m = Basemap(llcrnrlon=-125.671,llcrnrlat=24.4769,urcrnrlon=-66.5202,urcrnrlat=49.4391, epsg=4326)
#http://server.arcgisonline.com/arcgis/rest/services
#try local copy first
try:
    from PIL import Image
    m.imshow(Image.open('USAStreetMap.png'),origin='upper',alpha=0.6)
except FileNotFoundError as err:
    #arcgisimage occasionally fails to download properly try,try again
    while True:
        try:
           m.arcgisimage(service='ESRI_StreetMap_World_2D', xpixels=3500,alpha=0.6)
        except RuntimeError as err:
           pass
        else:
           break
#---------------------------------------------------------------------
vvmin = -10 #min temp for scale
vvmax = 50  #max temp for scale
vstep = 10  #step between ticks
#make colour normalization scale over vvmin to vvmax
vnorm = Normalize(vmin=vvmin,vmax=vvmax)
#---------------------------------------------------------------------
#c sets marker colour based on the values in temp variable
scplt = plt.scatter(x=df.longitude,y=df.latitude,c=df.road_temperature,s=1,norm=vnorm,cmap=plt.cm.gist_rainbow_r,edgecolor=None,lw=0,alpha=0.8)
#cbar = plt.colorbar(orientation='horizontal',norm=vnorm,shrink=0.625,aspect=30,fraction=0.5,pad=0.05,extend='both')
#cbar.set_label('Road Temperature')
#ticks = np.arange(vvmin,vvmax+1,vstep)
#cbar.set_ticks(ticks)
#cbar.set_ticklabels(ticks)

#for i, vid in enumerate(df.vid):
#    plt.annotate(vid, (df.longitude[i],df.latitude[i]))

if os.path.exists(output_name):
    os.remove(output_name)
#--------------------------------------------------------------------
plt.savefig(output_name,dpi=500,transparent=True,bbox_inches='tight')
#plt.show()
print("%s" % output_name);
#---------------------------------------------------------------------
#---------------------------------------------------------------------
dzi_name = output_name[:-3] + "dzi"
if os.path.exists(dzi_name):
    os.remove(dzi_name)
    folder = dzi_name[:-4] + "_files"
    shutil.rmtree(folder);
#------------------------------------------------
###cmd = "/usr/bin/python2.7 /var/www/http/convert2dzi.py %s %s" % (output_name, dzi_name);
cmd = ["/usr/bin/python2.7","/var/www/http/convert2dzi.py",output_name,dzi_name];
call(cmd);

#convert2dzi.main(output_name, dzi_name )
#---------------------------------------------------------------------
