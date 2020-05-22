'''
Author: Yunhai Han
Data: May 12
Function: main
'''
from modelFreePrediction import *
from costs import *
from mediumGrid import *

def main():
    # T = 5, 10, 100
    # M = 10, 50
    # gamma = 0.5, 0.8
    # eta = 0.25
    T = 100
    M = 50
    gamma = 0.8
    pi = (0, 1) #always go "up"
    TDzero(pi, getCost, gamma, O, T, M)
    plt.show()

if __name__ == '__main__':
    main()