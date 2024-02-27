# hihih.py

import subprocess
import time
import sys
import os


MAIN_SCRIPT_PATH = '../main_script.sh'
def run_main_script():
    subprocess.run(['bash', MAIN_SCRIPT_PATH])

def run_tests():
    subprocess.run(['pytest', 'tests.py'])

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
    # Daemonize the process
    if os.fork():
        sys.exit(0)

    # Decouple from parent environment
    os.chdir('/')
    os.umask(0)
    os.setsid()

    # Redirect standard file descriptors
    sys.stdout.flush()
    sys.stderr.flush()
    si = open(os.devnull, 'r')
    so = open('daemon.log', 'a+')
    se = open('daemon.log', 'a+', 0)
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())

    # Start the main function
    main()
