import unittest
import pandas as pd

""" Only on etest is written here. In future more test case ccould be written here"""


class TestDataFunctions(unittest.TestCase):

    def test_load_data(self):
        # Test that load_data successfully loads a CSV and returns a DataFrame
        test_file_path = '../data/Turbine_Data.csv'

        # Load the data using the function
        loaded_data = pd.read_csv(test_file_path)
        self.assertEqual(loaded_data.shape[1], 22, "DataFrame should have 22 columns")

   
if __name__ == "__main__":
    unittest.main()
