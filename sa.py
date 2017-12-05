import numpy
import re
import time
from random import randint
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

    ''' Evaluates given solution '''
    def eval(self, solution):
        pas = 0
        for clause in self.clauses:
            a = clause[0]
            b = clause[1]
            c = clause[2]

            a_sol = solution.get(a)
            b_sol = solution.get(b)
            c_sol = solution.get(c)

            if a < 0: a_sol = not a_sol
            if b < 0: b_sol = not b_sol
            if c < 0: c_sol = not c_sol

            if a_sol or b_sol or c_sol:
                continue
            else:
                return False
        return True

class SimulatedAnnealing:
    def __init__(self, fname):
        self.sat = ThreeSAT(fname)
        self.clauses = self.sat.clauses
        self.solution = {}

    def initial_solution(self):
        solution = {}
        for i in range(1, self.sat.num_vars + 1):
            val = randint(0, 1) == 0
            solution.update({i: val})
        return solution

if __name__ == '__main__':
    sa = SimulatedAnnealing('uf20-01.cnf')
    sa.solution = sa.initial_solution()
    print(sa.clauses)
    print(sa.solution)
    print(sa.sat.eval(sa.solution))
    print(sa.sat.num_vars)
    print(sa.sat.result)
