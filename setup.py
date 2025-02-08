from setuptools import setup, find_packages

setup(
    name="JobVerifier",
    version="1.0.0",
    description="A desktop app that verifies job postings for authenticity",
    author="Aaron Wechsler",
    author_email="wechsleraaron@gmail.com",
    packages=find_packages(),
    install_requires=[
        "PyQt5",
        "requests",
        "pyinstaller"
    ],
    entry_points={
        "console_scripts": [
            "jobverifier = main:main"
        ]
    }
)
