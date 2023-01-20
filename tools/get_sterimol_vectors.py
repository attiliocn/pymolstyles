#!/usr/bin/env python3

import sys, argparse
import numpy as np
import morfeus

parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('atom1', type=int)
parser.add_argument('atom2', type=int, nargs='+')
args = parser.parse_args()

elements, coordinates = morfeus.read_xyz(args.file)

sterimol = morfeus.Sterimol(elements, coordinates, args.atom1, args.atom2)
rotation_matrix = sterimol._rotation_matrix

sterimol_vectors = np.zeros(9).reshape(3,3)
sterimol_vectors[0] = sterimol.L
sterimol_vectors[1] = sterimol.B_1
sterimol_vectors[2] = sterimol.B_5

coordinates_rotation = (rotation_matrix @ coordinates.T).T
sterimol_vectors_rotation = (rotation_matrix.T @ sterimol_vectors.T).T
sterimol_vectors_rotation = sterimol_vectors_rotation + coordinates[args.atom1-1]

coordinates = coordinates.round(3)
sterimol_vectors_rotation = sterimol_vectors_rotation.round(3)

print(f"sterimol {list(coordinates[args.atom1-1])},[{list(sterimol_vectors_rotation[0])}, {list(sterimol_vectors_rotation[1])}, {list(sterimol_vectors_rotation[2])}]")