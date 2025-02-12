from setuptools import setup, find_packages

setup(
    name="example_python_project",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    isntall_requires=[
        "python-dotenv",
        "Flask",
        "Django",
        "djangorestframework",
    ],
    entry_points={
        'console_scripts': [
            'run=example_python_project.main:main',
        ],
    },
)