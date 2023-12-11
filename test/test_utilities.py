import unittest
import pandas as pd
from muncher import Utility

class TestUtility(unittest.TestCase):

    def setUp(self):
        self.util = Utility()
        self.sample_data = pd.DataFrame({
            'A': [1, 2, 3, None, 5],
            'B': ['x', 'y', 'z', 'x', 'y'],
            'C': [1.1, 2.2, 3.3, 4.4, 5.5]
        })

    def test_validate_data_structure(self):
        self.assertTrue(self.util.validate_data_structure(self.sample_data))
        with self.assertRaises(AssertionError):
            self.util.validate_data_structure([1, 2, 3])

    def test_validate_data_integrity(self):
        self.assertTrue(self.util.validate_data_integrity(self.sample_data))
        with self.assertRaises(ValueError):
            df = self.sample_data.append(self.sample_data)
            self.util.validate_data_integrity(df)

    def test_check_column_types(self):
        column_types = {'A': pd.Int64Dtype(), 'B': object, 'C': float}
        self.assertTrue(self.util.check_column_types(self.sample_data, column_types))
        with self.assertRaises(ValueError):
            wrong_column_types = {'A': float}
            self.util.check_column_types(self.sample_data, wrong_column_types)

    def test_check_column_values(self):
        valid_values = ['x', 'y', 'z']
        self.assertTrue(self.util.check_column_values(self.sample_data, 'B', valid_values))
        with self.assertRaises(ValueError):
            invalid_values = ['a', 'b', 'c']
            self.util.check_column_values(self.sample_data, 'B', invalid_values)

    def test_generate_statistics(self):
        stats = self.util.generate_statistics(self.sample_data)
        self.assertIn('mean', stats)
        self.assertIn('unique', stats)

    def test_plot_data(self):
        # Plotting functions are usually visually inspected and might not require automated tests
        # But you can ensure that they run without error
        self.util.plot_data(self.sample_data, column='A', kind='hist')

    def test_merge_datasets(self):
        df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2'], 'A': ['A0', 'A1', 'A2']})
        df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2'], 'B': ['B0', 'B1', 'B2']})
        merged = self.util.merge_datasets(df1, df2, 'key')
        self.assertEqual(list(merged.columns), ['key', 'A', 'B'])

    def test_join_datasets(self):
        df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2']}, index=['K0', 'K1', 'K2'])
        df2 = pd.DataFrame({'B': ['B0', 'B1', 'B2']}, index=['K0', 'K1', 'K2'])
        joined = self.util.join_datasets(df1, df2, 'key')
        self.assertEqual(list(joined.columns), ['A', 'B'])

    def test_parallelize_dataframe(self):
        def func(df):
            return df.assign(C=df['A']*2)

        result = self.util.parallelize_dataframe(self.sample_data, func)
        self.assertTrue('C' in result.columns)

# Run the tests
if __name__ == '__main__':
    unittest.main()
