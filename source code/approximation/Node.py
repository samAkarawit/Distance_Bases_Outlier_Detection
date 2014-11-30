__author__ = 'Akarawit'

class Node:
    obj = None
    id = None
    count_after = None
    fract_before = None

    def __str__(self):
        # return '('+ str(self.id) + ', '+ str(self.obj) + ', ' + str(self.count_after) + ', ' + str(len(self.fract_before)) + ')\n'
        return '\n'+ str(self.id) + '\t '+ str(self.obj) + '\t'
    def __repr__(self):
        # return '('+ str(self.id) + ', '+ str(self.obj) + ', ' + str(self.count_after) + ', ' + str(len(self.fract_before)) + '\n'
        return '\n'+ str(self.id) + '\t '+ str(self.obj) + '\t'