from sa import Annealer
from tsat import ThreeSAT
from rs import RandomSearch

if __name__ == '__main__':
    fname = 'uf250-01.cnf'
    sat = ThreeSAT(fname)
    print(fname)
    print(str(sat.num_clauses) + ' clauses')
    sa = Annealer(sat, temp=100, tempmin=0.01, alpha=0.05, maxpert=100)
    rs = RandomSearch(sat)
    print("Running annealer...")
    print(sa.run()[0])
    print("\nRunning random search...")
    print(rs.run())
