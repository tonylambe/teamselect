from setuptools import setup

setup(
    name='teamselect',
    version='0.1',
    py_modules=['teamselect'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        teamselect=teamselect:cli
    ''',
)
