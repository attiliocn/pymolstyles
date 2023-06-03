#!/usr/bin/env python3

import sys, argparse
import numpy as np
import morfeus

parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('atom1', type=int)
parser.add_argument('atom2', type=int, nargs='+')
args = parser.parse_args()


def get_angle(v1, v2):
    inner = np.inner(v1, v2)
    norms = np.linalg.norm(v1) * np.linalg.norm(v2)
    cos = inner / norms
    rad = np.arccos(np.clip(cos, -1.0, 1.0))
    deg = np.rad2deg(rad)
    return deg

elements, coordinates = morfeus.read_xyz(args.file)

sterimol = morfeus.Sterimol(elements, coordinates, args.atom1, args.atom2)
rotation_matrix = sterimol._rotation_matrix

print()
print(f'Sterimol results for {args.file}')
print("{:<20}{:<20.5}".format("L (uncorrected)", sterimol.L_value_uncorrected))
print("{:<20}{:<20.5}".format("B1", sterimol.B_1_value))
print("{:<20}{:<20.5}".format("B5", sterimol.B_5_value))
print()
print("{:<20}{:<20.1f}".format("Angle <L,B1>", get_angle(sterimol.L, sterimol.B_1)))
print("{:<20}{:<20.1f}".format("Angle <L,B5>", get_angle(sterimol.L, sterimol.B_5)))
print("{:<20}{:<20.1f}".format("Angle <B1,B5>", get_angle(sterimol.B_1, sterimol.B_5)))
print("{:<20}{:<20.5}".format("B1/L", sterimol.B_1_value/sterimol.L_value_uncorrected))
print("{:<20}{:<20.5}".format("B5/L", sterimol.B_5_value/sterimol.L_value_uncorrected))
print("{:<20}{:<20.5}".format("B1/B5", sterimol.B_1_value/sterimol.B_5_value))
print()

sterimol_vectors = np.zeros(9).reshape(3,3)
sterimol_vectors[0] = sterimol.L
sterimol_vectors[1] = sterimol.B_1
sterimol_vectors[2] = sterimol.B_5

coordinates_rotation = (rotation_matrix @ coordinates.T).T
sterimol_vectors_rotation = (rotation_matrix.T @ sterimol_vectors.T).T
sterimol_vectors_rotation = sterimol_vectors_rotation + coordinates[args.atom1-1]

args.atom2 = np.array(args.atom2)
atom2_center = (np.sum(coordinates[args.atom2-1], axis=0)/(len(args.atom2))).round(2)

coordinates = coordinates.round(2)
sterimol_vectors_rotation = sterimol_vectors_rotation.round(2)

print("Use the command below in PyMOL to plot the sterimol vectors")
print("----")
print(f"plot_sterimol [{list(coordinates[args.atom1-1])}, {list(atom2_center)}], [{list(sterimol_vectors_rotation[0])}, {list(sterimol_vectors_rotation[1])}, {list(sterimol_vectors_rotation[2])}]")
print("----")