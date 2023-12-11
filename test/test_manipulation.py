# -*- coding: utf-8 -*-

import unittest
from data_muncher.manipulation import Manipulation
import time
import random

class TestManipulation(unittest.TestCase):
    def setUp(self):
        self.dataset = [
            ['Name', 'Age', 'Salary', 'Department'],
            ['Alice', 25, 50000, 'HR'],
            ['Bob', 30, 60000, 'Finance'],
            ['Charlie', 28, 55000, 'IT'],
            ['David', 35, 70000, 'Finance'],
            ['Eva', 27, 52000, 'HR'],
            ['Frank', 32, None, 'IT']
        ]

        self.manipulator = Manipulation(self.dataset)

    def column_manipulation_test(self):
        manipulated_data = self.manipulator.columnManipulation(1, lambda x: x + 1)
        print("Column Manipulation:")
        for row in manipulated_data:
            print(row)

    def data_cleaning_test(self):
        cleaned_data = self.manipulator.dataCleaning(missing_value_strategy='mean')
        print("\nData Cleaning:")
        for row in cleaned_data:
            print(row)

    def data_selection_test(self):
        selected_data = self.manipulator.dataSelection(columns=[0, 2, 3], rows=[1, 3, 5])
        print("\nData Selection:")
        for row in selected_data:
            print(row)

    def data_grouping_test(self):
        grouped_data = self.manipulator.dataGroupBy(groupby_column_idx=3, aggregation_functions={1: 'mean', 2: 'sum'})
        print("\nData Grouping:")
        for row in grouped_data:
            print(row)

    def data_sampling_test(self):
        sampled_data = self.manipulator.dataSampling(fraction=0.5)
        print("\nData Sampling:")
        for row in sampled_data:
            print(row)


if __name__ == '__main__':
    unittest.main()
