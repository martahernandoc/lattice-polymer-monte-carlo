"""
Dynamics of a self-avoiding polymer inside a 2D lattice with a pore 

The polymer moves as a 'slithering snake' where all the monomers follow the 'head' and tries to scape throught the pore 
The path followed by the polymer is also shown as an animation
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

move = np.array([(1,0), (-1,0), (0,1), (0,-1)]) #right, left, up, down 
N = 10
position = np.zeros((N+1, 2))
new_pos = position[0]
pos_time = [position.copy()] #(IMPORTANT) we need the .copy() so we don't only get the last array
#position is a matrix of two rows (x,y) and N+1 columns (monomers), and the pos_time will store all the past positions

L=4

"""
FUNCTIONs THAT CHECK IF THE HEAD IS IN THE SQUARE OR PORE
"""
def in_box(new_pos, L):
    return (abs(new_pos[0]) < L) and (abs(new_pos[1]) < L)

def at_pore(new_pos, L, pore_center=[L, 0], pore_half_size= 2):
    return (new_pos[0] == pore_center[0]) and (abs(new_pos[1] - pore_center[1]) <= pore_half_size)

def check(new_pos, L, pore_center=[L, 0], pore_half_size= 3):
    if in_box(new_pos, L):
        return "inside"
    elif at_pore(new_pos, L):
        return "outside"
    else:
        return False

"""
FUNCTION THAT GENERATES THE SARW
"""
def generate_RW_N(pos, move, new_pos=position[0]):
    """
    Parameters:

    pos: current polymer configuration
    move: array of possible lattice moves
    new_pos: proposed new position for the 'head' of the polymer
    
    Returns:

    pos: updated configuration of the polymer
    moved: True if the move is accepted, False if it is forbidden 
    state: state of the head after the move
    """
    i = np.random.randint(4)
    new_pos = pos[0] + move[i]
    if check(new_pos, L)=="outside":
        if any(np.array_equal(new_pos, p) for p in pos):
            return pos, False, "inside"
        else:
            pos[1:] = pos[:-1]
            pos[0] = new_pos
        return pos, True, "escaped"
    
    if check(new_pos, L)=="inside":
        if any(np.array_equal(new_pos, p) for p in pos):
            return pos, False, "inside"
        else:
            pos[1:] = pos[:-1]
            pos[0] = new_pos
        return pos, True, "inside"
    else:
        return pos, False, "inside"

"""
THE POLYMER MOVES
"""
pore_half_size= 2
m = 0
max = 1000
while check(position[0,:], L):
    position, moved, state = generate_RW_N(position, move)
    m += 1
    if moved:
        pos_time.append(position.copy())

    if state == "escaped":
        print(f"Polymer has escaped through the pore! in {m} steps")
        break

    if m >= max:
        print(f"Simulation stopped: polymer did not escape after max steps (steps={m})")
        break 

"""
CODE TO PLOT THE ANIMATED POLYMER
"""
sqr_xside = [-L,L,L,-L,-L]
sqr_yside = [-L,-L,L,L,-L]
fig, ax = plt.subplots()
line, = ax.plot([], [], 'o-') #we need the comma bc ax.plot creates a list and add it to the axes, so we want it to unpack the first (and only) list added to the axes 
ax.axis('equal')
ax.grid(True)
ax.set_xlim(-L, L)
ax.set_ylim(-L-5, L+5)
mask = [-L, 0.0 - pore_half_size] and [L, 0.0 + pore_half_size]
plt.plot(sqr_xside,sqr_yside)#plots the boundaries as a square
plt.plot([L, L], [-pore_half_size, pore_half_size],linewidth=5, color='green')

def update(frame): #for each frame we need an update so the plot is animates
    pos = pos_time[frame]
    line.set_data(pos[:,0],pos[:,1]) #this updates the data for each frame
    return line

ani = animation.FuncAnimation(fig, update, frames=len(pos_time), interval=100)
ani.save("animation.gif", writer="pillow", fps=10)
plt.show()
