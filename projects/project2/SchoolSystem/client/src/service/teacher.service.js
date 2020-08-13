const axios = require('axios');

class TeacherService {
    constructor(){
        this.URI = 'http://localhost:5000/teachers';
    }

    getTeachers() {
        return axios.get(this.URI, {withCredentials: true})
    }

    updateTeacherProfile(name, newProfile) {
        return axios.put(this.URI + '/' + name, newProfile, {withCredentials: true})
    }

}

export default TeacherService;