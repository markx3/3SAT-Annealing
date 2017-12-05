import numpy
import re
import time
from random import randint

class ThreeSAT:
    def __init__(self, fname):
        self.num_vars = 0
        self.num_clauses = 0
        self.fname = fname
        self.clauses = self.proposition_read()
        self.init_solution = self.initial_solution()

    ''' Reads proposition from file '''
    def proposition_read(self):
        f = open(self.fname, 'r').readlines()
        header   = f[7:8]
        clauses  = f[8:-3]

        splt_hdr = header[0].split()
        num_vars = int(splt_hdr[2])
        num_clauses = int(splt_hdr[3])

        print(clauses[0].split()[:-1]) # Splits variables and removes separator
        clauses_res = []

        ''' Maps each clause to int list; appends list to list of clauses. '''
        for i in range(0, num_clauses):
            mapped = list(map(int, clauses[i].split()[:-1]))
            clauses_res.append(mapped)

        assert(len(clauses_res) == num_clauses) # Checks for trouble ;)

        self.num_vars = num_vars
        self.num_clauses = num_clauses
        return clauses_res

    ''' Generates a random initial solution. '''
    def initial_solution(self):
        solution = {}
        for i in range(1, self.num_vars + 1):
            val = randint(0, 1) == 0
            solution.update({i: val})
        return solution

    ''' Evaluates a given solution; returns a percentage of True clauses '''
    def eval(self, solution):
        passes = 0
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
                passes += 1
                continue
        return passes/self.num_clauses

    ''' Perturbates a given solution. ''' # Is it right?
    def perturbation(self, solution):
        alter_num = randint(1, num_vars//10)
        for _ in range(0, alter_num):
            altered = randint(1, num_vars+1)
            val = not solution.get(altered)
            solution.update({altered: val})
        return solution


class SimulatedAnnealing:
    def __init__(self, sat):
        self.sat = sat
        self.clauses = self.sat.clauses
        self.solution = sat.init_solution


class RandomSearch:
    def __init__(self, sat):
        self.sat = sat
        self.clauses = self.sat.clauses

    def run(self):
        counter = 0
        sol_out = self.sat.init_solution
        sol_out_fo = self.sat.eval(sol_out)
        while sol_out_fo != 1: # Precisa mudar p/ num. chamada de função (?)
            sol = self.sat.initial_solution()
            sol_fo = self.sat.eval(sol)
            counter += 2
            if sol_fo > sol_out_fo:
                sol_out = sol
                sol_out_fo = sol_fo
        print(self.sat.eval(sol_out))
        return(sol_out)


if __name__ == '__main__':
    fname = 'uf100-01.cnf'
    sat = ThreeSAT(fname)
    sa = SimulatedAnnealing(sat)
    rs = RandomSearch(sat)
    print(rs.run())
    # sa.solution = sa.sat.initial_solution()
    # print(sa.clauses)
    # print(sa.solution)
    # print(sa.sat.eval(sa.solution))
    # print(sa.sat.num_vars)
