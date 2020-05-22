#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 15:53:34 2020

@author: sonia
"""

# Here you can import variables of the Grid worlds
from mediumGrid import *
# from mediumGrid import *

from gridWorld import *
from nextState import nextState
import numpy as np


# this defines the stage cost function for any layout (small or mediumGrid)
# 
def getCost(xprime,O):
 # determine whether smallGrid or mediumGrid is loaded (give priority to mediumGrid)
    ismediumGrid = True
    issmallGrid = True
    try: CLOSEEXIT #small grid or medium grid
    except NameError: ismediumGrid = False
    try: WINSTATE
    except NameError: issmallGrid = False
    if ismediumGrid:
        flag = False
        for i in range(len(LOSESTATES)): # iterate through LOSESTATES
            if xprime == LOSESTATES[i]:
                flag = True
        if xprime == CLOSEEXIT or xprime == DISTANTEXIT: # mediumGrid win states
            cost = -1
        elif flag == True: # mediumGrid lose states
            cost = 1
        else:
            cost = 0
    elif issmallGrid:
        if xprime == WINSTATE: # smallGrid win state
            cost = -1
        elif xprime == LOSESTATE: # smallGrid lose state
            cost = 1
        else:
            cost = 0
    else:
       cost = 0
       print('getCost warning: neither smallGrid nor mediumGrid environments detected.')
    return cost


# this is the random realization version of the previous cost
def getRandomCost(x,u,O):
 # determine whether smallGrid or mediumGrid is loaded (give priority to mediumGrid)
    nta = 0.2
    xprime = nextState(x,u,eta,O)
    ismediumGrid = True
    issmallGrid = True
    try: CLOSEEXIT
    except NameError: ismediumGrid = False
    try: WINSTATE
    except NameError: issmallGrid = False
    if ismediumGrid:
        flag = False
        for i in range(len(LOSESTATES)): # iterate through LOSESTATES
            if xprime == LOSESTATES[i]:
                flag = True
        if xprime == CLOSEEXIT or xprime == DISTANTEXIT: # mediumGrid win states
            cost = -1
        elif flag == True: # mediumGrid lose states
            cost = 1
        else:
            cost = 0
    elif issmallGrid:
        if xprime == WINSTATE: # smallGrid win state
            cost = -1
        elif xprime == LOSESTATE: # smallGrid lose state
            cost = 1
        else:
            cost = 0
    else:
       cost = 0
       print('getCost warning: neither smallGrid nor mediumGrid environments detected.')
    return cost


# this defines a stage cost function for the bridge layout (medium Grid)
def getCostBridge(xprime,O):
#    xprime is the next state under an action of the MC
    cost = 0
    if xprime == CLOSEEXIT: # Small win state
        cost = -1
    elif xprime == LOSESTATES[5]: # Small lose state
        cost = 1
    elif xprime == DISTANTEXIT: # Big win state
        cost = -10
    else: 
        for i in range(5):
            if xprime == LOSESTATES[i]: # Big lose state
                cost = 10
    return cost


# this is the random cost realization of the bridge layout cost (medium Grid)
def getRandomCostBridge(x,u,O):
#    perturb the cost with a random variable 
    xprime = nextState(x,u)
    cost = 0
    if xprime == CLOSEEXIT: # Small win state
        cost = -1
    elif xprime == LOSESTATES[5]: # Small lose state
        cost = 1
    elif xprime == DISTANTEXIT: # Big win state
        cost = -10
    else: 
        for i in range(5):
            if xprime == LOSESTATES[i]: # Big lose state
                cost = 10
    return cost