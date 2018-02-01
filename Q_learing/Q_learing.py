import numpy as np
import pandas as pd
import time



N_STATES = 6  # 维度世界的宽度
ACTIONS = ['left', 'right']  # 探索者的动作
EPSILON = 0.1  # 贪婪度 greedy
ALPHA = 0.1  # 学习率
GAMMA = 0.9  # 奖励递减值
MAX_EPISODES = 13  # 最大回合数
FRESH_TIME = 0.3 # 移动间隔时间

def build_q_table(n_states,actions):
    table = pd.DataFrame(
        np.zeros((n_states , len(actions))),#q_table 全0初始
        columns = actions, #columns对应的是行动名称
     )
    print(table)
    return table


def choose_action(state,q_table):
    # This is how to choose an action
    state_action = q_table.iloc[state,:] # 选择某一状态下较大值
    if(np.random.uniform()>EPSILON)or(state_action.all() == 0):
        # 非贪婪or这个状态还没有探索过
        action_name = np.random.choice(ACTIONS)
    else:
        action_name = state_action.idxmax()  # 贪婪模式
    return action_name

def get_env_feedback(S ,A):
    # This is how agent will interact with the environment
    if A == 'right':   # move right
        if S == N_STATES - 2:  # terminate   # 不懂啊
            S_ = 'terminal'
            R = 1
        else:
            S_ = S+1
            R = 0
    else:
        R = 0
        if S == 0:
            S_ = S  #reach the wall
        else:
            S_ = S-1
    return S_, R

def update_env(S,episode,step_counter):
    # This is how environmene be updated
    env_list = ['-']*(N_STATES-1)+['T']  # '----T'our environment
    if S== 'terminal':
        interaction = 'Episode %s :total_steps = %s'%(episode+1,step_counter)
        print('\r{}'.format(interaction),end='')
        time.sleep(2)
        print('\r       ',end='')
    else:
        env_list[S]='o'
        interaction = ''.join(env_list)
        print('\r{}'.format(interaction),end='')
        time.sleep(FRESH_TIME)

def rl():
    q_table = build_q_table(N_STATES, ACTIONS) #初始q_table
    for episode in range(MAX_EPISODES): #回合
        step_counter = 0
        S = 0  # 回合初始位置
        is_terminated = False  # 回合是否结束
        update_env(S, episode,step_counter)  # 环境更新
        while not is_terminated:
            A= choose_action(S,q_table)  # 选择行为
            S_,R = get_env_feedback(S,A) # 实施行为并得到环境反馈
            q_predict = q_table.ix[S , A]  # 估算的状态行为值
            if S_ != 'terminal':
                q_target = R + GAMMA*q_table.iloc[S_,:].max() #实际的状态行为值（）回合没有结束
            else:
                q_target = R  # 实际的状态行为值（回合结束）
                is_terminated = True  # terminte this episode

            q_table.ix[S,A]+= ALPHA*(q_target-q_predict) #q_table更新
            S = S_ # 探索者移动到下一个state

            update_env (S,episode,step_counter+1) #环境更新

            step_counter += 1
    return q_table

if __name__ == "__main__":
    q_table = rl()
    print('\r\nQ-table:\n')
    print(q_table)