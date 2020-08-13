import React, { Component } from "react";
import MessagerService from '../../service/messager.service';
import { connect } from 'react-redux';

class Messages extends Component {
    constructor(props){
        super(props);
        this.to_msg = this.to_msg.bind(this);
      };
      messagerService = new MessagerService();
  state = {
  };

  to_msg = (event) => {
    console.log(event.target.id)
    this.props.dispatch({type: 'setMsgNum', msgNum: event.target.id})
  }

  render() {
        return (
            <center>
                <div id="messages">
                    {this.props.messages.map((msg) =>
                    <div class="msg_body" id={msg._id} onClick={this.to_msg}>
                      {msg._id}. {msg.msg_from}
                    </div>)}
                </div>
            </center>
        );
  }
}

function mapStateToProps(state) {
    const {user, msgNum, messages} = state;
    return {user: user, msgNum: msgNum, messages: messages}
  }
export default connect(mapStateToProps) (Messages);
