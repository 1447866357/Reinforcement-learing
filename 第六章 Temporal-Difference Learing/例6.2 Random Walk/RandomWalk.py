from __future__  import print_function
import numpy as np
import matplotlib.pyplot as plt

# 0 is the left terminal terminal state
# 6 is the right terminal state
# 1-5 represents A-E
states = np.zeros(7)
states[1:6] = 0.5
# the right terminal state is 1,others are 0
states[6] =1

trueValue = np.zeros(7)
trueValue[1:6] = np.arange(1,6)/6.0
trueValue[6] = 1
ACTION_LEFT = 0
ACTION_RIGHT = 1

def temporalDifference(states,alpha=0.1,batch=False):
    state = 3
    trajectory= [state]
    rewards = [0]
    while True:
        oldState =state
        if np.random.binomial(1,0.5) == ACTION_LEFT:
            state -= 1
        else:
            state +=1

        reward = 0
        trajectory.append(state)
        # TD update
        if not batch:
            states[oldState] += alpha*(reward+states[state]-states[oldState])
        if state ==6 or state==0:
            break
        rewards.append(reward)
    return trajectory,rewards

def monteCarlo(states,alpha=0.1,batch=False):
    state = 3
    trajectory = [3]
    returns = 0
    while True:
        if np.random.binomial(1 , 0.5) == ACTION_LEFT:
            state -=1
        else:
            state +=1
        trajectory.append(state)
        if state == 6:
            returns =1.0
            break
        elif state ==0:
            returns = 0.0
            break
    if not batch:
        for state_ in trajectory[:-1]:
            states[state_] += alpha*(returns - states[state_])
    return trajectory,[returns]*(len(trajectory)-1)
# FIgure 6.2 left
def  stateValue():
    episodes = [0,1,10,100]
    currentStates = np.copy(states)
    plt.figure(1)
    axisX =np.arange(0,7)
    for i in range(0,episodes[-1]+1):
        if i in episodes:
            plt.plot(axisX,currentStates,label=str(i)+'episodes')
        temporalDifference(currentStates)
    plt.plot(axisX,trueValue,label='true values')
    plt.xlabel('state')
    plt.legend()

# figure 6.2 right
def RMSError():
    # some alpha value can apper in both arrays
    TDAlpha = [0.15,0.1,0.05]
    MCAlpha = [0.01,0.02,0.03,0.04]
    episodes = 100+1
    runs =100
    plt.figure(2)
    axisX = np.arange(0,episodes)
    for i,alpha in enumerate(TDAlpha + MCAlpha):
        totalErrors = np.zeros(episodes)
        linestyle = 'solid'
        if i< len(TDAlpha):
            method = 'TD'
        else:
            method = 'MC'
            linestyle ='dashdot'
        for run in range(0,runs):
            errors = []
            currentStates = np.copy(states)
            for i in range(0,episodes):
                errors.append(np.sqrt(np.sum(np.power(trueValue-currentStates,2))/5.0))
                if method == 'TD':
                    temporalDifference(currentStates,alpha=alpha)
                else:
                    monteCarlo(currentStates,alpha=alpha)
            totalErrors += np.asarray(errors)
        totalErrors /=runs
        plt.plot(axisX,totalErrors,linestyle=linestyle,label=method+',alpha='+str(alpha))
    plt.xlabel('episodes')
    plt.legend()

# figure 6.3
def batchUpdating(method,episodes,alpha=0.001):
    runs = 100
    totalErrors = np.zeros(episodes -1)
    for run in range(0,runs):
        currentStates = np.copy(states)
        errors = []
        trajectories = []
        rewards = []
        for ep in range(1,episodes):
            print('Run:',run,'Episode:',ep)
            if method =='TD':
                trajectory_ ,rewards_ =temporalDifference(currentStates,batch=True)
            else:
                trajectory_,rewards_=monteCarlo(currentStates,batch=True)
            trajectories.append(trajectory_)
            rewards.append(rewards_)
            while True:
                updates = np.zeros(7)
                for trajectory_,rewards_ in zip(trajectories,rewards):
                    for i in range(0,len(trajectory_)-1):
                        if method == 'TD':
                            updates[trajectory_[i]] += rewards_[i] + currentStates[trajectory_[i+1]]-currentStates[trajectory_[i]]
                        else:
                            updates[trajectory_[i]] += rewards_[i] - currentStates[trajectory_[i]]
                updates *= alpha
                if np.sum(np.abs(updates))< 1e-3:
                    break
                currentStates += updates
            errors.append(np.sqrt(np.sum(np.power(currentStates-trueValue,2))/5.0))
        totalErrors += np.asarray(errors)
    totalErrors /= runs
    return totalErrors

def figure6_2():
    stateValue()
    plt.savefig('1.png')
    RMSError()
    plt.savefig('2.png')
def figure6_3():
    episodes = 100 + 1
    TDErrors = batchUpdating('TD', episodes)
    MCErrors = batchUpdating('MC', episodes)
    axisX =np.arange(1, episodes)
    plt.figure(3)
    plt.plot(axisX, TDErrors, label='TD')
    plt.plot(axisX, MCErrors, label='MC')
    plt.xlabel('episodes')
    plt.ylabel('RMS error')
    plt.savefig('3.png')
    plt.legend()


figure6_3()
plt.show()