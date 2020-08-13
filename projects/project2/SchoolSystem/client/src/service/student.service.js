const axios = require('axios');

class StudentService {
    constructor(){
        this.URI = 'http://localhost:5000/students';
    }

    assign(name, teacherName) {
        return axios.put(this.URI + '/' + name, {'teacher': teacherName}, {withCredentials: true})

    }

    getStudents() {
        return axios.get(this.URI, {withCredentials: true})
    }

    getRequirements(name) {
        return axios.get(this.URI + '/' + name)
    }

    updateProfile(name) {
        return axios.put(this.URI + '/' + name, {withCredentials: true})
    }

    denyProfileUpdate(name) {
        return axios.delete(this.URI + '/' + name, {withCredentials: true})
    }

    submitProfileUpdate(name, profileUpdate) {
        return axios.post(this.URI + '/' + name, profileUpdate, {withCredentials: true})
    }

    updateSchedule(name) {
        return axios.put(this.URI + '/' + name + '/schedule', {withCredentials: true})
    }

    denyScheduleUpdate(name) {
        return axios.delete(this.URI + '/' + name + '/schedule', {withCredentials: true})
    }

    submitScheduleUpdate(name, scheduleUpdate) {
        return axios.post(this.URI + '/' + name + '/schedule', scheduleUpdate, {withCredentials: true})
    }

}

export default StudentService;