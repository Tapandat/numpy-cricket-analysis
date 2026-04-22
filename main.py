from src.generate_data import generate_cricket_data
from src.numpy_advanced import *

players, runs, balls = generate_cricket_data()

print("Players:", players)
print("Runs:", runs)

print("\nMemory Optimization:", memory_optimization())

print("\nString Ops:", string_operations(players))

print("\nContiguous Arrays:", contiguous_arrays())

print("\nIteration:", iteration_example(runs))
