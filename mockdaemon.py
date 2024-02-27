import subprocess
import time
import sys
import os
import daemon

# Mock paths and data
MOCK_MAIN_SCRIPT_PATH = '/path/to/mock_main_script.sh'
MOCK_LOG_FILE_PATH = '/path/to/mock_log_file.log'

def run_main_script():
    # For testing purposes, we'll just print a message instead of running the actual script
    print("Running main script:", MOCK_MAIN_SCRIPT_PATH)

def run_tests():
    # For testing purposes, we'll print a message indicating that tests are running
    print("Running tests")

def main():
    # Change working directory to the directory of your script
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    # Check if running in test mode
    if '--test' in sys.argv:
        run_tests()
        return

    # Run the main script initially
    run_main_script()

    # Main loop: Run the main script every 60 seconds
    while True:
        run_main_script()
        time.sleep(60)

if __name__ == "__main__":
    # Start the daemon context
    with daemon.DaemonContext():
        main()

