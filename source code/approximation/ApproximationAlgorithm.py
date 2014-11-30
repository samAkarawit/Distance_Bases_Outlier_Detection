__author__ = 'Akarawit'
from approximation.StreamManager import *
from approximation.QueryManager import *

class ApproximationAlgorithm:
    def run(file_dir,w,r,k,p,s):
        isb = []
        streamMan = StreamManager()
        queryMan = QueryManager()
        file = open(file_dir, 'r')
        outlier = set()
        for line in file:
            rec = line.split()
            streamMan.stream(isb, int(rec[0]), float(rec[1]), w=w, r=r, k=k, p=p)
            if ( int(rec[0]) > w and int(rec[0])%s == 0 ):
                curr_outlier = queryMan.query(isb,w=w,k=k)
                if(len(curr_outlier)!=0):
                    for ni in curr_outlier:
                        outlier.add(ni.id)
        return outlier,len(isb)