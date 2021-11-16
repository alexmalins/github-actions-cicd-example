from typing import List, Tuple
import numpy as np

try:
    from importlib import resources
except ImportError:
    import importlib_resources as resources

def add_vectors(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """ Adds two numpy vectors """
    
    return a + b


def load_datafile(filename: str) -> Tuple[List[str], List[int]]:
    """ Loads people's names and ages from a TSV file """

    names = []
    ages = []

    with resources.open_text(f"{__package__}.data", filename) as file:
        for idx, line in enumerate(file.readlines()):
            if idx == 0:
                continue
            lineentries = line.split()
            names.append(lineentries[0])
            ages.append(int(lineentries[1]))

    return (names, ages)
