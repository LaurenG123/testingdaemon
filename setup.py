# setup.py
from setuptools import setup

setup(
    name='pytest_daemon',
    version='0.1',
    packages=['pytest_daemon'],
    entry_points={
        'console_scripts': [
            'pytest_daemon=pytest_daemon.daemon:main',
        ],
    },
)
