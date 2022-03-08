import precice
import numpy as np

interface = precice.Interface("Fluid", "precice-config.xml", 0, 1)

dim = interface.get_dimensions()
meshID = interface.get_mesh_id("Fluid-Mesh")
vertex_size = 1

coords = np.zeros((vertex_size, dim))
coords[0, :] = np.array([0, 0])



print(coords)

vertices_id = interface.set_mesh_vertices(meshID, coords)

temperature = np.array([350])
tempID = interface.get_data_id("Temperature", meshID)

dt = interface.initialize()

while interface.is_coupling_ongoing():
    interface.write_block_scalar_data(tempID, vertices_id, temperature)
    dt = interface.advance(dt)
    print(dt)

interface.finalize()