from __future__ import print_function
import numpy as np
import sys
WORLD_SIZE = 5
A_POS = [0,1]
A_PRIME_POS = [4,1]
B_POS = [0,3]
B_PRIME_POS = [2,3]
discount = 0.9

f_result=open('GridWord_result.txt', 'w')
sys.stdout=f_result
print ('  ')


world = np.zeros((WORLD_SIZE,WORLD_SIZE))

# left ,up , right ,down

actions = ['L','U','R','D']
actionProb = []
for i  in range(0, WORLD_SIZE):
    actionProb.append([])
    for j in range(0,WORLD_SIZE):
        actionProb[i].append(dict({'L':0.25,'U':0.25,'R':0.25,'D':0.25}))

nextState = []
actionReward = []
for i in range(0,WORLD_SIZE):
    nextState.append([])
    actionReward.append([])
    for j in range(0,WORLD_SIZE):
        next = dict()
        reward = dict()
        if i == 0 :
            next['U'] = [i,j]
            reward['U'] = -1.0
        else:
            next['U'] = [i-1,j]
            reward['U'] = 0.0

        if i == WORLD_SIZE -1:
            next['D'] = [i,j]
            reward['D'] =-1.0
        else:
            next['D'] = [i+1,j]
            reward['D'] =0.0

        if j ==0:
            next['L'] = [i,j]
            reward['L'] = -1.0
        else:
            next['L'] = [i,j-1]
            reward['L'] = 0.0

        if j == WORLD_SIZE - 1:
            next['R']  = [i,j]
            reward['R'] = -1.0
        else:
            next['R'] = [i,j+1]
            reward['R'] = 0.0

        if [i,j ] ==A_POS:
             next['L'] = next['R']=next['U']=next['D'] = A_PRIME_POS
             reward['L'] =reward['R']=reward['U']=reward['D']=10.0

        if [i, j] == B_POS:
            next['L'] = next['R'] = next['D'] = next['U'] = B_PRIME_POS
            reward['L'] = reward['R'] = reward['D'] = reward['U'] = 5.0
        nextState[i].append(next)
        actionReward[i].append(reward)

# for figure 3.5
# 使用策略π，迭代状态价值方法
while True:
    # keep iteration until convergence
    newWorld = np.zeros((WORLD_SIZE,WORLD_SIZE))
    for i in range(0,WORLD_SIZE):
        for j in range(0,WORLD_SIZE):
            for action in actions:
                newPosition = nextState[i][j][action]
                # bellman equation
                newWorld[i, j] += actionProb[i][j][action] * (actionReward[i][j][action] + discount * world[newPosition[0], newPosition[1]])
    if np.sum(np.abs(world - newWorld)) < 1e-4:
        print('Random Policy')
        print(newWorld)
        break
    world = newWorld



# for figure 3.8
# 最优化状态价值方法
world = np.zeros((WORLD_SIZE,WORLD_SIZE))
while True:
     # keep iteration until convergence
    newWorld = np.zeros((WORLD_SIZE,WORLD_SIZE))
    for i in range(0,WORLD_SIZE):
        for j in range(0,WORLD_SIZE):
            values = []
            for action in actions:
                newPosition =  nextState[i][j][action]
                # value iteration
                values.append(actionReward[i][j][action]+discount*world[newPosition[0],newPosition[1]])
            newWorld[i][j] = np.max(values)

    if np.sum(np.abs(world - newWorld))<1e-4:
        print('Optimal Policy')
        print(newWorld)
        break

    world = newWorld

"""a=world
f=open('new.txt', 'a')
# 将函数a里面的内容输出到文件
f.write(a)
f.close"""

