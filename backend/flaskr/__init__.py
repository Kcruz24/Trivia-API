import random

from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_questions(req, questions):
    page = req.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    formatted_questions = [question.format() for question in questions]
    current_questions = formatted_questions[start:end]

    return current_questions


def format_categories(categories):
    return {cat.id: cat.type for cat in categories}


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    #
    # @TODO: Set up CORS. Allow '*' for origins.
    #        Delete the sample route after completing the TODOs (DONE)
    CORS(app, resources={r"*": {"origins": "*"}})

    # @TODO: Use the after_request decorator to set Access-Control-Allow (DONE)
    @app.after_request
    def after_request(res):
        res.headers.add("Access-Control-Allow-Headers",
                        "Content-Type, authorization, true")

        res.headers.add("Access-Control-Allow-Methods",
                        'GET, POST, PATCH, DELETE, OPTIONS')

        return res

    # @TODO: Create an endpoint to handle GET requests for all available
    #        categories. (DONE)
    @app.route('/categories')
    def get_categories():
        categories = Category.query.order_by(Category.id).all()

        if len(categories) == 0:
            abort(404)

        formatted_categories = format_categories(categories)

        return jsonify({
            'success': True,
            'categories': formatted_categories,
            'all_categories': len(categories)
        })

    # @TODO: Create an endpoint to handle GET requests for questions, including
    #        pagination (every 10 questions).
    #        This endpoint should return a list of questions,
    #        number of total questions, current category, categories.
    #        (DONE)
    @app.route('/questions')
    def get_questions():
        questions = Question.query.order_by(Question.id).all()

        if len(questions) == 0:
            abort(404)

        categories = Category.query.order_by(Category.id).all()
        current_questions = paginate_questions(request, questions)
        formatted_categories = format_categories(categories)

        return jsonify({
            'success': True,
            'total_questions': len(questions),
            'questions': current_questions,
            'categories': formatted_categories,
            'current_category': None
        })

    # TEST: At this point, when you start the application
    # you should see questions and categories generated,
    # ten questions per page and pagination at the bottom of the
    # screen for three pages. Clicking on the page numbers should update
    # the questions.

    # @TODO: Create an endpoint to DELETE question using a question ID. (DONE)
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.get_or_404(question_id)
            question_id = question.id
            question.delete()

            questions = Question.query.order_by(Question.id).all()
            formatted_questions = paginate_questions(request, questions)

            return jsonify({
                'success': True,
                'deleted': question_id,
                'questions': formatted_questions,
                'total_questions': len(questions)
            })
        except:
            abort(422)

    # TEST: When you click the trash icon next to a question, the question will
    #       be removed. This removal will persist in the database and
    #       when you refresh the page.

    # @TODO: Create an endpoint to POST a new question,
    #        which will require the question and answer text,
    #        category, and difficulty score.
    @app.route('/questions', methods=['POST'])
    def create_question():
        body = request.get_json()

        get_question = body.get('question', None)
        get_answer = body.get('answer', None)
        get_difficulty = body.get('difficulty', None)
        get_category = body.get('category', None)
        search = body.get('searchTerm', None)

        try:
            if search:
                questions = Question.query.order_by(Question.id) \
                    .filter(Question.question.ilike(f'%{search}%')) \
                    .all()
                current_questions = paginate_questions(request, questions)

                return jsonify({
                    'success': True,
                    'questions': current_questions,
                    'total_questions': len(questions)
                })

            else:
                new_question = Question(question=get_question,
                                        answer=get_answer,
                                        category=get_category,
                                        difficulty=get_difficulty)
                new_question.insert()

                questions = Question.query.order_by(Question.id).all()
                current_questions = paginate_questions(request, questions)

                return jsonify({
                    'success': True,
                    'created': new_question.id,
                    'questions': current_questions,
                    'total_questions': len(questions)
                })

        except():
            abort(422)

    # TEST: When you submit a question on the "Add" tab,
    # the form will clear and the question will appear at the end of the last
    # page of the questions list in the "List" tab.

    # @TODO: Create a POST endpoint to get questions based on a search term.
    #        It should return any questions for whom the search term
    #        is a substring of the question. (DONE)

    # TEST: Search by any phrase. The questions list will update to include
    # only question that include that string within their question.
    # Try using the word "title" to start.

    # @TODO: Create a GET endpoint to get questions based on category. (DONE)
    @app.route('/categories/<int:category_id>/questions')
    def test_get_questions_based_on_category(category_id):
        questions = Question.query \
            .order_by(Question.id) \
            .filter(Question.category == category_id) \
            .all()

        if len(questions) == 0:
            abort(404)

        current_questions = paginate_questions(request, questions)
        current_category = Category.query.get(category_id).type

        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(questions),
            'current_category': current_category
        })

    # TEST: In the "List" tab / main screen, clicking on one of the
    # categories in the left column will cause only questions of that
    # category to be shown.

    # @TODO: Create a POST endpoint to get questions to play the quiz.
    #        This endpoint should take category and previous question parameters
    #        and return a random questions within the given category,
    #        if provided, and that is not one of the previous questions.

    # TEST: In the "Play" tab, after a user selects "All" or a category,
    # one question at a time is displayed, the user is allowed to answer
    # and shown whether they were correct or not.

    # @TODO: Create error handlers for all expected errors
    #        including 404 and 422. (DONE)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resource not found'
        }), 404

    @app.errorhandler(422)
    def unprocessable_entity(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Unprocessable Entity'
        }), 422

    @app.errorhandler(405)
    def unprocessable_entity(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Method Not Allowed'
        }), 405

    return app
