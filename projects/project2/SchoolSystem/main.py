'''Starts and operates the back-end of our application'''

import json
from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from SchoolSystem.data.logger import get_logger
from SchoolSystem.users.model import User, UserEncoder
from SchoolSystem.assignments.model import AssignmentEncoder
from SchoolSystem.submissions.model import SubmissionEncoder
from SchoolSystem.updates.model import UpdateEncoder
from SchoolSystem.schedules.model import ScheduleEncoder
from SchoolSystem.data.msgrModel import MessagerEncoder
import SchoolSystem.data.mongo as db

_log = get_logger(__name__)

app = Flask(__name__)
_log.debug(app)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
app.json_encoder = UserEncoder


@app.route('/assignments', methods=['GET'])
def assignments():
    '''Gets all assignments'''
    users = db.get_assignments()
    value = bytes(json.dumps(users, cls=AssignmentEncoder), 'utf-8')
    return value, 200

@app.route('/assignments', methods=['POST'])
def insert_assignment():
    '''Creates new assignment'''
    assignment = db.insert_assignment(request.json)
    _log.debug(assignment)
    value = bytes(json.dumps(assignment, cls=AssignmentEncoder), 'utf-8')
    if assignment:
        return value, 200
    return null, 401

@app.route('/teachers', methods=['GET'])
def teachers():
    '''Gets all teachers'''
    users = db.get_teachers()
    value = bytes(json.dumps(users, cls=UserEncoder), 'utf-8')
    return value, 200

@app.route('/students', methods=['GET'])
def students():
    '''Gets all students'''
    users = db.get_students()
    value = bytes(json.dumps(users, cls=UserEncoder), 'utf-8')
    return value, 200

@app.route('/students/<username>', methods=['PUT', 'POST', 'DELETE', 'GET'])
def student_update(username):
    '''All routes for a specific student'''
    if request.method == 'PUT':
        _log.info(username)
        user = db.update_student(username)
        _log.info(user.to_dict())
        return user.to_dict(), 200
    elif request.method == 'POST':
        _log.info(username)
        db.submit_student_update(username, request.json)
        return {}, 200
    elif request.method == 'DELETE':
        _log.info(username)
        db.delete_update(username)
        return {}, 200
    elif request.method == 'GET':
        users = db.get_requirements(username)
        value = bytes(json.dumps(users, cls=UserEncoder), 'utf-8')
        return value, 200
    else:
        empty = make_response({})
        return empty, 204

@app.route('/students/<username>/schedule', methods=['PUT', 'POST', 'DELETE'])
def schedule_update(username):
    '''All routes for scheduling classes'''
    if request.method == 'PUT':
        _log.info(username)
        user = db.update_schedule(username)
        _log.info(user.to_dict())
        return user.to_dict(), 200
    elif request.method == 'POST':
        _log.info(username)
        db.sumbit_schedule_update(username, request.json)
        return {}, 200
    elif request.method == 'DELETE':
        _log.info(username)
        db.delete_schedule_update(username)
        return {}, 200

@app.route('/teachers/<username>', methods=['PUT'])
def user_update(username):
    '''Updates a specific user'''
    _log.info(username)
    db.update_user(username, request.json)
    return {}, 200

@app.route('/users/<username>', methods=['PUT'])
def assign_teacher(username):
    '''Assigns a teacher to a student'''
    _log.info(username)
    db.assign_teacher(username, request.json)
    return {}, 200

@app.route('/submissions/<homework>', methods=['PUT'])
def grade(homework):
    '''Route for grading homework'''
    _log.info(type(homework))
    _log.info(request.json)
    db.grade_homework(int(homework), request.json)
    return {}

@app.route('/submissions', methods=['POST'])
def submit():
    '''Creates a new submission'''
    db.add_submission(request.json)
    return {}

@app.route('/submissions/<username>', methods=['GET'])
def assignments_by_teacher(username):
    '''Finds all assignments per teacher'''
    users = db.get_submissions(username)
    value = bytes(json.dumps(users, cls=SubmissionEncoder), 'utf-8')
    return value, 200


@app.route('/users', methods={'GET', 'POST', 'DELETE', 'PUT'})
def login():
    '''The login functionality'''
    if request.method == 'POST':
        _log.debug("In POST")
        # getting the user information from the form and getting the information from the db
        _log.debug(request.json['username'])
        temp = request.json['username']
        _log.debug(temp)
        user = db.login(temp)
        _log.debug(user)
        _log.debug(request.json)
        _log.debug(user.password)
        _log.debug(request.json['password'])
        if user.password == request.json['password']:
            # Generate our token
            auth_token = user.encode_auth_token()
            _log.debug(dir(auth_token))
            response = make_response(jsonify(user))
            response.set_cookie('authorization', auth_token.decode())
            return response, 200
        return {}, 401
    elif request.method == 'PUT':
        user = db.add_user(request.json)
        value = bytes(json.dumps(user, cls=SubmissionEncoder), 'utf-8')
        return value, 200
    elif request.method == 'GET':
        auth_token = request.cookies.get('authorization')
        if auth_token:
            _log.debug(auth_token)
            _log.debug(User.decode_auth_token(auth_token))
            return jsonify(db.get_user_by_id(User.decode_auth_token(auth_token))), 200
        else:
            return {}, 401
    else:
        empty = make_response({})
        empty.set_cookie('authorization', '')
        return empty, 204

@app.route('/admin', methods={'GET', 'POST', 'PUT', 'DELETE'})
def get_users():
    '''Gets all users'''
    if request.method == 'GET':
        users = db.get_users()
        value = bytes(json.dumps(users, cls=UserEncoder), 'utf-8')
        return value, 200

@app.route('/admin/<fullname>', methods=['DELETE'])
def user_remove(fullname):
    '''Deletes a user'''
    _log.info(request.json)
    db.remove_user(fullname)
    return {}, 200

@app.route('/admin/<username>', methods=['PUT'])
def edit_admin(username):
    '''Allows admin to edit their own information'''
    _log.info(username)
    _log.info(request.json)
    db.edit_admin(username, request.json)
    return {}, 200

@app.route('/admin/updates', methods={'GET'})
def get_updates():
    '''Finds all updates'''
    updates = db.get_updates()
    value = bytes(json.dumps(updates, cls=UpdateEncoder), 'utf-8')
    _log.info(value)
    return value, 200

@app.route('/admin/schedules', methods={'GET'})
def get_schedules():
    '''Finds all schedules'''
    schedules = db.get_schedules()
    value = bytes(json.dumps(schedules, cls=ScheduleEncoder), 'utf-8')
    _log.info(value)
    return value

@app.route('/messager/<user>', methods={'GET'})
def get_messages(user):
    '''Finds all messages'''
    msgs = db.get_msgs(user)
    value = bytes(json.dumps(msgs, cls=MessagerEncoder), 'utf-8')
    _log.info(value)
    _log.debug(msgs)
    return value, 200

@app.route('/messager', methods={'POST'})
def new_message():
    '''Creates a new message'''
    _log.debug(request.json)
    new_message = db.new_msg(request.json)
    value = bytes(json.dumps(new_message, cls=MessagerEncoder), 'utf-8')
    return value, 200
