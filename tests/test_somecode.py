import unittest
import numpy as np
from actionsci import add_vectors, load_datafile

class TestSomeCode(unittest.TestCase):
    """ Unit tests for somecode.py """

    def test_add_vectors(self) -> None:
        """ Test addition of two numpy vectors """

        a = np.array([1, 2])
        b = np.array([3, 4])
        self.assertTrue(np.alltrue((add_vectors(a, b) == np.array([4, 6]))))

    def test_load_datafile(self) -> None:
        """ Test loading of people's names and ages from TSV file """

        names = ["Bob", "Bill", "Jenny"]
        ages = [1, 2, 3]
        self.assertEqual(load_datafile("mogi_data.tsv"), (names, ages))

if __name__ == "__main__":
    unittest.main()
