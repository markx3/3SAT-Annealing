from sa import Annealer
from tsat import ThreeSAT
from rs import RandomSearch
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    files = ['uf20-01.cnf', 'uf100-01.cnf', 'uf250-01.cnf']
    for fname in files:
        fname = 'uf100-01.cnf'
        sat = ThreeSAT(fname)
        print(fname)
        print(str(sat.num_clauses) + ' clauses')
        sa = Annealer(sat, temp=100, tempmin=0.01, alpha=0.05, maxpert=100)
        rs = RandomSearch(sat)
        print("Running annealer...")
        sa.run()
        # plt.ylabel("Cláusulas satisfeitas")
        # plt.xlabel("Temperatura")
        # plt.plot(sa.temp_list[:], sa.cost_list[:])
        # plt.xlim(plt.xlim()[::-1])             # Reverses x axis
        # plt.show()
        print("\nRunning random search...")
        print(rs.run())
        # plt.ylabel("Custo")
        # plt.xlabel("Iteração")
        # plt.plot(np.arange(0, 500001, 1), rs.cost_list)
        # plt.xlim(plt.xlim()[::-1])             # Reverses x axis
        # plt.show()
