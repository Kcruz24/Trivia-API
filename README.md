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

---
## API Reference

### Getting Started
* **Base URL**: At present this app can only be run locally and is not hosted
with a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration. 
* **Authentication**: This version of the application does not require authentication or API keys. 

### Error Handling
Errors are returned as JSON objects in the following format:
``` py
{
    "success": False, 
    "error": 404,
    "message": "Resource not found"
}
```
The API will return four error types when requests fail:
* `404: Resource Not Found`
* `422: Unprocessable Entity`
* `405: Method Not Allowed`
* `500: Internal Server Error`

### Endpoints
#### GET `/categories`

* General:
    * Returns a list of categories, total number of categories, and a success
    value.
* Sample: `curl http://localhost:5000/categories`
    ``` js
    {
      "all_categories": 6,
      "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
      },
      "success": true
    }
    ```

#### GET `/questions`

* General:
  * Returns a list of categories, a list of questions, current category,
  success value and total number of questions.
  * Results of questions are paginated in groups of 10. You must include a 
  request argument to choose page number, starting from 1. Here's an example:
  `curl http://localhost:5000/questions?page=2`
* Sample: `curl http://localhost:5000/questions`

    ``` js
    {
      "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
      },
      "current_category": null,
      "questions": [
        {
          "answer": "Apollo 13",
          "category": 5,
          "difficulty": 4,
          "id": 2,
          "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
          "answer": "Tom Cruise",
          "category": 5,
          "difficulty": 4,
          "id": 4,
          "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
          "answer": "Maya Angelou",
          "category": 4,
          "difficulty": 2,
          "id": 5,
          "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
          "answer": "Edward Scissorhands",
          "category": 5,
          "difficulty": 3,
          "id": 6,
          "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
          "answer": "Muhammad Ali",
          "category": 4,
          "difficulty": 1,
          "id": 9,
          "question": "What boxer's original name is Cassius Clay?"
        },
        {
          "answer": "Brazil",
          "category": 6,
          "difficulty": 3,
          "id": 10,
          "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
          "answer": "Uruguay",
          "category": 6,
          "difficulty": 4,
          "id": 11,
          "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
          "answer": "George Washington Carver",
          "category": 4,
          "difficulty": 2,
          "id": 12,
          "question": "Who invented Peanut Butter?"
        },
        {
          "answer": "Lake Victoria",
          "category": 3,
          "difficulty": 2,
          "id": 13,
          "question": "What is the largest lake in Africa?"
        },
        {
          "answer": "The Palace of Versailles",
          "category": 3,
          "difficulty": 3,
          "id": 14,
          "question": "In which royal palace would you find the Hall of Mirrors?"
        }
      ],
      "success": true,
      "total_questions": 19
    }
    ```

#### GET `/categories/<id>/questions`

* General:
  * Returns a list of questions based on the specified category id, 
  success value, current category and total number of questions.
* Sample: `curl http://localhost:5000/categories/2/questions`

    ``` js
    {
      "current_category": "Art",
      "questions": [
        {
          "answer": "Escher",
          "category": 2,
          "difficulty": 1,
          "id": 16,
          "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
        },
        {
          "answer": "Mona Lisa",
          "category": 2,
          "difficulty": 3,
          "id": 17,
          "question": "La Giaconda is better known as what?"
        },
        {
          "answer": "One",
          "category": 2,
          "difficulty": 4,
          "id": 18,
          "question": "How many paintings did Van Gogh sell in his lifetime?"
        },
        {
          "answer": "Jackson Pollock",
          "category": 2,
          "difficulty": 2,
          "id": 19,
          "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
        }
      ],
      "success": true,
      "total_questions": 4
    }
    ```

#### POST `/questions`

* General:
  * Creates a new questions using the submitted question, answer, difficulty and 
  category. 
  * Returns the id of the created question, success value, total questions, and
  the new list of questions with the newly added question.
* In order to see the newly added question the sample will include a request 
  argument with page #2.
* Sample: 
`curl http://localhost:5000/questions?page=2
-X POST 
-H "Content-Type: application/json" 
-d '{
      "question":"What color is the sky?", 
      "answer":"Blue", 
      "difficulty":1,
      "category":3
}'`

    ``` js
    {
      "created": 24,
      "questions": [
        {
          "answer": "Agra",
          "category": 3,
          "difficulty": 2,
          "id": 15,
          "question": "The Taj Mahal is located in which Indian city?"
        },
        {
          "answer": "Escher",
          "category": 2,
          "difficulty": 1,
          "id": 16,
          "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
        },
        {
          "answer": "Mona Lisa",
          "category": 2,
          "difficulty": 3,
          "id": 17,
          "question": "La Giaconda is better known as what?"
        },
        {
          "answer": "One",
          "category": 2,
          "difficulty": 4,
          "id": 18,
          "question": "How many paintings did Van Gogh sell in his lifetime?"
        },
        {
          "answer": "Jackson Pollock",
          "category": 2,
          "difficulty": 2,
          "id": 19,
          "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
        },
        {
          "answer": "The Liver",
          "category": 1,
          "difficulty": 4,
          "id": 20,
          "question": "What is the heaviest organ in the human body?"
        },
        {
          "answer": "Alexander Fleming",
          "category": 1,
          "difficulty": 3,
          "id": 21,
          "question": "Who discovered penicillin?"
        },
        {
          "answer": "Blood",
          "category": 1,
          "difficulty": 4,
          "id": 22,
          "question": "Hematology is a branch of medicine involving the study of what?"
        },
        {
          "answer": "Scarab",
          "category": 4,
          "difficulty": 4,
          "id": 23,
          "question": "Which dung beetle was worshipped by the ancient Egyptians?"
        },
        {
          "answer": "Blue",
          "category": 3,
          "difficulty": 1,
          "id": 24,
          "question": "What color is the sky?"
        }
      ],
      "success": true,
      "total_questions": 20
    }
    ```
  
#### POST `/questions`

* General:
  * Returns a list of questions based on a search term, a success value, the 
  total number of questions, and the search term.
* Sample: 
`curl http://localhost:5000/questions 
-X POST 
-H "Content-Type: application/json" 
-d '{"searchTerm": "title"}'`

    ``` js
    {
      "questions": [
        {
          "answer": "Maya Angelou",
          "category": 4,
          "difficulty": 2,
          "id": 5,
          "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
          "answer": "Edward Scissorhands",
          "category": 5,
          "difficulty": 3,
          "id": 6,
          "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }
      ],
      "searchTerm": "title",
      "success": true,
      "total_questions": 2
    }
    ```

#### POST `/quizzes`

* General:
  * Takes category and previous questions parameters.
  * Returns a random question based on the given category and a success value.
* Sample: 
`curl http://localhost:5000/quizzes
-X POST 
-H "Content-Type: application/json" 
-d '{
      "quiz_category": {"type": "History", "id": 4},
      "previous_questions": []
}'`

    ``` js
    {
      "question": {
        "answer": "Scarab",
        "category": 4,
        "difficulty": 4,
        "id": 23,
        "question": "Which dung beetle was worshipped by the ancient Egyptians?"
      },
      "success": true
    }
    ```
  
#### DELETE `/questions/<id>`

* General:
  * Deletes the question of the given ID if it exists.
  * Returns the id of the deleted question, a success value, list of question
  updated, and total number of questions updated.
* Sample: `curl http://localhost:5000/questions/25 -X DELETE`

    ``` js
    {
      "deleted": 25,
      "questions": [
        {
          "answer": "Apollo 13",
          "category": 5,
          "difficulty": 4,
          "id": 2,
          "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
          "answer": "Tom Cruise",
          "category": 5,
          "difficulty": 4,
          "id": 4,
          "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
          "answer": "Maya Angelou",
          "category": 4,
          "difficulty": 2,
          "id": 5,
          "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
          "answer": "Edward Scissorhands",
          "category": 5,
          "difficulty": 3,
          "id": 6,
          "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
          "answer": "Muhammad Ali",
          "category": 4,
          "difficulty": 1,
          "id": 9,
          "question": "What boxer's original name is Cassius Clay?"
        },
        {
          "answer": "Brazil",
          "category": 6,
          "difficulty": 3,
          "id": 10,
          "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
          "answer": "Uruguay",
          "category": 6,
          "difficulty": 4,
          "id": 11,
          "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
          "answer": "George Washington Carver",
          "category": 4,
          "difficulty": 2,
          "id": 12,
          "question": "Who invented Peanut Butter?"
        },
        {
          "answer": "Lake Victoria",
          "category": 3,
          "difficulty": 2,
          "id": 13,
          "question": "What is the largest lake in Africa?"
        },
        {
          "answer": "The Palace of Versailles",
          "category": 3,
          "difficulty": 3,
          "id": 14,
          "question": "In which royal palace would you find the Hall of Mirrors?"
        }
      ],
      "success": true,
      "total_questions": 19
    }
    
    ```