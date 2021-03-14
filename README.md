# SCALAR FIELDS:
##### To generate Scalar Fields following command is needed to be given on your terminal from the project dir 
- `python scalar_field.py <Root dir containing your data> <Scalar quantity to be plotted against (opts. SST, SSHA, SSS)> <mapping_style (opts. color, contour, elevation)> <txt file from where you want to plot your figures (opts. any integer from 1 to 147)> <txt file till where you wnt your plots to be printed (opts. any integer between 1 to 147)>`
- an examplar command to run the code producing elevation maps for SSHA, plotting from 46 to 84 files is written below
 	`python scalar_field.py /home/kunika/Desktop/Data_Visualisation_assignment_01/CD732-Datathon-1 SSHA elevation 46 84`


# VECTOR FIELDS
##### To generate Vector Fields following command is needed to be given on your terminal from the project dir 
- `python vector_field.py <Root dir containing your data> <mapping_style (opts. quiver)> <txt file from where you want to plot your figures (opts. any integer from 1 to 147)> <txt file till where you wnt your plots to be printed (opts. any integer between 1 to 147)> <level of spartsity in data(opts. int between 2 to 7)`
- an examplar command to run the code producing quiver plots for meridonial current and zonal current dataset, plotting from 46 to 84 files is written below
 `python vector_field.py /home/kunika/Desktop/Data_Visualisation_assignment_01/CD732-Datathon-1 quiver 1 147`

## GENERATING VIDEOS
##### To generate videos for your results following command is needed to be given on your terminal from the project dir 
- python video.py <Root dir containing your results> <output_video.mp4>
- an examplar command to run the code producing video for some elevation maps for scalar quantity, SST is written below
` python video.py /home/kunika/Desktop/Data_Visualisation_assignment_01/CD732-Datathon-1/Results/elevation/SST/ elevtionMap_SST.mp4`


## WHERE TO CHECK FOR OUTPUTS
- To check the outputs navigate through the directory from where you are accessing the data, under that directory a new folder named *results* is generated. All the output plots are structurly saved there. 
- To check out the videos navigate into the *results* directory. A dir named *resultant_video* is present, under that path you will find all your generated videos.

## DATASET
##### dataset can be obtained from the link mentioned below,
` https://las.incois.gov.in/las/UI.vm `

## RESULTS
##### results can be viewed on,
`https://drive.google.com/file/d/1600RiA6FE2cBw7qdE3bUx0UqnxP0RK2d/view?usp=sharing`


## Querries 
Your querries related to this code will be addressed on *Kvalecha.work@gmail.com*
