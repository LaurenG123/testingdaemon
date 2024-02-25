import pytest
import csv

def compare_csv_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        reader1 = csv.reader(f1)
        reader2 = csv.reader(f2)
        for row1, row2 in zip(reader1, reader2):
            assert row1 == row2

@pytest.mark.parametrize("file1, file2", [("file1.csv", "file2.csv")])
def test_compare_csv_files(file1, file2):
    compare_csv_files(file1, file2)
