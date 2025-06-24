from setuptools import setup

setup(
    name='alkis-sampler',
    version='0.1.0',
    py_modules=['alkis_sampler'],
    install_requires=[
        'geopandas',
        'fiona'
    ],
    entry_points={
        'console_scripts': [
            'alkis-sampler=alkis_sampler:main',
        ],
    },
)
