# Udacitrivia!

### Description
This is the final project of Udacity's Full Stack Web Dev Nanodegree second 
course. The project is about a trivia game which have multiple categories that
you can choose from, some categories are: Sports, Entertainment, Arts, 
and more! You can do the following things in the app:

1. Display a list of questions - You can see all of them or see them based on a
specific category.
2. Search for questions you might be interested in.
3. Add questions your own questions to make the game more enjoyable!
4. Play the quiz game with random questions based on a selected category or
with all questions from all categories altogether!
5. Finally, you can also delete questions you don't like!

My job was to implement all the backend code for the Trivia 
API. 

The backend is built with Python utilizing the Flask micro framework.
The implementation includes basic error handling and testing with Python
unittests (All errors are formatted to be returned as JSON objects as 
well as the routes). It performs almost all CRUD operations (mentioned above)
except for update, and I planned and structured all routes following the
REST arquitectural style.
                                                            

### Code Style
The backend is built with Python utilizing the Flask micro framework and 
follows the PEP8 code style guidelines.


## Getting Started

### Local Development
The instructions below will guide you through the process of running the 
application locally on your machine.

#### Prerequisites

* The latest version of [Python](https://www.python.org/downloads/), 
[pip](https://pip.pypa.io/en/stable/getting-started/), 
[node](https://nodejs.org/en/), and [PostgreSQL](https://www.postgresql.org/)
should already be installed on your machine.
You can verify that you have these technologies installed on your machine by 
running the following commands:
    ``` py
    # For Python:
    > python --version
    
    # For pip:
    > pip --version
    
    # For Node:
    > node --version
    
    # For PostgreSQL:
    > postgres --version
    ```
    to verify that you have the latest versions of these technologies click on
    their respective links above.


* **Start a virtual environment** from the backend folder. If you don't know
how to start your own virtual environment, below are the instructions to do so:

    ``` py
    # Mac users
    python -m venv venv 
    source venv/bin/activate
    
    # Windows users on Git Bash, not CMD
    > py -m venv venv
    > venv/Scripts/activate
    ```

    If you're using the PyCharm IDE you can start a virtual environment following 
    these [instructions](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env).
    From the [PyCharm official docs](https://www.jetbrains.com/help/pycharm/quick-start-guide.html) website.


* **Install dependencies**. From the backend folder run:
    ```
    pip install -r requirements.txt
    ```

### Step 0: Start/Stop the PostgreSQL server.
Mac users can follow the command below:
``` 
pg_ctl -D /usr/local/var/postgres start
```
if you encounter a problem, run these commands:
```
pg_ctl -D /usr/local/var/postgres stop
pg_ctl -D /usr/local/var/postgres restart
```

Windows users can follow the commands below:
* Find the database directory, it could be something like this: 
`C:\Program File\PostgreSQL\13.3\data` the path depends on where you installed
postgres on your machine. If you can't find the directory, run this command:
    ```
    which postgres
    ```
    that command should output the path to where postgres is installed.
* Then, in the command line ([Git Bash](https://git-scm.com/downloads)),
execute the following command:
    ``` py
    # Start the server
    pg_ctl -D "C:\Program File\PostgreSQL\13.3\data" start
    ```
    if you encounter a problem with starting the server you can execute these
    other commands:
    ``` py
    # Stop the server
    pg_ctl -D "C:\Program File\PostgreSQL\13.3\data" stop
  
    # Restart the server
    pg_ctl -D "C:\Program File\PostgreSQL\13.3\data" restart
    ```
if it shows the *port already occupied* error, run:
``` py
sudo su -
ps -ef | grep postmaster | awk '{print $2}'
kill <PID>
```

### Step 1: Create and Populate the database
1. **Verification**

    Verify that the **database user** in the `/backend/models.py`, 
    `/backend/trivia.psql`, and `/backend/test_flaskr.py` (In case you want to
    run some tests or all of them).
2. **Create the database** 

   In your terminal, navigate to the `/backend` 
directory path and run the following commands:
   ``` py
   # Connect to PostgreSQL
   psql <your database username>
   
   # View all databases
   \l
   
   # Create the database
   \i setup.sql
   
   # Exit the PostgreSQL prompt
   \q
   ```
3. **Create tables** 

   Once your database is created, you can create tables and apply 
   constraints.
   
   ``` py
   # Mac & Windows users
   psql -f books.psql -U <Your database username> -d trivia
   
   # Linux users
   su - postgres bash -c "psql trivia < /path/to/backend/trivia.psql"
   ```

### Step 2: Start the backend server
From the `/backend` directory run:
``` py
# Mac users
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run

# Windows users on CMD
set FLASK_APP=flaskr
set FLASK_ENV=development
flask run
```
These commands put the application in development and directs our application to 
use the `__init__.py` file in our *flaskr* folder.

The application will run on `http://127.0.0.1:5000` by default and is set as
a proxy in the frontend configuration. 

#### Authentication
- The current version of the application does not require authentication or 
API keys.

### Step 3: Start the frontend
(You can start the frontend before the backend is up if you want) \
From the `/frontend` folder, run the following commands to start the client:
```
npm install // Only once to install dependencies
npm upgrade // To upgrade any outdated dependencies
npm start
```
By default, the frontend will run on `localhost:3000`. You can close the 
terminal if you wish to stop the frontend server.

### Runnning Tests
If any route needs testing, navigate to the `/backend` folder and
run the following commands:
```
psql trivia_test < trivia.psql
python test_flaskr.py
```
Also, make sure to change the database from `trivia` to `trivia_test` 
on this files `/backend/models.py` and `/backend/test_flaskr.py`.
