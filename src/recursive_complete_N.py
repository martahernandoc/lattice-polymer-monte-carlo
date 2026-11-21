"""
Complete enumeration of a 2D SAW of length N (N steps)

Using the exact enumeration method we compute for different values of N:
Z(N): number of SAWs
sum_r2(N): sum of the end-to-end squared distances over all SAWs
<r**2>(N): average of the squared end-to-end length

It also plots <r**2> as a function of N in logarithmic scale and the estimate of 2*nu as a function of N

Since the runtime grows quickly for N we have chosen to compute up to N=15
"""


import numpy as np
import matplotlib.pyplot as plt

move = [(1,0), (-1,0), (0,1), (0,-1)] #right, left, up, down 
x = 0; y = 0 #initial position

class SAW:

    #Attributes: N, Z, sum_r2

    def __init__(self, N):
        self.N = N
        self.Z = 0
        self.sum_r2 = 0
        self.visited = [(0,0)]
        self.move = move

    def step(self, x, y, i):
        if i == self.N:
            r2 = x**2 + y**2
            self.Z += 1
            self.sum_r2 += r2
            return

        for (dx, dy) in self.move:
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) not in self.visited:
                self.visited.append((new_x, new_y))
                self.step(new_x, new_y, i+1)
                self.visited.remove((new_x, new_y))

N_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
Z_array = []
sum_r2_array = []
mean_r2_array = []

for N in N_array:
    saw = SAW(N)
    saw.step(x, y, 0)
    Z_array.append(saw.Z)
    sum_r2_array.append(saw.sum_r2)
    mean_r2_array.append(saw.sum_r2 / saw.Z)

mean_r2 = np.array(mean_r2_array)
two_nu = (N_array[1:-1] / mean_r2[1:-1]) * (mean_r2[2:] - mean_r2[:-2]) / 2

print("Z =", Z_array)
print("sum r2 =", sum_r2_array)
print("mean r2 =", mean_r2_array)

plt.loglog(N_array, mean_r2_array, '+')
plt.xlabel('N')
plt.ylabel('Average squared end-to-end length')
plt.title('Evolution of the average length as a function of the polymer´s length')
plt.grid(True)
plt.show()

plt.plot(N_array[1:-1], two_nu, '+')
plt.xlabel('N')
plt.ylabel('2$ν$')
plt.grid(True)
plt.show()
