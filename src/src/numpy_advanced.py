import numpy as np

# Memory Optimization
def memory_optimization():
    arr_default = np.array([10, 20, 30])
    arr_optimized = np.array([10, 20, 30], dtype=np.int8)

    return arr_default.nbytes, arr_optimized.nbytes


# String Operations
def string_operations(players):
    upper = np.char.upper(players)
    length = np.char.str_len(players)
    return upper, length


# Contiguous Arrays
def contiguous_arrays():
    arr_c = np.array([[1, 2], [3, 4]], order='C')
    arr_f = np.array([[1, 2], [3, 4]], order='F')

    return arr_c.flags['C_CONTIGUOUS'], arr_f.flags['F_CONTIGUOUS']


# Iteration Techniques
def iteration_example(runs):
    result = []

    for value in np.nditer(runs):
        result.append(int(value))

    return result
