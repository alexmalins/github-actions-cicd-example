"""Some basic Python code for adding two NumPy arrays and loading data from a
sub-packaged TSV file."""

from importlib import resources
from typing import Any, List, Tuple
import numpy.typing as npt


def add_arrays(arr1: npt.NDArray[Any], arr2: npt.NDArray[Any]) -> npt.NDArray[Any]:
    """Adds two numpy arrays"""

    return arr1 + arr2


def load_datafile(filename: str) -> Tuple[List[str], List[int]]:
    """Loads people's names and ages from a TSV file"""

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


def unused_fn() -> None:
    """Unused dummy function to give an example of code not covered by tests"""

    return
