import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv ('GrowLocations.csv') #reading and loading data into dataframe
# cleaning the grow data
clean = data[['Serial','Latitude','Longitude']] #taking only the necessary columns
clean = clean.drop_duplicates(subset = "Serial").rename(columns = {'Serial':'Name','Latitude':'Longitude','Longitude':'Latitude'})# taking one value per sensor and renaming columns
clean = clean.loc[(clean['Longitude'] >= -10.592) | (clean['Longitude'] <= 1.685)] #setting longitude bounds
clean = clean.loc[(clean['Latitude'] >= 50.681) | (clean['Latitude'] <= 57.985)] #setting latitude bounds
clean['Name'] = clean['Name'].str.split('.').str[0] #cleaning sensor names
clean = clean.reset_index().drop(columns = {'index'}) # rearranging reset_index
# plotting the data on the UK map
uk = plt.imread('map7.png') # reading input map
BBox = (-10.592,1.685,50.681,57.985) # map bounds which is also the x and y axis limits
fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(clean.Longitude, clean.Latitude, zorder=1, alpha= 0.2, c='b', s=10) # creating a scatter plot
ax.set_title('Geo Locations of GROW sensors')
ax.set_xlim(BBox[0],BBox[1])# setting x axis
ax.set_ylim(BBox[2],BBox[3])#setting y axis
ax.imshow(uk, zorder=0, extent = BBox, aspect= 'equal') #imposing the scatter plot on the map
plt.savefig('output_map.png')
plt.show() # output
