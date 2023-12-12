# Muncher
A python package for data analytics.<br />
[Package Main Website](https://github.com/ShaoPG47/DS5010_Project.git)

## Description
Muncher is a package that provides importing, merging, manipulation, and exporting.
It also supports data visualization and statistical analysis.

## Installation
This package can be installed by downloading the source code directly or install from git repo using pip
```bash
pip install git+https://github.com/ShaoPG47/muncher.git
```

## Usage

### 1. Importer
Importer is a tool for reading in .csv files without using any external packages,
it contains certain functions that can help users to understand some basic informations of the 
dataset.

#### Load in csv file
```py
from muncher import Importer as imp

df = imp("your_csv_file.csv")
df.readCsv()
```

#### Data Visualization
```py
df.table() #Convert data set to a table with row index and column index
df.colnames #Prints out column names
df.header #Print out the begining of the data set as table with default length of 5 rows
```
#### Accessing Data
```py
df[i,j] #Access the element on the ith row and jth column
df['column_name'] #Access the elements under "column name"
```
#### Data handling
```py
df.addrow() #Add a row
df.droprow() #Drop a row
df.addcol() #Add a column
df.dropcol() #Drop a column by index or column name
df.dropna() #Drop all rows with NA values
```

### 2. Merger
Merger is a tool for multiple data merging, it helps user to understand 
which pair of importer type data sets in the the data sets list has common columns and it's name.

#### Create the data set list
```py
from muncher import Importer as imp
from muncher import Merger as meg
df1 = imp("your_csv_file.csv")
df2 = imp("your_csv_file.csv")
df1.readCsv()
df2.readCsv()

df_list = [df1,df2]
```
#### Merging
```py
meg_list = meg(df_list)
meg_list.commonCols() #Returns the common column names of each pair in the data list
meg_list.merge([i,j], key) #left merge the ith and jth element in data list by key
```

### 3. Manipulation
The Manipulation module involves performing fundamental data processing tasks such as data cleaning, sampling and selection.
#### Create Dataset
```py
from muncher import Manipulation

dataset = [
            ['Name', 'Age', 'Salary', 'Department'],
            ['Alice', 25, 50000, 'HR'],
            ['Bob', 30, 60000, 'Finance'],
            ['Charlie', 28, 55000, 'IT'],
            ['David', 35, 70000, 'Finance'],
            ['Eva', 27, 52000, 'HR'],
            ['Frank', 32, None, 'IT']
        ]

df = Manipulation(dataset)
```

#### Data Manipulation
```py
# add 1 for each row in column 1
df.columnManipulation(1, lambda x: x + 1)

# handle missing value using mean for numerical data
df.dataCleaning(missing_value_strategy='mean')

# select data in specific columns and rows
df.dataSelection(columns=[0, 2, 3], rows=[1, 3, 5])

# get mean of column 1 and sum of column 2 for distinct value of column 3
df.dataGroupBy(groupby_column_idx=3, aggregation_functions={1: 'mean', 2: 'sum'})

# random sample 50% of data
df.dataSampling(fraction=0.5)
```

### 4. Utilities
Utility is a comprehensive toolkit for ensuring data integrity, statistical analysis, visualization, 
and efficient processing in Python data analysis projects.
#### Validate Data Structure 
```py
import pandas as pd
from muncher.utilities import Utility

# Create a DataFrame for testing
df = pd.DataFrame({
    'A': [1, 2, 3, None, 5],
    'B': ['x', 'y', 'z', 'x', 'y'],
    'C': [1.1, 2.2, 3.3, 4.4, 5.5]
})
print(Utility.validate_data_structure(df))
# Output: True
```
#### Validate Data Integrity 
```py
print(Utility.validate_data_integrity(df))
# Output:ValueError: DataFrame contains missing values
```
#### Check Column Values 
```py
# Check if a column in the DataFrame contains only valid values
valid_values_for_A = [1, 2, 3, 5]
print(Utility.check_column_values(df, 'A',valid_values_for_A))
# Output: ValueError: Column A contains invalid values
```
#### Statistical Summary 
```py
# Generate extended statistical summaries for a DataFrame
summary = Utility.generate_statistics(df)
# Output: ValueError: Column A contains invalid values
```
#### Basic Visualizations 
```py
plot = Utility.plot_data(df, 'A', kind ='box')
```

### 5. Exporter
The Exporter module in Muncher is designed for exporting data to various formats such as CSV, XML, JSON, and SQLite databases. This tool allows users to easily convert and export data for diverse applications.

#### Export to CSV file
```py
from muncher import exporter as exp

data = [[...]]  # Your data here
exporter = exp.Exporter(data)
exporter.to_csv('path/to/yourfile.csv')
```

#### Export to XML
```py
exporter.to_xml('path/to/yourfile.xml', root_tag='YourRootTag', row_tag='YourRowTag')
```

#### Export to JSON
```py
exporter.to_json('path/to/yourfile.json')
```

#### Export to SQLite Database
```py
exporter.to_sqlite('path/to/database.db', 'your_table_name')
```

#### Notes
Ensure data is correctly formatted for each export type.
For SQLite export, the first row in your data should contain the column names.
Customize XML tags to suit your data structure.

## Known Issues
1. importer.table() function would not work if there is NA values in data set <br />


## Authors
#### Anqi Guo
Contact Info: [guoanqi57@gmail.com](guoanqi57@gmail.com) <br />
Main Contributions: utilities

#### Zhenan Zhuang
Contact Info: [z28964713@gmail.com](z28964713@gmail.com) <br />
Main Contributions: manipulation

#### Zuoming Zhang
Contact Info: [zhang.zu@northeastern.edu](zhang.zu@northeastern.edu) <br />
Main Contributions: exporter

#### Pengli Shao
Contact Info: [shao.pe@northeastern.edu](shao.pe@northeastern.edu) <br />
Main Contributions: muncher.importer, muncher.merger

## Reference



