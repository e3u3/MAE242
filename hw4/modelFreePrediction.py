#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 13:36:52 2020

@author: sonia
"""

# Here you can import variables of the Grid worlds
#from smallGrid import *
from mediumGrid import *

from gridWorld import *
from nextState import nextState
import numpy as np
# previous homework 
from costs import *


def generate(start, pi, T, O):
    eta = 0.25 #uncertainy in robot movement
    path = []
    path.append(start)
    for i in range(T):
        if path[i] != CLOSEEXIT and path[i] != DISTANTEXIT and path[i] not in LOSESTATES:
            nextx = nextState(path[i], pi, eta, O)
        else:
            nextx = path[i]
        path.append(nextx)
    return path

#   In this part you will first implement two methods to do 
# model-free predictions:
def Compute_L(index, path, gamma):
    L = 0
    upper_index = 0
    for i in range(index + 1, len(path)):
        L += gamma ** upper_index * getCost(path[i], O)
        upper_index += 1
        if upper_index != 0:
            if path[i] == CLOSEEXIT or path[i] == DISTANTEXIT or path[i] in LOSESTATES:
                return L
    return L

def Compute_l(index, path):
    L = 0
    upper_index = 0
    L = getCost(path[index + 1], O)
    return L

def firstvisitMC(pi,randomcost,gamma,O,T,M):
    gridvals = makeMaze(n, m, O) #[1,1,1] -> free space
    fig,ax = plt.subplots()  # make a figure + axes
    ax.imshow(gridvals)  # Plot it
    ax.invert_yaxis()  # Needed so that bottom left is (0,0)
    N = np.zeros([n, m]) - 10
    J = np.zeros([n, m]) - 10
    for i in range(m): #initialization
        for j in range(n):
            x = [j,i]
            if not (isObstacle(x, O)):
                N[j, i] = 0
                J[j, i] = 0
    for i in range(M):
        path = generate(START, pi, T, O)
        print(path)
        for i in range(m):  # initialization
            for j in range(n):
                x = [j, i]
                if not (isObstacle(x, O)):
                    if x in path and x != CLOSEEXIT and x!= DISTANTEXIT:
                        N[j, i] += 1
                        alpha = 1 / N[j, i]
                        L = Compute_L(path.index(x), path, gamma)
                        print(x, L, alpha)
                        J[j, i] = J[j, i] + alpha * (L - J[j, i])
    # new_values = makeValues(J, START, [CLOSEEXIT, DISTANTEXIT], n, m, O, LOSESTATES)
    # fig1,ax1 = plt.subplots()  # make a figure + axes
    # ax1.imshow(new_values)  # Plot it
    # ax1.invert_yaxis()  # Needed so that bottom left is (0,0)
    np.set_printoptions(precision=3)
    print(J.T[::-1])
    print(J[3, 3])
    print(J[3, 2])
    print(J[2, 2])
    print(J[1, 2])

        # given a policy pi generate T long episodes to calculate approximation 
        # policy evaluation cost to go via MC simulation
        
        # you need to use the random cost version of the function getRandomCost
        # choose a sequence alpha_k = 1/(k+1)
        
        
def TDzero(pi,randomcost,gamma,O,T,M):
    gridvals = makeMaze(n, m, O) #[1,1,1] -> free space
    fig,ax = plt.subplots()  # make a figure + axes
    ax.imshow(gridvals)  # Plot it
    ax.invert_yaxis()  # Needed so that bottom left is (0,0)
    N = np.zeros([n, m]) - 10
    J = np.zeros([n, m]) - 10
    for i in range(m): #initialization
        for j in range(n):
            x = [j,i]
            if not (isObstacle(x, O)):
                N[j, i] = 0
                J[j, i] = 0
    J_tmp = J
    for i in range(M):
        path = generate(START, pi, T, O)
        for i in range(m):  # initialization
            for j in range(n):
                x = [j, i]
                if not (isObstacle(x, O)):
                    if x in path and x != CLOSEEXIT and x!= DISTANTEXIT and path.index(x) < T -1:
                        if x == [2, 2] or x == [3,2]:
                            print(path)
                        next = path[path.index(x)+1]
                        N[j, i] += 1
                        alpha = 1 / N[j, i]
                        l = Compute_l(path.index(x), path)
                        J_tmp[j, i] = J[j, i] + alpha * (l + gamma * J[next[0], next[1]] - J[j, i])
        J = J_tmp
    np.set_printoptions(precision=3)
    print(J.T[::-1])
    # print(J[3, 3])
    # print(J[3, 2])
    # print(J[2, 2])
    # print(J[1, 2])
        # given a policy pi generate T long episodes to calculate approximation 
        # policy evaluation cost to go via TD(0) simulation
        
        # you need to use the random cost version of the function getRandomCost
        # choose a sequence alpha_k = 1/(k+1)
        
        
        