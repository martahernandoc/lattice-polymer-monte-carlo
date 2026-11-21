"""
Markov Chain Monte Carlo method for a 2D SAW of leght N (N steps)

This script implements the method of local moves by selecting a random monomer, computing the possible moves and rejecting the ones that violate self-avoidance

It is not finished and it will include measurements such as <r**2>
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

move = np.array([(1,0), (-1,0), (0,1), (0,-1)]) #right, left, up, down 

class Markov_chain:
    def __init__(self):
        self.N = 10
        self.position = np.array([[i,0] for i in range(self.N + 1)])
        self.rng = np.random.default_rng()

    def posible_steps(self, m):

        """
        Parameter:
        
        pos: current polymer configuration
        m: random monomer chosen

        Returns:

        posible steps that the monomer chosen can take (withought taking into account self-avoidance)
        """
        def check_dist(a, b):
            d = b - a
            return abs(d[0]) + abs(d[1]) == 1

        candidates = [self.position[m]]
        if m == 0:
            candidates.extend([self.position[1] + move[i] for i in range(len(move))])
            return candidates
        if m == self.N:
            candidates.extend([self.position[self.N - 1] + move[i] for i in range(len(move))])
            return candidates
        else:
            for i in range(len(move)):
                new_pos = self.position[m] + move[i]
                if check_dist(new_pos, self.position[m + 1]) and check_dist(new_pos, self.position[m - 1]):
                    candidates.append(new_pos)
            return candidates

    def local_move(self):
        """
        Perdorm one local-move for the polymer

        steps followed:
        1. chooses a random monomer m
        2. computes all the candidate positions
        3. rejects the candidates that don't satisfy self-avoidance
        4. choose randomly the next move from the allowed candidates
        """
        m = self.rng.integers(0, self.N + 1) #random monomer from the polymer
        candidates = self.posible_steps(m)
        allowed = []
        for c in candidates:
            if not any(np.array_equal(c, p) for p in self.position):
                allowed.append(c)

        if len(allowed) == 0:
            return self.position, False #stays in the same spot
        else:
            new_pos = self.position.copy()
            new_pos[m] = allowed[np.random.randint(len(allowed))]
            self.position = new_pos
            return self.position, True #moved to a random of the allowed positions
        
    def delta_x(self):
        """
        End-to-end distance projected on the x axis
        """
        return self.position[-1, 0] - self.position[0, 0]

saw = Markov_chain()
print(saw.delta_x())
max_steps = 200000
t_neg = None
for t in range(1, max_steps):
    position, moved = saw.local_move()
    if saw.delta_x() < 0:
        t_neg = t
        break
print(t_neg, saw.delta_x())
