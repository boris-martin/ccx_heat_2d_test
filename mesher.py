import numpy as np

# Output, geometric parameters
output_file_name = "out.msh"

x_begin, x_end = 0, 30
y_begin, y_end = 0, 10
z_begin, z_end = 0, 10

# Number of elements. Add one for number of nodes!
n_x, n_y, n_z = 10, 10, 10

# Coordinates in (i, j, k) space. i = 0, ..., n_x etc
xs = np.linspace(x_begin, x_end, n_x + 1)
ys = np.linspace(y_begin, y_end, n_y + 1)
zs = np.linspace(z_begin, z_end, n_z + 1)

# List of 3D points
nodes = []
# Map from (i,j,k) pos to index
indices = dict()

# Build nodes
for i in range(0, n_x + 1):
    for j in range(0, n_y + 1):
        for k in range(0, n_z + 1):
            nodes.append((xs[i], ys[j], zs[k]))
            # CCX index starts at 1!
            v = len(nodes)
            indices[(i, j, k)] = v

print("** Nodes")
print("*Node, NSET=Nall")
for v, (x, y, z) in enumerate(nodes):
    print("{}, {}, {}, {},".format(v + 1, x, y, z))

# Build elements
print("** Volume elements")
print("* Element, TYPE=C3D8, ELSET=Eall")

elem_id = 1
for i in range(0, n_x):
    for j in range(0, n_y):
        for k in range(0, n_z):
            print("{}, {}, {}, {}, {}, {}, {}, {}, {},".format(elem_id,
                                                               indices[(
                                                                   i, j, k)],
                                                               indices[(
                                                                   i+1, j, k)],
                                                               indices[(
                                                                   i+1, j+1, k)],
                                                               indices[(
                                                                   i, j+1, k)],
                                                               indices[(
                                                                   i, j, k+1)],
                                                               indices[(
                                                                   i+1, j, k+1)],
                                                               indices[(
                                                                   i+1, j+1, k+1)],
                                                               indices[(i, j+1, k+1)],))
            elem_id += 1

# Set of border. Adapt freely
print("** Nodes, border with x = x_begin")
print("*NSET, NSET=Nxbegin")
for j in range(0, n_y + 1):
    for k in range(0, n_z + 1):
       print("{}, ".format(indices[0, j, k]))
print("** Nodes, border with x = x_end")
print("*NSET, NSET=Nxend")
for j in range(0, n_y + 1):
    for k in range(0, n_z + 1):
        print("{}, ".format(indices[n_x, j, k]))
