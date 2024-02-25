
import pytest
from sqlalchemy import create_engine, MetaData, Table, select
import csv

def compare_sql_with_csv(sql_url, table_name, csv_file):
    engine = create_engine(sql_url)
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table = Table(table_name, metadata, autoload=True, autoload_with=engine)

    with engine.connect() as conn:
        query = select([table])
        sql_result = conn.execute(query).fetchall()

    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        csv_result = list(reader)

    assert sql_result == csv_result

@pytest.mark.parametrize("sql_url, table_name, csv_file", [("sqlite:///data.db", "table1", "file1.csv")])
def test_compare_sql_with_csv(sql_url, table_name, csv_file):
    compare_sql_with_csv(sql_url, table_name, csv_file)
