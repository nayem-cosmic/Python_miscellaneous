# Finite Element Analysis Code for 2-D Truss
# Author : Zulkar Nayem <nayem.cosmic@gmail.com>
# I'm grateful to Jack Chessa <https://www.youtube.com/channel/UCpuD3HnxvCV10ucnIZluELg> for matlab code

# imports
import numpy as np
from scipy.sparse.linalg import cg

# ---------------------- INPUT -------------------------- #

# nodal coordinates
nodes = np.array([
    [0,0],
    [20,0],
    [20,15],
    [0,15]
    ])*12

# nodal connectivity
connectivity = np.array([
    [1,2],
    [1,3],
    [2,4],
    [2,3],
    [4,3],
    [1,4]
    ])

# dof sum
ndof = nodes.size

# properties
A = 1.0
E = 10e6

# force matrix
F = np.zeros((ndof,1))
F[5] = 1000

# boundary condition
unconstrained = np.array([2,3,4,5]) # unconstrained DOF's

# ------------------- END OF INPUT ---------------------- #

# global stiffness matrix
K = np.zeros((ndof,ndof))

# global displacement matrix
D = np.zeros((ndof,1))

for n1, n2 in connectivity:
    # local node 1 coordinate
    x1 = nodes[n1-1][0]
    y1 = nodes[n1-1][1]

    # local node 2 coordinate
    x2 = nodes[n2-1][0]
    y2 = nodes[n2-1][1]

    # element length
    L = np.sqrt((x2-x1)**2+(y2-y1)**2)

    # cos theta
    C = (x2-x1)/L
    
    # sin theta
    S = (y2-y1)/L

    # element stiffness matrix
    Ke = (A*E/L)*np.array([
        [C*C, C*S, -C*C, -C*S],
        [C*S, S*S, -C*S, -S*S],
        [-C*C, -C*S, C*C, C*S],
        [-C*S, -S*S, C*S, S*S]
        ])

    # scatter matrix; helps putting element stiffness matrix into global stiffness matrix
    scatter  = np.array([2*n1-2, 2*n1-1, 2*n2-2, 2*n2-1])

    # putting element stiffness matrix into global stiffness matrix
    for i, loc in enumerate(scatter):
        K[loc][scatter] = K[loc][scatter] + Ke[i][range(4)]

# final stiffness matrix dimension after elimination
nsolution = unconstrained.size
Kf = np.zeros((nsolution,nsolution))

for i, loc in enumerate(unconstrained):
    Kf[i][range(nsolution)] = K[loc][unconstrained]

# conjugate gradient method
D[unconstrained] = np.array(cg(Kf, F[unconstrained])[0]).reshape((nsolution,1))

#D[unconstrained] = np.linalg.solve(Kf, F[unconstrained])

#print nodal displacements
f = open("report.txt", "w")
header = "NODE               X-DSISPLACEMENT                  Y-DISPLACEMENT"
print header
f.write(header+"\n")
for i in range(ndof/2):
    row = "{:>2}            {:>20}            {:>20}".format(i+1, D[2*(i+1)-2][0], D[2*(i+1)-1][0])
    print row
    f.write(row+"\n")
f.close()
