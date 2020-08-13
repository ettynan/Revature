import React, { Component } from "react";
import AdminService from '../../service/admin.service';
import MessagerService from '../../service/messager.service';

import { connect } from 'react-redux';

class MsgBody extends Component {
    constructor(props){
        super(props);
        this.message = React.createRef();
        this.toMessage = React.createRef();
      };
      adminService = new AdminService();
      messagerService = new MessagerService();
  state = {
  };

  componentDidMount(){
    this.adminService.getUsers().then(res => {
      console.log(res.data)
      this.props.dispatch({type: 'getUsers', user_array: res.data})
    })
  }

  to_msg = (event) => {
    console.log(event.target.id)
    this.props.dispatch({type: 'setMsgNum', msgNum: event.target.id})
  }

  msgSend = () => {
    let newMsg = {
      "_id": -1,
      "msg_msg": this.message.current.value,
      "msg_to": this.toMessage.current.value,
      "msg_from": this.props.user.username
  }
    this.messagerService.sendMessage(newMsg).then(res => {
      this.props.dispatch({type: 'setMsgNum', msgNum: 0})

    })
  }
  

  render() {
    let myNum = this.props.msgNum
    if(myNum>0){
      console.log(myNum)
      let map = new Map(this.props.messages.map(el=>[el._id,el]));
      console.log(map.get(myNum).msg_msg)
      return (
          <center>
              <div>
                From: {map.get(myNum).msg_from}<br/>
                <div class="message">{map.get(myNum).msg_msg}</div><br/>

              </div>
          </center>
          
        );
      }
    else{
      return (
        <center>
            <div>
              To: <select ref={this.toMessage} id='sendToWho'>
              {this.props.user_array.map((user) =>
                    <option value={user.username}>
                      {user.username}
                    </option>)}
              </select>
              Message:<br/>
              <textarea ref={this.message} id="msgBody"></textarea>
              <button onClick={this.msgSend}>Send</button>
            </div>
        </center>
      );
    }
  }
}

function mapStateToProps(state) {
  const {user, msgNum, messages, user_array} = state;
  return {user: user, msgNum: msgNum, messages: messages, user_array: user_array}
}
export default connect(mapStateToProps) (MsgBody);
