# IDS706-Week7-Mini-Project: Package a Python Script into a Command-Line Tool

This is a Python GitHub Template Repository that includes the following contents:
- A .devcontainer configuration for a Python environment
- A Makefile with commands for setup, testing, and linting
- GitHub Actions for CI/CD
- A requirements.txt for project dependencies
- A Python script with setuptools or a similar tool
- A user guide on how to install and use the tool
- Communication with an external or internal database
  
## Prerequisites

- sqlite3

## User Guide

This tool provides a simple command-line interface to interact with an SQLite database.  
1. Clone the GitHub repository:  
   git clone [https://github.com/carolxu369/IDS706-Week7-Mini-Project.git]
2. Install the tool:  
   pip install .
3. Initializing the Database:  
   mytool init
4. Adding Data to the Database:  
   mytool add "Some data content here."
5. Viewing All Data:  
   mytool view  
  
After testing with the following prompts:  
  
mytool add "Sample text entry 1"  
mytool add "Database testing content"  
mytool add "Test data"  

Run mytool view should have the following:  
(1, 'Sample text entry 1')  
(2, 'Database testing content')  
(3, 'Test data')  
