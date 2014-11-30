__author__ = 'Akarawit'
from approximation.StreamManager import *
from approximation.QueryManager import *

class ApproximationAlgorithmMulti:
    def run(file_dir,w,r,k,p,s):
        streamMan = StreamManager()
        queryMan = QueryManager()
        file = open(file_dir, 'r')
        outlier = set()
        id = None
        isbs = None
        for line in file:
            rec = line.split()
            obj = []
            dim = -1
            for value in rec:
                if dim == -1:
                    id = int(value)
                else:
                    obj.append(float(value))
                dim+=1
            if isbs == None:
                isbs = [ [] for x in range(dim)]
            for i in range(dim):
                streamMan.stream(isbs[i],id,n_obj=obj[i],w=w,r=r[i],k=k,p=p)
            if ( int(rec[0]) > w and int(rec[0])%s == 0 ):
                for i in range(dim):
                    curr_outlier = queryMan.query(isbs[i],w=w,k=k)
                if(len(curr_outlier)!=0):
                    for ni in curr_outlier:
                        outlier.add(ni.id)
        return outlier