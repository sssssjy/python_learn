import numpy as np

def create_random_start_position(loc):
    x = np.random.normal(loc['center_position'][0], 15)
    y = np.random.normal(loc['center_position'][1], 15)
    return (x, y)