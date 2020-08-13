const axios = require('axios');

class AssignmentService {
    constructor(){
        this.URI = 'http://localhost:5000/assignments';
    }



    getAssignments() {
        return axios.get(this.URI, {withCredentials: true})
    }

    teacher_assign_work(the_assignment) {
        console.log(the_assignment)
        return axios.post(this.URI , the_assignment, {withCredentials: true}).then(res => {
            console.log(res.data)
        })
    }


}

export default AssignmentService;