import numpy as np

def generate_cricket_data():
    players = np.array(['virat', 'rohit', 'dhoni', 'rahul'])
    runs = np.random.randint(0, 100, size=4, dtype=np.int16)
    balls = np.random.randint(1, 60, size=4, dtype=np.int16)

    return players, runs, balls
