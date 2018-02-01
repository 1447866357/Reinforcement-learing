import  matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:

    rw = RandomWalk()
    rw.fill_walk()

    plt.figure(figsize=(11,11))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Reds,edgecolors='none',s=15)

    plt.scatter(0, 0, c='green', edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='Blue', edgecolors='none', s=100)

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.savefig('d.png', bbox_inchees='tight')
    plt.show()

    keep_runing = input("Make another walk? (y/n):")
    if keep_runing == 'n':
        break