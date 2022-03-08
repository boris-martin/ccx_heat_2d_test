python mesher.py > all.msh
ccx_preCICE_main heated_plate -precice-participant Solid
ccx2paraview heated_plate.frd vtk
mv *vtk ~/Bureau/shared/