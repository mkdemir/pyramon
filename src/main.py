import sys
sys.path.append('../')
from apps.pyra import Pyra
from apps.pyra_connection import PyraConnector
from apps.pyra_performance import PyraPerformance


def pyra_performance():
    pyraperformance = PyraPerformance()
    pyraperformance.dbstats()
    pyraperformance.dbserverStatus()
    pyraperformance.dbcurrentOp()

def pyra():
    pyra = Pyra()
    pyra.get_query()

def main():
    pyra_performance()

if __name__ == '__main__':
    main()
