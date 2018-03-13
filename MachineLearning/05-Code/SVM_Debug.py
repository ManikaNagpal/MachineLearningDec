import numpy as np
import matplotlib.pyplot as plt

X = np.array([
        [-1.5, 4, -1],
        [1, 3, -1],
        [4, 1, -1],
        [3, 5, -1],
        [5, 6, -1],
        [6, 3, -1]
        ])

y = np.array([-1,-1,-1,1,1,1])

weight = np.array([  2.91092987,   3.22162823,  17.87374367])

for i, sample in enumerate(X):
    
    if i < 3:
        plt.scatter(sample[0], sample[1], marker='+', s=120, c='r')
    
    else:
        plt.scatter(sample[0], sample[1], marker='_', s=120, c='b')
        
        
x2 = np.array([weight[0], weight[1], -weight[1], weight[0]])
x3 = np.array([weight[0], weight[1], weight[1], -weight[0]])

x2x3 = np.array([x2])

X,Y,U,V = zip(*x2x3)

axes = plt.gca()

axes.quiver(X,Y,U,V, scale=100)

plt.show()
