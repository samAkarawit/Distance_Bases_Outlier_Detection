__author__ = 'Akarawit'
from exact.StreamManager import*
from exact.QueryManager  import*

class ExactAlgorithmMulti:
    def run(file_dir,w,r,k,s):

        streamMan = StreamManager()
        queryMan = QueryManager()
        file = open(file_dir,'r')
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
                streamMan.stream(isbs[i],id,n_obj=obj[i],w=w,r=r[i])
            if( id > w and id%s == 0 ):
                for i in range(dim):
                    curr_outlier = queryMan.query(isbs[i],k=k)
                if(len(curr_outlier)!=0):
                    for ni in curr_outlier:
                        outlier.add(ni.id)
        return outlier,len(isbs)



