from random import randint
from copy import deepcopy


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
            val = randint(-1, 1) == 0
            solution[i] = val
        return solution

    ''' Evaluates a given solution; returns num_clauses - passes. This way, as
        the number of true clauses increases, the evaluation tends to zero '''
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
        return self.num_clauses - passes

    ''' Changes a single value of a solution to its negation in order to disturb
        the solution '''
    def perturbation(self, solution):
        new_sol = deepcopy(solution)
        altered = randint(1, self.num_vars)
        val = new_sol.get(altered)
        new_sol[altered] = not val
        return new_sol
