const axios = require('axios');

class MessagerService {
    constructor(){
        this.URI = 'http://localhost:5000/messager';
    }

    getMessages(user) {
        console.log(user.username)
        return axios.get(this.URI + '/' + user.username, {withCredentials: true})
    }

    sendMessage(newMsg) {
        console.log(newMsg)
        return axios.post(this.URI , newMsg, {withCredentials: true}).then(res => {
            console.log(res.data)
        })
    }


}

export default MessagerService;