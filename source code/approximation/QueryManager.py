__author__ = 'Akarawit'


class QueryManager:
    def query(self, isb, w, k):

        # if(int(isb[4999].id)>7450):
        # print(str(isb[4999].id)+" in_query_man")
        outlier = []
        #search for nn_before + counr_after < k
        for ni in isb:
            prec_neigh = ni.fract_before * (w - isb[len(isb) - 1].id + ni.id - 1)
            if (prec_neigh + ni.count_after <= k):
                outlier.append(ni)

        # if(int(isb[4999].id)>7450):
        #     print(str(isb[4999].id)+" out_query_man")
        return outlier
