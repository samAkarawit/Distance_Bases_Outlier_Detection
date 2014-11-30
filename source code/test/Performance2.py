__author__ = 'Akarawit'
from approximation.ApproximationAlgorithm import *
from exact.ExactAlgorithm import *
from datetime import datetime

# parameter input
file_dir = input('Data set: ')
w = int(input('Windows size: '))
r = float(input('Range: '))
k = int(input('number of K neighbors: '))
p = float(input('ρ for Approximation Algorithm: '))
s = int(input('Query rate: '))
# promp
print('\nrunning: ' + 'w: ' + str(w) + ' r: ' + str(r) + ' k: ' + str(k) + ' p: ' + str(p) + ' s: ' + str(s))
#read evaluation
true_outlier = set()
data_input = open(file_dir, 'r')
for line in data_input:
    if line.split()[2] == '1':
        true_outlier.add(int(line.split()[0]))
print('\nFrom data, true outlier : ' + str(len(true_outlier)) + '\n' + str(true_outlier))
#Exact Algorithm
print('\nStart Exact Algorithm!')
exact_start = datetime.now()
exact_result, exact_n_isb = ExactAlgorithm.run(file_dir=file_dir, w=w, r=r, k=k, s=s)
exact_stop = datetime.now()
print('Done Exact Algorithm!')
print('Exact Algorithm Running time: ' + str(exact_stop - exact_start))
print('Exact Algorithm isb items: ' + str(exact_n_isb))
print('Exact Algorithm error: {:.2%}'.format(
    len((true_outlier - exact_result) | (exact_result - true_outlier)) / len(true_outlier)))
print('Exact Algorithm precision: {:.2%}'.format(len(true_outlier & exact_result) / len(exact_result)))
print('Exact Algorithm recall: {:.2%}'.format(len(exact_result & true_outlier) / len(true_outlier)))
print('Exact Algorithm detected outlier: ' + str(len(exact_result)))
print(str(exact_result))
#Approximation Algorithm
print('\nStart Approximation Algorithm!')
appro_strat = datetime.now()
app_n_isb = 0
appro_result, appro_n_isb = ApproximationAlgorithm.run(file_dir=file_dir, w=w, r=r, k=k, p=p, s=s)
appro_stop = datetime.now()
print('Done Approximation Algorithm!')
print('Approximation Algorithm Running time: ' + str(appro_stop - appro_strat))
print('Approximation Algorithm isb items: ' + str(appro_n_isb))
print('Approximation Algorithm error: {:.2%}'.format(
    len((true_outlier - appro_result) | (appro_result - true_outlier)) / len(true_outlier)))
if len(appro_result) == 0:
    print('Approximation Algorithm precision ERROR: result from Approximation Algorithm is null')
else:
    print('Approximation Algorithm precision: {:.2%}'.format(len(true_outlier & appro_result) / len(appro_result)))
print('Approximation Algorithm recall: {:.2%}'.format(len(appro_result & true_outlier) / len(true_outlier)))
print('Approximation Algorithm detected outlier: ' + str(len(appro_result)))
print(str(appro_result))

print("EXIT")