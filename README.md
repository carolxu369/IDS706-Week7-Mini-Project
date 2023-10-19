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
   git clone [URL]
2. Navigate to the tool's directory:  
   cd my_tool
3. Install the tool:  
   pip install .
4. Initializing the Database:  
   mytool init
5. Adding Data to the Database:  
   mytool add "Some data content here."
6. Viewing All Data:  
   mytool view
