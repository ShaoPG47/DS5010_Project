# -*- coding: utf-8 -*-

import time
import random

class Manipulation:
    def __init__(self, dataset):
        self.dataset = dataset

    def columnManipulation(self, column_idx, manipulation_function):
        """
        Purpose: Manipulate a specific column in the dataset using a provided function.

        Parameters:
        column_idx: The index of the column to be manipulated.
        manipulation_function: The function to be applied to the column.
        """
        for i in range(1, len(self.dataset)):
            self.dataset[i][column_idx] = manipulation_function(self.dataset[i][column_idx])
        return self.dataset

    def dataCleaning(self, missing_value_strategy='mean'):
        """
        Purpose: Handling missing values for numerical data.

        Parameters:
        missing_value_strategy (str, default 'mean'): The strategy to handle missing values.
          Possible values: 'mean', 'median', 'mode', 'remove' (remove rows with missing values).
        """
        cleaned_data = [self.dataset[0]]
        for i, row in enumerate(self.dataset[1:]):
            cleaned_row = {}
            for j, value in enumerate(row):
                if isinstance(value, (int, float)):
                    cleaned_row[j] = value
                elif value is None or value == '':
                    if missing_value_strategy == 'mean':
                        values = [float(r[j]) for r in self.dataset[1:] if isinstance(r[j], (int, float))]
                        cleaned_row[j] = sum(values) / len(values) if values else None
                    elif missing_value_strategy == 'median':
                        values = sorted([float(r[j]) for r in self.dataset[1:] if isinstance(r[j], (int, float))])
                        cleaned_row[j] = values[len(values) // 2] if values else None
                    elif missing_value_strategy == 'mode':
                        values = [float(r[j]) for r in self.dataset[1:] if isinstance(r[j], (int, float))]
                        cleaned_row[j] = max(set(values), key=values.count) if values else None
                    elif missing_value_strategy == 'remove':
                        continue  # Skip rows with missing values
                else:
                    cleaned_row[j] = value

            cleaned_data.append(cleaned_row)

        return cleaned_data

    def dataSelection(self, columns=None, rows=None):
        """
        Purpose: Select specific columns or rows from the dataset.

        Parameters:
        columns: List of column indices to be selected.
        rows: List of row indices to be selected.
        """
        selected_data = [self.dataset[0]]  # Include header in the selected data
        for i, row in enumerate(self.dataset[1:]):
            selected_row = {}
            if rows is None or i in rows:
                for j, value in enumerate(row):
                    if columns is None or j in columns:
                        selected_row[j] = value
                selected_data.append(selected_row)

        return selected_data

    def dataGroupBy(self, groupby_column_idx, aggregation_functions):
        """
        Purpose: Group data by a specified column and apply aggregation functions.

        Parameters:
        groupby_column_idx: The index of the column by which the data should be grouped.
        aggregation_functions: A dictionary where keys are column indices and
          values are aggregation functions (e.g., 'sum', 'mean', 'max').
        """
        grouped_data = {}
        for row in self.dataset[1:]:
            group_key = row[groupby_column_idx]
            if group_key not in grouped_data:
                grouped_data[group_key] = {col_idx: [] for col_idx in aggregation_functions.keys()}

            for column_idx, agg_function in aggregation_functions.items():
                value = float(row[column_idx]) if isinstance(row[column_idx], (int, float)) else None

                if agg_function == 'sum' and value is not None:
                    grouped_data[group_key][column_idx].append(value)
                elif agg_function == 'mean' and value is not None:
                    grouped_data[group_key][column_idx].append(value)

        aggregated_data = [self.dataset[0]]
        for group_key, group_data in grouped_data.items():
            aggregated_row = {groupby_column_idx: group_key}
            for column_idx, agg_function in aggregation_functions.items():
                if column_idx in group_data:
                    if agg_function == 'sum':
                        aggregated_row[column_idx] = sum(group_data[column_idx])
                    elif agg_function == 'mean':
                        aggregated_row[column_idx] = sum(group_data[column_idx]) / len(group_data[column_idx]) if len(group_data[column_idx]) > 0 else None
                    # Add more aggregation functions as needed
            aggregated_data.append(aggregated_row)

        return aggregated_data

    def dataSampling(self, fraction):
        """
        Purpose: Randomly sample a fraction of the dataset.

        Parameters:
        fraction: The fraction of the dataset to be sampled.
        """
        seed = int(time.time())
        dataset_copy = self.dataset[1:].copy()

        sampled_data = [self.dataset[0]]  # Include header in the sampled data
        total_size = len(dataset_copy)
        sample_size = int(total_size * fraction)

        for _ in range(sample_size):
            index = seed % len(dataset_copy)
            sampled_data.append(dataset_copy.pop(index))
            seed += 1

        return sampled_data

    def dataPivoting(self, pivot_column_idx, value_column_idx):
        """
        Purpose: Pivot the dataset based on specified columns.

        Parameters:
        pivot_column_idx: The index of the column whose unique values become new columns.
        value_column_idx: The index of the column whose values populate the new columns.
        """
        pivoted_data = {col_idx: [] for col_idx in
                        set(row[pivot_column_idx] for row in self.dataset[1:] if isinstance(row[pivot_column_idx], (int, float)))}
        for row in self.dataset[1:]:
            pivot_value = row[pivot_column_idx]
            if isinstance(pivot_value, (int, float)):
                pivoted_data[pivot_value] = row[value_column_idx]

        return [{'pivot_column': key, 'value_column': value} for key, value in pivoted_data.items()]
