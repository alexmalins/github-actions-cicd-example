"""Unit tests for functions exported from actionscicd package"""

import unittest
import numpy as np
from actionscicd import add_arrays, load_datafile


class TestSomeCode(unittest.TestCase):
    """Unit tests for functions in somecode.py"""

    def test_add_arrays(self) -> None:
        """Test addition of two numpy arrays"""

        arr1 = np.array([1, 2])
        arr2 = np.array([3, 4])
        self.assertTrue((add_arrays(arr1, arr2) == np.array([4, 6])).all())

    def test_load_datafile(self) -> None:
        """Test loading of people's names and ages from TSV file"""

        names = ["Bob", "Bill", "Jenny"]
        ages = [1, 2, 3]
        self.assertEqual(load_datafile("mogi_data.tsv"), (names, ages))


if __name__ == "__main__":
    unittest.main()
