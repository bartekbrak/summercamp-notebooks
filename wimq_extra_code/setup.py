from setuptools import setup

setup(
    name='sample_project',
    packages=['project'],
    entry_points={
        'wimq.application': [
            'main = project.main:main'
        ]
    }
)
