import React, { Component } from "react";

import Messages from './messages.component'
import MsgBody from './msgBody.component'
import MessagerService from '../../service/messager.service';

import { connect } from 'react-redux';

class Messager extends Component {
    constructor(props){
        super(props);
        this.props.dispatch({type: 'setMsgNum', msgNum: 0})
      };
      messagerService = new MessagerService();
  state = {
  };
  
  componentDidMount() {
    this.messagerService.getMessages(this.props.user).then(res => {
      console.log(res.data);
      this.props.dispatch({type: 'getMsgs', messages: res.data})
    });
  }

  closeMsg = () => {
    this.props.dispatch({type: 'setMsgNum', msgNum: 0})
  }
  
  newMsg = () => {
    this.props.dispatch({type: 'setMsgNum', msgNum: -1})
  }

  render() {
      console.log(this.props.msgNum)
      if(this.props.user.role ){
        if(!this.props.msgNum){
          return (
            <center>
              <div id="messager">
                <h2>Messenger</h2>
                  <Messages/>
                  <div class='newMsg' onClick={this.newMsg}>New Message</div>
              </div>
            </center>
          );
        }
        else
        {
          return (
            <center>
              <div id="messager">
                <h2>Messenger</h2>
                  <MsgBody/>
                  <button id='closeMsg' onClick={this.closeMsg}>Close Message</button>
              </div>

            </center>
          );
        }
      }
      else{return(<></>);}
      
    }
  }
  function mapStateToProps(state) {
    const {user, msgNum, messages} = state;
    return {user: user, msgNum: msgNum, messages: messages}
  }
export default connect(mapStateToProps) (Messager);
