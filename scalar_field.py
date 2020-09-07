import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt 
import os
import matplotlib.ticker as mticker  
import sys
import argparse
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as tri
from matplotlib.mlab import griddata
from mpl_toolkits.basemap import Basemap
import scipy.interpolate


#SSS_file = open("/home/kunika/Desktop/Data_Visualisation_assignment_01/CD732-Datathon-1/SSS/001_29_Dec_2003.txt", 'r' )
root_folder = sys.argv[1]
print(root_folder)
scalar_quantity = sys.argv[2]
mapping_style = sys.argv[3]
if os.path.exists(root_folder + '/Results/' + mapping_style + "/" + scalar_quantity):
	pass
else:
	os.makedirs(root_folder + '/Results/' + mapping_style + "/" + scalar_quantity)
data_folder = "/home/kunika/Desktop/Data_Visualisation_assignment_01/CD732-Datathon-1/" + scalar_quantity
results_dir = root_folder + '/Results/' + mapping_style + "/" + scalar_quantity + "/"

max_list = []
min_list = []

for fname in sorted(os.listdir(data_folder)):
	if fname.endswith(".txt"):
		data = pd.read_csv(os.path.join(data_folder, fname), header=0, skiprows= 9)
		cols = [scalar_quantity, 'TIME', 'LAT', 'LON']
		data[cols] = data[cols].mask(np.isclose(data[cols].values, -1.000000e+34))
		data_processed = data.dropna()
		Scalar_min = np.min(data_processed[scalar_quantity])
		Scalar_max = np.max(data_processed[scalar_quantity])
		max_list.append(Scalar_max)
		min_list.append(Scalar_min)

min_in_Scalar = np.min(min_list)
max_in_Scalar = np.max(max_list)

print(min_in_Scalar, max_in_Scalar)
count = 0

for fname in sorted(os.listdir(data_folder)):

	count = count + 1
	if count > int(sys.argv[5]):
		break
	elif fname.endswith(".txt") and count >= int(sys.argv[4]):
		data = pd.read_csv(os.path.join(data_folder, fname), header=0, skiprows= 9)
		cols = [scalar_quantity, 'TIME', 'LAT', 'LON']
		data[cols] = data[cols].mask(np.isclose(data[cols].values, -1.000000e+34))
		min_LAT = np.min(data.LAT)
		max_LAT = np.max(data.LAT)
		min_LON = np.min(data.LON)
		max_LON = np.max(data.LON)
		data_processed = data.dropna()
		
		c = data_processed[scalar_quantity]																						
		
		if mapping_style == "color":
			fig, ax1 = plt.subplots()
			fig.set_size_inches(17, 10)
			ax1.set_xlabel('LON')
			ax1.set_ylabel('LAT')
		
			ax1.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
			ax1.set_title('ColorMap for %s %s' %(scalar_quantity, fname))
			plt.scatter( data_processed['LON'], data_processed['LAT'] , c=c, vmin=min_in_Scalar, vmax=max_in_Scalar, marker= "*", cmap =plt.cm.viridis)
			plt.ylim(min_LAT, max_LAT)
			plt.xlim(min_LON, max_LON)
			plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%d °E'))
			plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d °N'))
			cbar = plt.colorbar()
			cbar.set_label(scalar_quantity)
			#base = os.path.splitext(fname)[0]
			new_fname = fname.replace(".txt", ".png")
			print(new_fname)
			plt.savefig(results_dir + new_fname)


		elif mapping_style == "contour":
			# data_processed =  data_processed.to_frame()
			# # x = data_processed['LON']
			# # y = data_processed['LAT']
			# triang = tri.Triangulation(data_processed['LON'],data_processed['LAT'])
			# triang.set_mask(np.hypot(data_processed['LAT'][triang.triangles].mean(axis=1),
   #                       data_processed['LON'][triang.triangles].mean(axis=1))
   #              < min_radius)
   			fig, ax1 = plt.subplots()
   			n = Basemap( lat_0=0, lon_0=3,llcrnrlon=data_processed['LON'].min(), 
                  llcrnrlat= data_processed['LAT'].min(), 
                  urcrnrlon=data_processed['LON'].max(), 
                  urcrnrlat=data_processed['LAT'].max())
   			n.fillcontinents(color = 'white')
   			parallels = np.arange(data_processed['LAT'].min(), data_processed['LAT'].max(), 15.)
   			n.drawparallels(np.arange(data_processed['LAT'].min(), data_processed['LAT'].max(), 15.), color = 'black', linewidth = 0.5)
   			n.drawparallels(parallels,labels=[True,False,False,False])
   			meridians = np.arange(data_processed['LON'].min(),data_processed['LON'].max(), 15.)
   			n.drawmeridians(np.arange(data_processed['LON'].min(),data_processed['LON'].max(), 15.), color = '0.25', linewidth = 0.5)
   			n.drawmeridians(meridians,labels=[False,False,False,True])
			
			

   			# n.drawmeridians(meridians,labels=[True,False,False,True])
   			# numcols = 1000
   			# numrows = 1000
   			# xi = np.linspace(data_processed['LON'].min(), data_processed['LON'].max(), numcols)
   			# yi = np.linspace(data_processed['LAT'].min(), data_processed['LAT'].max(), numrows)
   			# xi, yi = np.meshgrid(xi, yi)
   			# x, y, z = data_processed['LON'].values, data_processed['LAT'].values, c.values
   			# zi = griddata(x, y, z, xi, yi)
   			
   			fig.set_size_inches(17, 10)
   			ax1.set_xlabel('LON',  labelpad=50)
   			ax1.set_ylabel('LAT',  labelpad=80)
   			ax1.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
   			ax1.set_title('ContourMap for %s %s' %(scalar_quantity, fname))
   			# plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%d °E'))
   			# plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d °N'))
   			plt.tricontourf(data_processed['LON'], data_processed['LAT'], c, alpha=0.6, vmin=min_in_Scalar, vmax=max_in_Scalar,  cmap =plt.cm.viridis)
   			m = plt.cm.ScalarMappable(cmap= plt.cm.viridis)
   			m.set_array(c)
   			m.set_clim(min_in_Scalar, max_in_Scalar)
   			cbar = plt.colorbar(m)
   			cbar.set_label(scalar_quantity)
   			new_fname = fname.replace(".txt", ".png")
   			print(new_fname)
   			plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%d °E'))
   			plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d °N'))
   			plt.savefig(results_dir + new_fname)


			# x_mesh, y_mesh = np.meshgrid(data_processed['LON'], data_processed['LAT'], sparse= True, copy = False)
			# plt.contourf(x_mesh, y_mesh, c)
			# xi = np.linspace(4, 8, 10)
			# yi = np.linspace(1, 4, 10)
			# zi = matplotlib.mlab.griddata(data_processed['LON'], data_processed['LAT'], c, xi, yi, interp='linear')

			# ax1.fillcontinents(color='white')
			# contour.fillcontinents(color = 'white')
			


			

		elif mapping_style == "elevation":
			fig = plt.figure(figsize=(17,10))


			ax = fig.gca(projection='3d')
			ax.xaxis.set_major_formatter(mticker.FormatStrFormatter('%d °E'))
			ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%d °N'))
			#fig.set_size_inches(17, 10)
			z = []
			for i in c:
				q = (i - np.min(c))/(np.max(c) - np.min(c)) * 30
				z.append(q)

			# print(z)





			# #x_mesh, y_mesh = np.meshgrid(data_processed['LON'], data_processed['LAT'])
			ax.set_title('ElevationMap for %s %s' %(scalar_quantity, fname))
			ax.plot_trisurf(data_processed['LON'], data_processed['LAT'] , z, cmap=plt.cm.viridis,
			           linewidth=0, antialiased=False)

			# ax.set_zlim(min_in_Scalar, max_in_Scalar
			# m = cm.ScalarMappable(cmap=cm.jet)
			# m.set_array(z)
			# plt.colorbar(m)
			m = plt.cm.ScalarMappable(cmap= plt.cm.viridis)
			m.set_array(z)
			m.set_clim(min_in_Scalar, max_in_Scalar)
			cbar = plt.colorbar(m)
			# cbar = plt.colorbar()
			cbar.set_label(scalar_quantity)


			new_fname = fname.replace(".txt", ".png")
			print(new_fname)
			plt.savefig(results_dir + new_fname)

			



			
			
#plt.show() 


#plt.show()
# data_LON = (data[data.LON != -1.000000e+34])
# data_LAT = (data_LON[data_LON.LAT != -1.000000e+34])
# data_TIME = (data_LAT[data_LAT.TIME != -1.000000e+34])

# print(data_TIME)
# print(data)
# print(data.size)
# print(data_TIME.size)
# print(np.max(data_TIME.SSS))
# print(np.min(data_TIME.SSS))
# print(data_TIME.SSS.dtype)

# cols = ['SSS', 'TIME', 'LAT', 'LON']
#data_TIME['SSS'] = data_TIME['SSS'].replace(np.isclose(data_TIME['SSS'].values, -1.000000e+34), 70.0)
# data[cols] = data[cols].mask(np.isclose(data[cols].values, -1.000000e+34))
#data_TIME['SSS'] = data_TIME['SSS'].mask(np.isclose(data_TIME['SSS'].values, -1.000000e+34))
# data_TIME = data.replace(np.nan , 70.0)
#data_TIME = data.dropna()
# print(np.min(data_TIME.SSS))
# print(data_TIME)

# fig, ax1 = plt.subplots()
# fig.set_size_inches(13, 10)

#labels
# ax1.set_xlabel('LON')
# ax1.set_ylabel('LAT')
# ax1.set_title('ColorMap for Ocean Data')

#c sequence
# c = data_TIME['SSS']

# plt.scatter( data_TIME['LON'], data_TIME['LAT'] , c=c, cmap ='RdYlBu')
# cbar = plt.colorbar()
# cbar.set_label('SSS')
