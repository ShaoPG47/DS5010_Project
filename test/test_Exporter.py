#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
import os
import sqlite3
import xml.etree.ElementTree as ET
import json
from exporter import Exporter

class TestExporter(unittest.TestCase):

    def setUp(self):
        self.test_data = [["Header1", "Header2"], ["Row1Col1", "Row1Col2"], ["Row2Col1", "Row2Col2"]]
        self.exporter = Exporter(self.test_data)

    def test_to_csv(self):
        file_path = "test.csv"
        self.exporter.to_csv(file_path)
        self.assertTrue(os.path.exists(file_path))
        os.remove(file_path)

    def test_to_xml(self):
        file_path = "test.xml"
        self.exporter.to_xml(file_path)
        self.assertTrue(os.path.exists(file_path))
        tree = ET.parse(file_path)
        root = tree.getroot()
        self.assertEqual(len(root), len(self.test_data) - 1)  # Assuming first row is header
        os.remove(file_path)

    def test_to_json(self):
        file_path = "test.json"
        self.exporter.to_json(file_path)
        self.assertTrue(os.path.exists(file_path))
        with open(file_path, 'r') as file:
            data = json.load(file)
        self.assertEqual(data, self.test_data)
        os.remove(file_path)

    def test_to_sqlite(self):
        db_path = "test.db"
        table_name = "test_table"
        self.exporter.to_sqlite(db_path, table_name)

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        self.assertEqual(len(rows), len(self.test_data) - 1)  # Assuming first row is header
        conn.close()
        os.remove(db_path)

if __name__ == '__main__':
    unittest.main()


# In[ ]:




