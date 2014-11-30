/data sets		data sets using  the experiments.

/references		references paper in this study.

/test result 	test results from the experiments.

/source code	source code of algorirthms and experiments, programed in python.

	/approximation	souce code of approximation algorithm
	
		/ApproximationAlgorithm.py	ApproximationAlgorithm class for run the Approximation algorithm with single-dimension data set, 'run' function require: data set directory 'file_dir' (string), windows size 'w' (int), range 'r' (float), k-neigbour 'k' (int), p (float), and sample rate 's' (int).
		
		/ApproximationAlgorithmMulti.py	ApproximationAlgorithmMulti class for run the Approximation algorithm with multi-dimension data set,'run' function require: data set directory 'file_dir' (string), windows size 'w' (int), range 'r' (float[]), k-neigbour 'k' (int), p (float), and sample rate 's' (int).
		
	/exact	souce code of exact algorithm
	
		/ExactAlgorithm.py	ExactAlgorithm class for run the Exact algorithm with single-dimension data set, 'run' function require: data set directory 'file_dir' (string), windows size 'w' (int), range 'r' (float), k-neigbour 'k' (int), and sample rate 's' (int).
		
		/ExactAlgorithmMulti.py	ExactAlgorithmMulti class for run the Exact algorithm with multi-dimension data set,'run' function require: data set directory 'file_dir' (string), windows size 'w' (int), range 'r' (float[]), k-neigbour 'k' (int), and sample rate 's' (int).
	
	/test
	
		/Performance.py	Performance class for evaluation of the single dimension unlabelled data set of bouth algorithms.
		
		/Performance2.py Performance2 class for evaluation of the single dimension labelled data set of bouth algorithms.
		
		/Performance3.py Performance class for evaluation of the multi dimension unlabelled data set of bouth algorithms.
		
		
