__author__ = 'Akarawit'
from exact.Node import*

class StreamManager:

    def stream(self,isb,n_id,n_obj,w,r):
        #create node
        node = Node()
        node.obj = n_obj
        node.id = n_id
        node.nn_before = []
        node.count_after = 0
        # remove expired node
        n_ex = None
        if(len(isb)>=w):
            n_ex = isb[0]
            isb.remove(n_ex)
        # range query search
        for ni in isb:
            #updata nn_before
            if( len(ni.nn_before) > 0 and ni.nn_before[0] == n_ex):
                ni.nn_before.remove(ni.nn_before[0])
            #update count after of ni and nn_before of node
            if( abs(ni.obj-node.obj)<=r ):
                ni.count_after += 1
                node.nn_before.append(ni)
        isb.append(node)