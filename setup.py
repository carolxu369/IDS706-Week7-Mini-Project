from setuptools import setup, find_packages

setup(
    name="my_tool",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        #"sqlite3"
    ],
    entry_points={
        "console_scripts": [
            "mytool = my_tool.main:main"
        ]
    }
)