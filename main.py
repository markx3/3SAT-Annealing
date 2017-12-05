from sa import Annealer
from tsat import ThreeSAT
from rs import RandomSearch
import matplotlib.pyplot as plt

if __name__ == '__main__':
    fname = 'uf20-01.cnf'
    sat = ThreeSAT(fname)
    print(fname)
    print(str(sat.num_clauses) + ' clauses')
    sa = Annealer(sat, temp=100, tempmin=0.01, alpha=0.05, maxpert=100)
    rs = RandomSearch(sat)
    print("Running annealer...")
    print(sa.run()[0])
    plt.ylabel("Custo")
    plt.xlabel("Temperatura")
    plt.plot(sa.temp_list, sa.cost_list)
    plt.xlim(plt.xlim()[::-1])             # Reverses x axis

    plt.show()
    print("\nRunning random search...")
    print(rs.run())
