/data sets
	/normaldis.txt	Synthetic data with Gaussian distributions 
	
		Synthetic data with Gaussian distributions
			Random mixture of three Gaussian distributions 35000 records contain randomly mixed 250 records labelled as outlier, 
				Mean = 50, SD = 2.5;  32500 records
				Mean = 30, SD = 2.5;  125 records, (labelled as outlier)
				Mean = 70, SD = 2.5;  125 records, (labelled as outlier)
				
			Data format: id(int)	value(float)	label(int, 0 as inlier and 1 as outlier)
			example:	
				1	51.76	0
				2	50.33	0
				3	47.95	0
				
				
	/home_sensor.txt  real data set from Activity Recognition in the Home Setting, http://courses.media.mit.edu/2004fall/mas622j/04.projects/home/
		
		Data set contain 18914 records with 2 dimension data
	
			Data format: id(int) humidity(float) temparature(float)
			example:
				1	45.93	27.97
				2	45.9	27.95
				3	45.9	27.96