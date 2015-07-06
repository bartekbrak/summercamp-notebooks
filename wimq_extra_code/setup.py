from setuptools import setup

setup(
    name='sample_project',
    version='0.1.0',
    packages=['project'],
    entry_points={
        'wimq.application': [
            'main = project.main:main'
        ]
    }
)
