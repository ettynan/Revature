const axios = require('axios');

class SubmissionService {
    constructor(){
        this.URI = 'http://localhost:5000/submissions';
    }
    newSubmission(student, assignment, content) {
        return axios.post(this.URI, {'student': student, 'assignment': assignment,
                                     'teacher': "this teacher", 'grade': '',
                                     'content': content}, {withCredentials: true})

    }
    getSubmissions(username) {
        return axios.get(this.URI + '/' + username, {withCredentials: true})
    }

    grade(id, letter) {
        return axios.put(this.URI + '/' + id, {'grade': letter}, {withCredentials: true})

    }




}

export default SubmissionService;