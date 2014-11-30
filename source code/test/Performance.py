__author__ = 'Akarawit'
from approximation.ApproximationAlgorithm import *
from exact.ExactAlgorithm import *
from datetime import datetime

file_dir = input('Data set: ')
w =int(input('Windows size: '))
r =float(input('Range: '))
k =int(input('number of K neighbors: '))
p =float(input('ρ for Approximation Algorithm: '))
s =int(input('Query rate: '))

print('running: ' + 'w: ' + str(w) + ' r: ' + str(r) + ' k: ' + str(k) + ' p: ' + str(p) + ' s: ' + str(s))

print('Start Exact Algorithm!')
exact_start = datetime.now()
exact_result, exact_n_isb = ExactAlgorithm.run(file_dir=file_dir, w=w, r=r, k=k, s=s)
exact_stop = datetime.now()
print('Done Exact Algorithm!')

print('Start Approximation Algorithm!')
appro_strat = datetime.now()
app_n_isb = 0
appro_result, appro_n_isb = ApproximationAlgorithm.run(file_dir=file_dir, w=w, r=r, k=k, p=p, s=s)
appro_stop = datetime.now()
print('Done Approximation Algorithm!')
# Running Time
print('\nRunning time of Exact Algorithm: ' + str(exact_stop - exact_start))
print('Running time of Approximation Algorithm: ' + str(appro_stop - appro_strat))
#node inside IS (Memory Usage)
print("\nNumber of node in Exact Algorithm's ISB  " + str(exact_n_isb))
print("Number of node in Approximation Algorithm's ISB  " + str(appro_n_isb))
# result
print('\nNumber of outlier from Exact Algorithm: ' + str(len(exact_result)))
print('Number of outlier from Approximation Algorithm: ' + str(len(appro_result)))
#error
difference = (exact_result | appro_result) - (exact_result & appro_result)
print('\nResult difference: ' + str(len(difference)))
if(len(exact_result)==0):
    print('exact_result = 0')
    exit()
print('error: {:.2%}'.format(len(difference) / len(exact_result)))
#precision
print('\nPercision of Approximation Algorithm: {:.2%}'.format(len(appro_result & exact_result) / len(appro_result)))
#recall
print('Recall of Approximation Algorithm: {:.2%}'.format(len(exact_result & appro_result) / len(exact_result)))

print('\nexact_result: ' + str(sorted(exact_result)))
print('appro_result: '+ str(sorted(appro_result)))

print("EXIT")