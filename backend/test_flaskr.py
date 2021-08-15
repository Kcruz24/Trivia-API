import json
import unittest

from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}:{}@{}/{}" \
            .format('postgres',
                    'Dariel24',
                    'localhost:5432',
                    self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {
            'question': 'What is my gaming nickname?',
            'answer': 'Kakin Blu',
            'category': 5,
            'difficulty': 3
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    #
    # TODO: Write at least one test for each test for successful operation
    #       and for expected errors.

    # /////////////// TEST GET CATEGORIES ///////////////
    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['all_categories'])
        self.assertTrue(len(data['categories']))

    def test_404_categories(self):
        res = self.client().get('/categorie')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    # /////////////// TEST GET QUESTIONS ///////////////
    def test_get_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['current_category'], None)
        self.assertTrue(len(data['questions']))
        self.assertTrue(len(data['categories']))
        self.assertTrue(data['total_questions'])

    def test_404_get_questions(self):
        res = self.client().get('/question')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    # /////////////// TEST DELETE QUESTION ///////////////
    def test_delete_question(self):
        QUESTION_ID = 13

        res = self.client().delete(f'/questions/{QUESTION_ID}')
        data = json.loads(res.data)

        question = Question.query \
            .filter(Question.id == QUESTION_ID) \
            .one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        self.assertEqual(question, None)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
