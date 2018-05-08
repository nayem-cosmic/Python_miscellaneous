import numpy as np
from scipy.sparse.linalg import cg

class Node:
    def __init__(self, numnode, xcord, force):
        self.num = numnode # node number
        self.x = xcord # x coordinate
        self.f = force # force
        self.d = 0

class Element(Node):
    def __init__(self, numele, node1, node2, xarea, melas, tdof):
        self.num = numele # element number
        self.n1 = node1
        self.n2 = node2
        self.xa = xarea # cross sectional area
        self.me = melas # modulus of elasticity
        self.M = np.zeros((tdof, tdof), float)
        self.le = self.n2.x - self.n1.x # element length
        self.eta = 0 # strain
        self.sigma = 0 # stress

node_table = []
element_table = []
constrained_nodes = []

fr = open("in_data.txt", 'r')
fw = open("out_data.txt", 'w')

header = fr.readline()
tn, te, ndof = [int(item) for item in fr.readline().split()]
N = tn*ndof
K = np.zeros((N, N), float)

header = fr.readline()
for i in range(tn):
    nnum, xc, is_con, force = [float(item) for item in fr.readline().split()]
    if is_con>0:
        constrained_nodes.append(int(nnum-1))
    node_table.append(Node(int(nnum-1), xc, force))

header = fr.readline()
for i in range(te):
    enum, nnum1, nnum2, xa, xe = [float(item) for item in fr.readline().split()]
    element_table.append(Element(int(enum-1), node_table[int(nnum1-1)], node_table[int(nnum2-1)], xa, xe, N))

for i, item in enumerate(element_table):
    item.M[i, i] = item.me*item.xa/item.le
    item.M[i, i+1] = -item.me*item.xa/item.le
    item.M[i+1, i] = -item.me*item.xa/item.le
    item.M[i+1, i+1] = item.me*item.xa/item.le

for item in element_table:
    K += item.M

C = abs(np.amax(K)) if abs(np.amax(K))>abs(np.amin(K)) else abs(np.amin(K))

for item in constrained_nodes:
    K[item, item] += C*10**8

F = np.array([item.f for item in node_table])

# solving matrix
D = cg(K, F)[0]

# adding displacement to class variable
for i, item in enumerate(D):
    node_table[i].d = item if item>10**-5 else 0

# calculating strain and stress
for item in element_table:
    item.eta = (-item.n1.d+item.n2.d)/(item.n2.x-item.n1.x)
    item.sigma = item.me*item.eta

print("NodeIndex        Displacement")
fw.write("NodeIndex        Displacement\n")

for item in node_table:
    print("{:9} {:19.4f}".format(item.num+1, item.d))
    fw.write("{:9} {:19.4f}\n".format(item.num+1, item.d))

print("ElementIndex              Stress              Strain")
fw.write("\nElementIndex              Stress              Strain\n")

for item in element_table:
    print("{:12} {:19.4f} {:19.4f}".format(item.num+1, item.sigma, item.eta))
    fw.write("{:12} {:19.4f} {:19.4f}\n".format(item.num+1, item.sigma, item.eta))

fr.close()
fw.close()
