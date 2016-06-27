import pickle
import numpy as np
import gmplot
import pandas as pd

# pip install gmplot
# use "2to3 -w *.py" to convert gmplot to python 3 (sudo it on unix-likes)
# you have to do this in the directory where the module gets installed
# on my system it goes to /Users/davidnola/anaconda/lib/python3.5/site-packages/gmplot

df = pickle.load(open('Location_pandas_data_barc.pkl','rb'))
N = 63
# t1 = df[df['topic']==15]
t1 = df[df['topics']==N]
t1 = t1[t1['gps_precision']==10.0]

print(t1.head())

#gmap = gmplot.GoogleMapPlotter(49.2827, -123.1207, 11)
gmap =gmplot.GoogleMapPlotter(41.390205, 2.154007, 11)

lats = t1['latitude'].tolist()
longs = t1['longitude'].tolist()
print(len(lats))

gmap.heatmap(lats, longs,dissipating=True,radius=40)
mymap = "mymap_barc"+ str(N)+".html"
gmap.draw(mymap)

#print(topics[:10])