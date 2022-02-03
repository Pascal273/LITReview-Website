# Introduction
This is the 9th project for the Python path of Openclassrooms. The goal is to Develop a Web Application Using Django.
The primary use-cases for the app are two-fold:
1. People asking for reviews on a particular book or article.
2. People looking for interesting articles and books to read based on others reviews.


# Required Setup to run the program:

1. Python version 3.9.5 or higher must be installed.
2. Create the directory in which you want to keep the program.
3. Open your terminal.
4. Navigate to the folder with the "LITReview" -folder and requirements.txt in it
5. Create your Virtual Environment by running the command: `python -m venv .venv`
6. Activate the Environment by running: 
 `.venv\Scripts\activate.bat` (Windows) 
 or `.venv\Scripts\activate.ps1` (Powershell)
 or `source .venv/bin/activate` (OS)
7. Install the Requirements by running the command: `pip install -r requirements.txt`
   
# How to run the program:
1. Open your terminal
2. Navigate to the directory that contains the "chess_club_app" folder
3. Activate the environment by running: 
 `.venv\Scripts\activate.bat` (Windows) 
 or `.venv\Scripts\activate.ps1` (Powershell)
 or `source .venv/bin/activate` (OS)
4. Run the command: `python -m chess_club_app`

# How to create a Flake8 html report:
1. Open your terminal
2. Navigate to the directory that contains the "chess_club_app" folder
3. Activate the environment by running: 
 `.venv\Scripts\activate.bat` (Windows) 
 or `.venv\Scripts\activate.ps1` (Powershell)   
 or `source .venv/bin/activate` (OS)
4. Run the command: `flake8 --format=html --htmldir=flake-report`
   
## Notes
- The program will create a database folder and file automatically
- The folder and files for the flake8 report will be created automatically

## Technologies
- Python version 3.9.5
- TinyDB version 4.5.1
- Flake8 version 4.0.1