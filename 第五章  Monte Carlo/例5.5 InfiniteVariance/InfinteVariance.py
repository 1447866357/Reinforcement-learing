from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

ACTION_BACK =0
ACTION_END =1

# behavior policy
def behaviorPolicy():
    return np.random.binomial(1,0.5) # 二项式
def play():
    # track the action for importance ratio
    trajectory = []
    while True:
        action = behaviorPolicy()
        trajectory.append(action)
        if action ==ACTION_END:
            return 0,trajectory
        if np.random.binomial(1,0.9) ==0:
            return 1,trajectory

# figure 5.5
def monteCarloSample():
    runs =100
    episodes =100000
    axisX=np.arange(1,episodes+1)
    for run in range(0,runs):
        sumOfRewards = [0]
        for episode in range(0,episodes):
            reward,trajectory = play()
            if trajectory[-1] ==ACTION_END:
                importanceRatio=0
            else:
                importanceRatio = 1.0/pow(0.5,len(trajectory))
            sumOfRewards.append(sumOfRewards[-1]+importanceRatio*reward)
        del sumOfRewards[0]
        estimations = np.asarray(sumOfRewards)/np.arange(1,episodes+1)
        plt.plot(axisX,estimations)
    plt.xlabel('Episodes(10^x)')
    plt.ylabel('Ordinary Importance Sampling')
    plt.savefig('figure4.jpg', bbox_inches='tight')
    plt.show()

    return

monteCarloSample()

