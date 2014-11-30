__author__ = 'Akarawit'
from exact.StreamManager import*
from exact.QueryManager  import*

class ExactAlgorithm:
    def run(file_dir,w,r,k,s):
        isb=[]
        streamMan = StreamManager()
        queryMan = QueryManager()
        file = open(file_dir,'r')
        outlier = set()
        for line in file:
            rec = line.split()
            streamMan.stream(isb,int(rec[0]),float(rec[1]),w=w,r=r)
            if( int(rec[0]) > w and int(rec[0])%s == 0 ):
                curr_outlier = queryMan.query(isb,k=k)
                if(len(curr_outlier)!=0):
                    for ni in curr_outlier:
                        outlier.add(ni.id)
        return outlier,len(isb)