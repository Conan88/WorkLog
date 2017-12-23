from setuptools import setup

setup(
    name='work',
    version='0.1',
    py_modules=['work'],
    install_requires=[
        'Click',
        'datetime',
    ],
    entry_points='''
        [console_scripts]
        work=work:work
    ''',
)
