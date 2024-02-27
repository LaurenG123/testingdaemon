import subprocess
import os
import pytest

def test_main_script():
    # Run the main shell script
    subprocess.run(['bash', 'main_script.sh'])

    # Check if output files are generated in the expected directory
    assert os.path.exists('output.csv')
    assert os.path.exists('log_file.log')

    # Check the content of the output files if necessary
    # Assert on CSV content or log content if needed

    # Clean up: remove generated files
    os.remove('output.csv')
    os.remove('log_file.log')
