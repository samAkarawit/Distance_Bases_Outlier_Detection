__author__ = 'Akarawit'

class QueryManager:

    def query(self,isb,k):

        outlier = []
        #search for nn_before + counr_after < k
        for ni in isb:
            if(len(ni.nn_before)+ni.count_after <= k):
                outlier.append(ni)

        return outlier
