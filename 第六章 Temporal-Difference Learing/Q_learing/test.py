from maze_env import Maze
from RL_brain import QLearningTable

def update():
    for episode in range(100):
         # initial observation
        observation = env.reset()

        while True:
            # env.render（）
            env.render()

            # rl choose action based on observation
            action = RL.choose_action(str(observation))

            # RL take action and get next obsevation and reward
            observation_, reward, done=env.step(action)

            # RL learn from this transition
            RL.learn(str(observation), action,reward,str(observation_))

            #swap observation
            observation = observation_

            # break while looop when end this episode

            if done:
                break
    # end of game
    print('game over')
    env.destory()

if __name__ == "__main__":
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    env.after(100, update)
    env.mainloop()