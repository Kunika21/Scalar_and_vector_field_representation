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
import matplotlib.colors as colors

root_folder = sys.argv[1]
print(root_folder)
#vector_quantity = sys.argv[2]

mapping_style = sys.argv[2]
order = sys.argv[5]
if os.path.exists(root_folder + '/Results/' + mapping_style +'/'+ order + "/"):
	pass
else:
	os.makedirs(root_folder + '/Results/' + mapping_style +'/'+ order +'/')
m_folder = root_folder + "/meridional-current/"
z_folder = root_folder + "/zonal-current/"
results_dir = root_folder + '/Results/' + mapping_style +'/'+ order +'/'

max_list = []
min_list = []

for fname in sorted(os.listdir(m_folder)):
	if fname.endswith(".txt"):
		m_data = pd.read_csv(os.path.join(m_folder, fname), header=0, skiprows= 10)
		z_data = pd.read_csv(os.path.join(z_folder, fname), header=0, skiprows= 10)
		data = pd.concat([m_data, z_data["U"]], axis = 1)
		# print(data)



		cols = ['DEP', 'TIME', 'LAT', 'LON', 'V' , 'U']
		data[cols] = data[cols].mask(np.isclose(data[cols].values, -1.000000e+34))
		data_processed = data.dropna()
		data_new = []
		for rows in range(len(data_processed)):
			if rows % int(sys.argv[5]) == 0:
				data_new.append(data_processed.iloc[rows])
		df = pd.DataFrame (data_new)
		n = -2
		color = np.sqrt(((df['V']-n)/2)*2 + ((df['U']-n)/2)*2)

		Vector_min = np.min(color)
		Vector_max = np.max(color)
		max_list.append(Vector_max)
		min_list.append(Vector_min)

min_in_Vector = np.min(min_list)
max_in_Vector = np.max(max_list)

# print(min_in_Scalar, max_in_Scalar)
count = 0
for fname in sorted(os.listdir(m_folder)):
	count = count + 1
	if count > int(sys.argv[4]):
		break
	elif fname.endswith(".txt") and count >= int(sys.argv[3]):
		m_data = pd.read_csv(os.path.join(m_folder, fname), header=0, skiprows= 10)
		z_data = pd.read_csv(os.path.join(z_folder, fname), header=0, skiprows= 10)
		data = pd.concat([m_data, z_data["U"]], axis = 1)
		# print(data)



		cols = ['DEP', 'TIME', 'LAT', 'LON', 'V' , 'U']
		data[cols] = data[cols].mask(np.isclose(data[cols].values, -1.000000e+34))
		data_processed = data.dropna()
		# print(data_processed.to_csv)
		counter = 0
		data_new = []
		for rows in range(len((data_processed))):
			if rows % int(sys.argv[5]) == 0:
				data_new.append(data_processed.iloc[rows])
		df = pd.DataFrame (data_new)	
		# print(df.to_csv)
		# X, Y= []
		

		# for x,y in zip(data_processed['LON'], data_processed['LAT']): 
		# 	x_mesh, y_mesh = np.meshgrid(x,y)
		# 	print(x_mesh, y_mesh)
		# 	count = count + 1
		# 	# print(X)
		# print(count)

		fig, ax = plt.subplots()
		ax.set_title('QuiverPlot for %s' %(fname))
		fig.set_size_inches(17, 10)
		ax.set_xlabel('LON')
		ax.set_ylabel('LAT')
		plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%d °E'))
		plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d °N'))
		# ax1.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
		n = -2
		color = np.sqrt(((df['V']-n)/2)*2 + ((df['U']-n)/2)*2)


		if mapping_style == "quiver":
			fig = ax.quiver(df['LON'], df['LAT'], df['U'], df['V'] ,color, cmap= plt.cm.viridis, norm=colors.LogNorm(vmin = min_in_Vector, vmax = max_in_Vector),  scale = 30, width = 0.001, headaxislength=5.5)
			# ax.set_title('Quiver plot with one arrow')
			# m = plt.cm.ScalarMappable(cmap= plt.cm.viridis)
			# m.set_array(color)
			# m.set_clim(min_in_Scalar, max_in_Scalar)
			cbar = plt.colorbar(fig)
			# cbar = plt.colorbar()
			# cbar.set_label(scalar_quantity)
		elif mapping_style == "streamline":
			x_mesh, y_mesh = np.meshgrid(data_processed['LON'], data_processed['LAT'], copy = False, sparse = True)
			u, v = np.meshgrid(data_processed['U'], data_processed['V'], copy = False, sparse = True)
			ax.streamplot(data_processed['LON'], data_processed['LAT'] ,u,v, color, linewidth=2, cmap='autumn', scale=0.0005)

		new_fname = fname.replace(".txt", ".png")
		print(new_fname)
		plt.savefig(results_dir + new_fname)


# 		V_min = np.min(data_processed[scalar_quantity])
# 		V_max = np.max(data_processed[scalar_quantity])
# 		max_list.append(V_max)
# 		min_list.append(V_min)

# min_in_Vector = np.min(min_list)
# max_in_Vector = np.max(max_list)

# for fname in sorted(os.listdir(data_folder)):
# 	if fname.endswith(".txt"):