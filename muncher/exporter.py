#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import json
import xml.etree.ElementTree as ET
import sqlite3

class Exporter:
    def __init__(self, data):
        self.data = data

    def to_csv(self, file_path):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.data)

    def to_xml(self, file_path, root_tag="Data", row_tag="Row"):
        root = ET.Element(root_tag)
        for row in self.data:
            row_elem = ET.SubElement(root, row_tag)
            for i, cell in enumerate(row):
                cell_tag = f"Cell{i}"
                cell_elem = ET.SubElement(row_elem, cell_tag)
                cell_elem.text = str(cell)

        tree = ET.ElementTree(root)
        tree.write(file_path)

    def to_json(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.data, file)

    def to_sqlite(self, db_path, table_name):
        # This method assumes the first row of self.data contains column names
        # and the rest of the rows contain the data.
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Create table
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(self.data[0])})")

        # Insert rows
        for row in self.data[1:]:
            placeholders = ', '.join(['?'] * len(row))
            cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", row)

        conn.commit()
        conn.close()


# In[ ]:




