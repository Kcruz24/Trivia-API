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

        self.quiz_question = {
            'previous_questions': [2, 4, 10, 12],
            'quiz_category': 'Art',
            'question': self.new_question
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

    def test_404_if_get_questions_does_not_exist(self):
        res = self.client().get('/question')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    # /////////////// TEST DELETE QUESTION ///////////////
    # def test_delete_question(self):
    #     QUESTION_ID = 13
    #
    #     res = self.client().delete(f'/questions/{QUESTION_ID}')
    #     data = json.loads(res.data)
    #
    #     question = Question.query \
    #         .filter(Question.id == QUESTION_ID) \
    #         .one_or_none()
    #
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['deleted'])
    #     self.assertTrue(len(data['questions']))
    #     self.assertTrue(data['total_questions'])
    #     self.assertEqual(question, None)

    def test_422_delete_if_question_does_not_exist(self):
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable Entity')

    # /////////////// TEST CREATE QUESTION ///////////////
    def test_create_new_question(self):
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['created'], 26)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])

    def test_405_if_create_question_not_allowed(self):
        res = self.client().post('/questions/321', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed')

    # /////////////// TEST SEARCH QUESTION ///////////////
    def test_search_questions(self):
        res = self.client().post('/questions', json={'searchTerm': 'actor'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])

    def test_if_searchTerm_does_not_exist(self):
        res = self.client().post('/questions', json={'searchTerm': 'title'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['questions'], [])
        self.assertEqual(len(data['questions']), 0)

    # /////////// TEST GET QUESTION BASED ON CATEGORY ////////////
    def test_get_questions_based_on_category(self):
        res = self.client().get('/categories/2/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        self.assertEqual(data['current_category'], 'Art')

    def test_404_if_category_not_found(self):
        res = self.client().get('/categories/9/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    # /////////// TEST GET QUESTION TO PLAY QUIZ ////////////
    def test_play_quiz(self):
        res = self.client().post('/quizzes', json={
            "quiz_category": {"type": "History", "id": 4},
            "previous_questions": [],
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['question']))

    def test_422_if_play_quiz_not_params_correct(self):
        res = self.client().post('/quizzes', json=self.quiz_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable Entity')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
