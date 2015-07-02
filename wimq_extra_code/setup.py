from setuptools import setup

setup(
    entry_points={
        'wimq.application': [
            'main = asleep.main:main'
        ]
    }
)
