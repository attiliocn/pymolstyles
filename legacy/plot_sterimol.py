import ast

def plot_sterimol(origin, sterimol_coordinates):
    cmd.delete('*_vector')

    origin = ast.literal_eval(origin)
    sterimol_coordinates = ast.literal_eval(sterimol_coordinates)

    cmd.pseudoatom('c', pos=origin, elem='Cs')
    cmd.pseudoatom('L', pos=sterimol_coordinates[0], elem='Cs')
    cmd.pseudoatom('B1', pos=sterimol_coordinates[1], elem='Cs')
    cmd.pseudoatom('B5', pos=sterimol_coordinates[2], elem='Cs')

    cgo_arrow('/c','/L', 0.1, color='red', name='L_vector')
    cgo_arrow('/c','/B1', 0.1, color='green', name='B1_vector')
    cgo_arrow('/c','/B5', 0.1, color='blue', name='B5_vector')

    cmd.delete('c')
    cmd.delete('L')
    cmd.delete('B1')
    cmd.delete('B5')
   
cmd.extend('sterimol', plot_sterimol)
