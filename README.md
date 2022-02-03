# Introduction
This is the 9th project for the Python path of Openclassrooms. The goal is to Develop a Web Application Using Django.
The primary use-cases for the app are two-fold:
1. People asking for reviews on a particular book or article.
2. People looking for interesting articles and books to read based on others reviews.


# Required Setup to run the program:

1. Python version 3.9.5 or higher must be installed.
2. Create the directory in which you want to keep the program.
3. Open your terminal.
4. Navigate to the folder that contains the `manage.py` and `requirements.txt` files
5. Create your Virtual Environment by running the command: `python -m venv venv`
6. Activate the Environment by running: 
 `venv\Scripts\activate.bat` (Windows) 
 or `venv\Scripts\activate.ps1` (Powershell)
 or `source venv/bin/activate` (OS)
7. Install the Requirements by running the command: `pip install -r requirements.txt`
   
# How to run the program:
1. Open your terminal
2. Navigate to the directory that contains the `manage.py` file
3. Activate the environment by running: 
 `venv\Scripts\activate.bat` (Windows) 
 or `venv\Scripts\activate.ps1` (Powershell)
 or `source venv/bin/activate` (OS)
4. Run the command: `python manage.py create_db` (Windows) or `python3 manage.py create_db`(Mac)
5. Run the command: `python manage.py runserver` (Windows) or `python3 manage.py runserver`(Mac)
The default port is 8000. Add the port-number as a parameter to runserver to use a different
port to run the server. For Example: `python manage.py runserver 9000`

When the server is running after step 5 of the procedure, the LITReview-Website can be 
accessed with your browser by pasting the URL: `http://127.0.0.1:8000/` 
or copy and paste the URL that is displayed in the Terminal.

Steps 1-4 are only required for initial installation. For subsequent launches,
you only have to execute step 5 from the root folder of the project.

## Technologies
- Python version 3.9.5
- Django version 4.0.1