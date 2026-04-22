from src.generate_data import generate_cricket_data
from src.numpy_advanced import *

players, runs, balls = generate_cricket_data()

print("Players:", players)
print("Runs:", runs)

print("\nMemory Optimization:", memory_optimization())

print("\nString Ops:", string_operations(players))

print("\nContiguous Arrays:", contiguous_arrays())

print("\nIteration:", iteration_example(runs))

from src.linear_algebra import linear_algebra_demo

print("\nLinear Algebra Output:")
dp, mp, t, det = linear_algebra_demo()

print("Dot Product:", dp)
print("Matrix Product:\n", mp)
print("Transpose:\n", t)
print("Determinant:", det)
