import sys
import grid_mdp
import random
random.seed(0)
import matplotlib.pyplot as plt
from model_free import *

if __name__ == "__main__":
    read_best()
    plt.figure(figsize=(12, 6))
############ epsilon_greedy##############
    mc(num_iter1=5000, epsilon=0.2);
    mc(num_iter1=5000, epsilon=0.4);
    mc(num_iter1=5000, epsilon=1.0);

    sarsa(num_iter1=5000, alpha=0.2, epsilon=0.2);
    sarsa(num_iter1=5000, alpha=0.2, epsilon=0.4);
    sarsa(num_iter1=5000, alpha=0.2, epsilon=1.0)

    qlearning(num_iter1=5000, alpha=0.2, epsilon=0.2);
    qlearning(num_iter1=5000, alpha=0.2, epsilon=0.4);
    qlearning(num_iter1=5000, alpha=0.2, epsilon=1.0);



    plt.xlabel("number of iterations")
    plt.ylabel("square errors")
    plt.savefig('图1')
    plt.legend()
    plt.show()

    ############# Learning rate ##############
    mc(num_iter1=2500, epsilon=0.2);

    sarsa(num_iter1=2500, alpha=0.1, epsilon=0.2);
    sarsa(num_iter1=2500, alpha=0.2, epsilon=0.2);
    sarsa(num_iter1=2500, alpha=0.3, epsilon=0.2)

    qlearning(num_iter1=2500, alpha=0.1, epsilon=0.2);
    qlearning(num_iter1=2500, alpha=0.2, epsilon=0.2);
    qlearning(num_iter1=2500, alpha=0.3, epsilon=0.2);

    plt.xlabel("number of iterations")
    plt.ylabel("square errors")
    plt.legend()
    plt.savefig('图2')
    plt.show();

    #############near_optimal  e-greedy vs greedy##########
    print ("epsilon = 0.5")
    qfunc = mc(num_iter1=5000,epsilon=0.9)
    for s in states:
        for a in actions:
            key = "%d_%s"%(s,a)
            print ("%d_%s:%f"%(s,a,qfunc[key]))
    print ("best")
    for s in states:
        for a in actions:
            key = "%d_%s"%(s,a)
            print ("%d_%s:%f"%(s,a,best[key]))

    plt.xlabel("number of iterations")
    plt.ylabel("square errors")
    plt.legend()
    plt.savefig("图3")
    plt.show()
    #############variance##########
    mc(num_iter1= 6000,epsilon=0.2)
    mc(num_iter1=6000,epsilon=0.2)
    mc(num_iter1=6000,epsilon=0.2)
    mc(num_iter1=6000,epsilon=0.2)
    sarsa(num_iter1=6000,alpha=0.2,epsilon=0.2)
    sarsa(num_iter1=6000, alpha=0.2, epsilon=0.2)
    sarsa(num_iter1=6000, alpha=0.2, epsilon=0.2)
    sarsa(num_iter1=6000, alpha=0.2, epsilon=0.2);
    qlearning(num_iter1=6000, alpha=0.2, epsilon=0.2);
    qlearning(num_iter1=6000, alpha=0.2, epsilon=0.2);
    qlearning(num_iter1=6000, alpha=0.2, epsilon=0.2);
    qlearning(num_iter1=6000, alpha=0.2, epsilon=0.2);

    plt.xlabel("number of iterations")
    plt.ylabel("square errors")
    plt.legend()
    plt.savefig('图4')
    plt.show()

    ############comprehensive#############
    mc(num_iter1=1000, epsilon=0.1)
    mc(num_iter1=1000, epsilon=0.2)
    sarsa(num_iter1=1000, alpha=0.2, epsilon=0.1);
    sarsa(num_iter1=1000, alpha=0.4, epsilon=0.1);
    sarsa(num_iter1=1000, alpha=0.2, epsilon=0.2);
    sarsa(num_iter1=1000, alpha=0.4, epsilon=0.2);
    qlearning(num_iter1=1000, alpha=0.2, epsilon=0.1);
    qlearning(num_iter1=1000, alpha=0.4, epsilon=0.1);
    qlearning(num_iter1=1000, alpha=0.2, epsilon=0.2);
    qlearning(num_iter1=1000, alpha=0.4, epsilon=0.2);

    plt.xlabel("number of iterations")
    plt.ylabel("square errors")
    plt.legend()
    plt.savefig('图5')
