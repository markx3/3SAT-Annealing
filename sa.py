import numpy
import re
from functools import reduce

class ThreeSAT:
    def __init__(self, fname):
        self.num_vars = 0
        self.result = 0
        self.fname = fname
        self.clauses = self.proposition_read()

    ''' Reads proposition from file '''
    def proposition_read(self):
        f = open(self.fname, 'r').readlines()
        header   = f[7:8]
        clauses  = f[8:-3]
        result   = f[-2:-1]

        splt_hdr = header[0].split()
        num_vars = int(splt_hdr[2])
        num_clauses = int(splt_hdr[3])

        print(clauses[0].split()[:-1]) # Splits variables and removes separator
        clauses_res = []

        ''' Maps each clause to int list; appends list to list of clauses. '''
        for i in range(0, num_clauses):
            mapped = list(map(int, clauses[i].split()[:-1]))
            clauses_res.append(mapped)

        assert(len(clauses_res) == num_clauses)

        self.num_vars = num_vars
        self.num_clauses = num_clauses
        print((result[0].split()))
        return clauses_res

class SimulatedAnnealing:
    def __init__(self, fname):
        self.sat = ThreeSAT(fname)
        self.clauses = self.sat.clauses


if __name__ == '__main__':
    sa = SimulatedAnnealing('uf20-01.cnf')
    print(sa.clauses)
    print(sa.sat.num_vars)
    print(sa.sat.result)
    v = reduce(lambda a, b: max(a, *b), sa.clauses, 0)
    s = v * 'x' + ';' + len(sa.clauses) * 'x,'
    e = '^' + v * '(x?)' + '.*;' + ''.join(
    '(?:' + '|'.join(
        '\\' + (str(-x) + 'x' if x < 0 else str(x))
        for x in clause) + '),'
    for clause in sa.clauses)

    print (re.match(e, s).groups())
