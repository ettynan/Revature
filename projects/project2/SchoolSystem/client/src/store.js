import { createStore } from 'redux';

const initialState = {
    user: null,
    grades: [],
    schedule: {},
    username: '',
    password: '',
    user_array: [],
    student_array: [],
    teacher_array: [],
    assignment_array: [],
    submission_array: [],
    update_array: [],
    schedule_array: [],
    new_admin: {},
    new_student: {},
    new_teacher: {},
    student: [],
    messages: [],
    msgNum: 0
};

function schoolReducer(state = initialState, action) {
    console.log(state);
    switch(action.type) {
        case 'login':
            return Object.assign({}, state, {username: ''}, {user: action.user}, {password: ''})
        case 'logout':
            return Object.assign({}, state, {username: ''}, {user: action.user}, {password: ''})
        case 'showGrades':
            return Object.assign({}, state, {grades: action.grades})
        case 'handleUsername':
            return Object.assign({}, state, {username: action.username})
        case 'handlePassword':
            return Object.assign({}, state, {password: action.password})
        case 'remove':
            return Object.assign({}, state)
        case 'editAdmin':
            return Object.assign({}, state)
        case 'getUsers':
            return Object.assign({}, state, {user_array: action.user_array})
        case 'getStudents':
            return Object.assign({}, state, {student_array: action.student_array})
        case 'getTeachers':
            return Object.assign({}, state, {teacher_array: action.teacher_array})
        case 'getAssignments':
            return Object.assign({}, state, {assignment_array: action.assignment_array})
        case 'getSubmissions':
            return Object.assign({}, state, {submission_array: action.submission_array})
        case 'getUpdates':
            return Object.assign({}, state, {update_array: action.update_array})
        case 'getRequirements':
            return Object.assign({}, state, {student: action.student})
        case 'getSchedules':
            return Object.assign({}, state, {schedule_array: action.schedule_array})
        case 'getSchedule':
            return Object.assign({}, state, {schedule: action.schedule})
        case 'toggleAssignHW':
            return Object.assign({}, state, {isAssigning: action.isAssigning})
        case 'setMsgNum':
            return Object.assign({}, state, {msgNum: action.msgNum})
        case 'getMsgs':
            return Object.assign({}, state, {messages: action.messages})
        default:
            return state;
    }
}
const store = createStore(schoolReducer);

export default store