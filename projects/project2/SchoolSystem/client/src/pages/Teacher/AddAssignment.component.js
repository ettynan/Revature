import React, { Component } from "react";

import TeacherService from '../../service/teacher.service';
import AssignmentService from '../../service/assignment.service';

import { connect } from 'react-redux';

class AddAssignment extends Component {
  /*
  constructor(props){
    super(props);
  };
  */
  teacherService = new TeacherService();
  assignmentService = new AssignmentService();
  state = {
  };

  componentDidMount() {
  }

  assign_work = () => {
    console.log('in assign work')
    let the_assignment = {
        "_id": -1,
        "name": document.getElementById('name').value,
        "due": document.getElementById('due').value,
        "description": document.getElementById('description').value,
        "teacher": this.props.user.fullname
    }
    this.assignmentService.teacher_assign_work(the_assignment).then(res => {
        this.to_teach_menu()
    })
  }

  to_teach_menu = () => {
    this.props.dispatch({type: 'toggleAssignHW', isAssigning: false})
    document.getElementById('to_assign').hidden = false
    document.getElementById('hideAssign').hidden = true
  }

  render() {
    console.log(this.props.isAssigning)
    if(this.props.isAssigning === true){

    return (
        <center>
            <table align="center">
            <tr>
                <td id='toRight'>Assignment Name:</td>
                <td>
                <input type="text" id="name" value={this.state.assignment}/>
                </td>
            </tr>
            <tr>
                <td id='toRight'>Due Date:</td>
                <td>
                <input type="date" id="due" value={this.state.due}/>
                </td>
            </tr>
            <tr>
                <td id='toRight'>Description of Assignment:</td>
                <td>
                <textarea id="description" value={this.state.description}>
                </textarea>
                </td>
            </tr>
            </table>
            <button id="to_assign" onClick={this.assign_work}>Add Assignment </button>
        </center>

      );}
      else{
          return (<></>)
      }
  }
}
function mapStateToProps(state) {
    const {user, user_array, isAssigning} = state;
    return {user: user, user_array: user_array, isAssigning: isAssigning}
  }
export default connect(mapStateToProps) (AddAssignment);
