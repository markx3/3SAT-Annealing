class RandomSearch:
    def __init__(self, sat, maxcalls=500000):
        self.sat = sat
        self.clauses = self.sat.clauses
        self.maxcalls = maxcalls

    def run(self):
        counter = 0
        sol_out = self.sat.init_solution
        sol_out_fo = self.sat.eval(sol_out)
        while counter <= self.maxcalls:
            sol = self.sat.initial_solution()
            sol_fo = self.sat.eval(sol)
            counter += 1
            if sol_fo > sol_out_fo:
                sol_out = sol
                sol_out_fo = sol_fo
        print(self.sat.eval(sol_out))
        return(sol_out)
