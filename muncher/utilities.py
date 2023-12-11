import pandas as pd
import numpy as np
import matplotlib.pyplot as plt      
from joblib import Parallel, delayed

        
class Utility:
    """
    Utility is a comprehensive toolkit for data manipulation, 
    ensuring data integrity, statistical analysis, visualization, 
    and efficient processing in Python data analysis projects.
    """
    
    # Validate Data
    def validate_data_structure(df):
        """Check if the DataFrame has a valid structure."""

        assert isinstance(df, pd.DataFrame), "Input must be a pandas DataFrame"
        if df.empty:
            raise ValueError("DataFrame is empty")
        return True
        
    def validate_data_integrity(df):
        """Check for missing values and duplicate rows in the DataFrame."""
        # Check for missing values
        if df.isnull().any().any():
            raise ValueError("DataFrame contains missing values")
        
        # Check for duplicate rows
        if df.duplicated().sum() > 0:
            raise ValueError("DataFrame contains duplicate rows")
        
        return True
        
    def check_column_types(df, column_types):
        """
        Check if columns in the DataFrame have expected types.
        
        Parameters:
        - df: pandas DataFrame.
        - column_types: dict, where keys are column names and values are types.
        """
        
        for column, expected_type in column_types.items():
            if not pd.api.types.is_dtype_equal(df[column].dtype, expected_type):
                raise ValueError(f"Column {column} does not match the expected type of {expected_type}")
        return True
        
    def check_column_values(df, column_name, valid_values):
        """
        Check if a column in the DataFrame contains only valid values.
        
        Parameters:
        - df: pandas DataFrame.
        - column_name: string, the name of the column to check.
        - valid_values: list, the valid values that the column should contain.
        """
        if not df[column_name].isin(valid_values).all():
            raise ValueError(f"Column {column_name} contains invalid values")
        return True
        
    
    # Statistical Summary
    def generate_statistics(df):
        """Generate extended statistical summaries for a DataFrame."""
        
        # Separate numeric and categorical columns
        numeric_df = df.select_dtypes(include='number')
        categorical_df = df.select_dtypes(include='object')
        
        # Basic statistical summaries for numeric columns
        numeric_summaries = numeric_df.describe()
        
        # Calculate additional statistical measures for numeric columns
        numeric_summaries.loc['mode'] = numeric_df.mode().iloc[0]
        numeric_summaries.loc['variance'] = numeric_df.var()
        numeric_summaries.loc['skewness'] = numeric_df.skew()
        numeric_summaries.loc['kurtosis'] = numeric_df.kurt()
        
        # Basic summaries for categorical columns
        categorical_summaries = categorical_df.describe(include='all')
        
        # Count unique values for categorical columns
        unique_counts = categorical_df.nunique()
        categorical_summaries.loc['unique'] = unique_counts
        categorical_summaries.loc['mode'] = categorical_df.mode().iloc[0]
        
        # Concatenate the summaries for numeric and categorical columns
        summaries = pd.concat([numeric_summaries, categorical_summaries], axis=1, sort=False)
        
        return summaries
        
    # Basic Visualizations
    def plot_data(df, column=None, x_column=None, y_column=None, kind='hist', bins=10,
                  title=None, xlabel=None, ylabel=None):
        """
        Create basic visualizations of the DataFrame using matplotlib.
        If no column is specified for histograms or boxplots, visualize the entire DataFrame.
        For scatter, line, and bar plots, specify the x and y columns.
        """

        if kind in ['hist', 'box']:
            if column:
                data_to_plot = df[column]
            else:
                data_to_plot = df
            
            if kind == 'hist':
                plt.hist(data_to_plot, bins=bins, color='skyblue', edgecolor='black')
                plt.ylabel(ylabel if ylabel else 'Frequency')
            elif kind == 'box':
                data_to_plot.plot(kind='box')
                plt.ylabel(ylabel if ylabel else 'Value')
        elif kind == 'scatter':
            plt.scatter(df[x_column], df[y_column], color='purple', alpha=0.5)
            plt.ylabel(ylabel if ylabel else y_column)
        elif kind == 'line':
            plt.plot(df[x_column], df[y_column], color='green', marker='o')
            plt.ylabel(ylabel if ylabel else y_column)
        elif kind == 'bar':
            plt.bar(df[x_column], df[y_column], color='orange', edgecolor='black')
            plt.ylabel(ylabel if ylabel else y_column)
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        plt.title(title if title else f'{kind.capitalize()} Plot')
        plt.xlabel(xlabel if xlabel else (column if column else x_column))
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        
           
        
    # Data Merging
    def merge_datasets(df1, df2, on_key, how='inner', validate=None):
        """
        Merge two pandas DataFrames based on a common key.
        
        Parameters:
        - df1 (pandas.DataFrame): The first DataFrame.
        - df2 (pandas.DataFrame): The second DataFrame.
        - on_key (str or list of str): Column or index level names to join on. 
                                      These must be found in both DataFrames.
        - how (str, default 'inner'): One of 'left', 'right', 'outer', 'inner'.
                                      Default 'inner' performs inner join.
        - validate (str, optional): If specified, checks if merge is of specified type.
        
        Returns:
        - pandas.DataFrame: The merged DataFrame.
        
        Raises:
        - ValueError: If key columns are not found in both DataFrames.
        """
        if on_key not in df1.columns or on_key not in df2.columns:
            raise ValueError(f"Key '{on_key}' not found in both DataFrames.")
        
        return df1.merge(df2, on=on_key, how=how, validate=validate)
        
        
        
    # Data Joining
    def join_datasets(df1, df2, on_key, how='inner', suffixes=('_df1', '_df2'), reset_index=True):
        """
        Join two pandas DataFrames on a key.
        
        Parameters:
        - df1 (pandas.DataFrame): The first DataFrame.
        - df2 (pandas.DataFrame): The second DataFrame.
        - on_key (str or list of str): Key column or index level to join on.
        - how (str, default 'inner'): One of 'left', 'right', 'outer', 'inner'.
        - suffixes (tuple of str, default ('_df1', '_df2')): Suffixes to apply to overlapping column names.
        - reset_index (bool, default True): Whether to reset the index of the joined DataFrame.
        
        Returns:
        - pandas.DataFrame: The joined DataFrame.
        
        Raises:
        - ValueError: If the on_key is not found in either DataFrame.
        """
        if on_key not in df1.columns or on_key not in df2.columns:
            raise ValueError(f"Key '{on_key}' not found in both DataFrames.")
        
        if on_key in df1.index.names and on_key in df2.index.names:
            joined_df = df1.join(df2, how=how, lsuffix=suffixes[0], rsuffix=suffixes[1])
        else:
            joined_df = df1.merge(df2, left_on=on_key, right_on=on_key, how=how, suffixes=suffixes)
        
        if reset_index:
            joined_df.reset_index(drop=True, inplace=True)
        
        return joined_df
        
        
    # Parallel Processing
    def parallelize_dataframe(df, func, n_cores=4):
        """Split a DataFrame into parts and apply a function in parallel."""

        df_split = np.array_split(df, n_cores)
        pool = Parallel(n_cores=n_cores)
        df = pd.concat(pool.map(delayed(func), df_split))
        pool.close()
        pool.join()
        return df


