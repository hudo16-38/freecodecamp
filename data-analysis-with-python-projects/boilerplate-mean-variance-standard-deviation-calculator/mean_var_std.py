import numpy as np
from pprint import pprint

def calculate(data):
    if len(data) != 9:
        raise ValueError("List must contain nine numbers.")
    data = np.array(data).reshape((3, 3))
    #print(type(list))

    calculations =  {
        "max" : [np.max(data, axis=0), np.max(data, axis=1), np.max(data.flatten())],
        "min" : [np.min(data, axis=0), np.min(data, axis=1), np.min(data.flatten())],
        "variance" : [np.var(data, axis=0), np.var(data, axis=1), np.var(data.flatten())],
        "standard deviation" : [np.std(data, axis=0), np.std(data, axis=1), np.std(data.flatten())],
        "mean" : [np.mean(data, axis=0), np.mean(data, axis=1), np.mean(data.flatten())],
        "sum" : [np.sum(data, axis=0), np.sum(data, axis=1), np.sum(data.flatten())]
    }

    for key, value in calculations.items():
        calculations[key] = list(map(lambda x: list(x) if isinstance(x, np.ndarray) else x, value))
    return calculations

if __name__ == "__main__":
    pprint(calculate([0,1,2,3,4,5,6,7,8]))