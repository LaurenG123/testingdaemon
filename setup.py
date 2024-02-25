from setuptools import setup

setup(
    name='test_daemon',
    version='0.1',
    packages=['test_daemon'],
    install_requires=[
        'pytest',
        # Add any other dependencies required for your test daemon
    ],
    entry_points={
        'console_scripts': [
            'test_daemon=test_daemon.daemon:run_tests_as_daemon',
        ],
    },
)

