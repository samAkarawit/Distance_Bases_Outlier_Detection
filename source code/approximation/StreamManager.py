__author__ = 'Akarawit'
from approximation.Node import *
from random import shuffle
import math


class StreamManager:
    def stream(self, isb, n_id, n_obj, w, r, k, p):

        # create node
        node = Node()
        node.obj = n_obj
        node.id = n_id
        node.fract_before = 0
        node.count_after = 0
        # remove expired node
        if len(isb) > 1 and isb[len(isb) - 1].id - isb[0].id + 1 >= w:
            n_ex = isb[0]
            isb.remove(n_ex)

        safe_inlier = []
        count_before = 0
        # range query search
        for ni in isb:
            if abs(ni.obj - node.obj) <= r:
                ni.count_after += 1
                if ni.count_after >= k:
                    safe_inlier.append(ni)
                else:
                    count_before += 1
        # randomly delete safe inliner
        if len(safe_inlier) >= p * w:
            shuffle(safe_inlier)
            for i in range(0, len(safe_inlier) - math.floor(p * w + 1)):
                isb.remove(safe_inlier[i])
        # correct count before
        if len(safe_inlier) >= p * w:
            count_before += math.floor(p * w)
        else:
            count_before += len(safe_inlier)
        #asing fract before
        if len(safe_inlier) != 0:
            if len(safe_inlier) < p * w:
                node.fract_before = count_before / len(safe_inlier)
            elif math.floor(p * w) == 0:
                node.fract_before = 0
            else:
                node.fract_before = count_before / math.floor(p * w)
        else:
            node.fract_before = 0
        isb.append(node)