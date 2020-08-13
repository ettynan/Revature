const axios = require('axios');

class AdminService {
    constructor(){
        this.URI = 'http://localhost:5000/admin';
    }

    getUsers() {
        return axios.get(this.URI, {withCredentials: true})
    }

    getUpdates() {
        return axios.get(this.URI + '/updates', {withCredentials: true})
    }

    getSchedules() {
        return axios.get(this.URI + '/schedules', {withCredentials: true})
    }

    remove(name) {
        return axios.delete(this.URI + '/' + name, {withCredentials: true})
    }

    editAdmin(person, username, password, fullName, address) {
        return axios.put(this.URI + '/' + person, {'username': username,
                        'password': password, 'fullname': fullName,
                        'address': address, 'role': 'admin'}, {withCredentials: true})
    }
}

export default AdminService;