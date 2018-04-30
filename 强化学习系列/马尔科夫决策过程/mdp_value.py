import numpy
import random as ran
ran.seed(0) #seed() 方法改变随机数生成器的种子
from  grid_mdp import *

def random_pi():
    actions = ['n','w','e','s']
    r  = int(ran.random()*4)
    return actions[r]

def compute_random_pi_state_value():
    value = [0.0 for r in range(9)]
    num = 1000000

    for k in range(1,num):
        for i in range(1,6):
            mdp = Mdp()
            s = i
            is_terminal = False
            gamma = 1.0
            v = 0.0
            while False == is_terminal:
                a = random_pi()
                is_terminal,s,r = mdp.transform(s,a)
                v  +=gamma*r
                gamma *=0.5

            value[i] = (value[i]*(k-1)+v)/k

        if k % 10000 == 0:
            print(value)

    print(value)
compute_random_pi_state_value()