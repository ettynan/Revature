import React, { Component } from "react";
import { connect } from 'react-redux';
import StudentService from '../../service/student.service'
import AssignmentService from '../../service/assignment.service';
import SubmissionService from '../../service/submission.service';


class Student extends Component {
  constructor(props){
    super(props);
    this.getAssignments = this.getAssignments.bind(this);
    this.getRequirements = this.getRequirements.bind(this);
    this.assignment = '';
  };

  assignmentService = new AssignmentService();
  submissionService = new SubmissionService();

  studentService = new StudentService();

  showGrades = () => {
    this.hideAll();
    console.log('Show Grades')
    console.log(this.props.user.grades)
    //If the student does not have any grades, display a message
    if (!this.props.user.grades || this.props.user.grades === []) {
      this.props.dispatch( { type: 'showGrades', grades: [{'class': 'There are no grades', 'grade': ''}]})
    }
    //Else show their grades
    else {
      this.props.dispatch({ type: 'showGrades', grades: this.props.user.grades})
    }
    document.getElementById('hideGrades').hidden = false
    document.getElementById('showGrades').hidden = true
  };

  hideGrades = () => {
    this.props.dispatch({ type: 'showGrades', grades: []})
    document.getElementById('showGrades').hidden = false
    document.getElementById('hideGrades').hidden = true
  }

  updateForm =  () => {
    this.hideAll();
    let name = this.props.user.username
    let password = this.props.user.password
    let address = this.props.user.address
    document.getElementById('usernameLabel').hidden = false
    document.getElementById('username').hidden = false
    document.getElementById('username').value = name
    document.getElementById('passwordLabel').hidden = false
    document.getElementById('password').hidden = false
    document.getElementById('password').value = password
    document.getElementById('addressLabel').hidden = false
    document.getElementById('address').hidden = false
    document.getElementById('address').value = address
    document.getElementById('submitEdit').hidden = false
    document.getElementById('hideEdit').hidden = false
    document.getElementById('showEdit').hidden = true
  }

  hideUpdateForm = () => {
    document.getElementById('usernameLabel').hidden = true
    document.getElementById('username').hidden = true
    document.getElementById('passwordLabel').hidden = true
    document.getElementById('password').hidden = true
    document.getElementById('addressLabel').hidden = true
    document.getElementById('address').hidden = true
    document.getElementById('submitEdit').hidden = true
    document.getElementById('showEdit').hidden = false
    document.getElementById('hideEdit').hidden = true
  }

  updateProfile = () => {

    let newUsername = document.getElementById('username').value
    let newPassword = document.getElementById('password').value
    let newAddress = document.getElementById('address').value
    let updateForm = {'username': newUsername, 'password': newPassword, 'address': newAddress}
    this.studentService.submitProfileUpdate(this.props.user.username, updateForm).then(res => {
      
      window.alert('Your profile update is pending approval')
      this.hideUpdateForm()
  });
  }

  scheduleForm =  () => {
    this.hideAll();
    let p1 = this.props.user.current_schedule.period_1
    let p2 = this.props.user.current_schedule.period_2
    let p3 = this.props.user.current_schedule.period_3
    let p4 = this.props.user.current_schedule.period_4
    let p5 = this.props.user.current_schedule.period_5

    document.getElementById('period1Label').hidden = false
    document.getElementById('period1').hidden = false
    document.getElementById('period1').value = p1
    document.getElementById('period2Label').hidden = false
    document.getElementById('period2').hidden = false
    document.getElementById('period2').value = p2
    document.getElementById('period3Label').hidden = false
    document.getElementById('period3').hidden = false
    document.getElementById('period3').value = p3
    document.getElementById('period4Label').hidden = false
    document.getElementById('period4').hidden = false
    document.getElementById('period4').value = p4
    document.getElementById('period5Label').hidden = false
    document.getElementById('period5').hidden = false
    document.getElementById('period5').value = p5
    document.getElementById('submitSchedule').hidden = false
    document.getElementById('hideSchedule').hidden = false
    document.getElementById('showSchedule').hidden = true
  }

  hideScheduleForm = () => {
    document.getElementById('period1Label').hidden = true
    document.getElementById('period1').hidden = true
    document.getElementById('period2Label').hidden = true
    document.getElementById('period2').hidden = true
    document.getElementById('period3Label').hidden = true
    document.getElementById('period3').hidden = true
    document.getElementById('period4Label').hidden = true
    document.getElementById('period4').hidden = true
    document.getElementById('period5Label').hidden = true
    document.getElementById('period5').hidden = true
    document.getElementById('submitSchedule').hidden = true
    document.getElementById('showSchedule').hidden = false
    document.getElementById('hideSchedule').hidden = true
  }

  updateSchedule = () => {

    let p1 = document.getElementById('period1').value
    let p2 = document.getElementById('period2').value
    let p3 = document.getElementById('period3').value
    let p4 = document.getElementById('period4').value
    let p5 = document.getElementById('period5').value
    let scheduleForm = {'period_1': p1, 'period_2': p2, 'period_3': p3, 'period_4': p4, 'period_5': p5}
    this.studentService.submitScheduleUpdate(this.props.user.username, scheduleForm).then(res => {
      
      window.alert('Your profile update is pending approval')
      this.hideScheduleForm()
  });
  }

  select = (event) => {
    this.assignment = event.target.previousSibling.wholeText;
    document.getElementById("thisAssignment").innerHTML = this.assignment;
  }

  getAssignments() {
    this.hideAll();
    this.assignmentService.getAssignments().then(res => {
      console.log(res.data)
      this.props.dispatch({type: 'getAssignments', assignment_array: res.data})
      document.getElementById('assignments').hidden = false
      document.getElementById('homework').hidden = false
      document.getElementById('submitHomework').hidden = false
      document.getElementById('cancelHomework').hidden = false
      document.getElementById('findHomework').hidden = true
    })
  }

  hideAssignments() {
    console.log('Hide Assignments')
    document.getElementById('assignments').hidden = true
    document.getElementById('homework').hidden = true
    document.getElementById('submitHomework').hidden = true
    document.getElementById('cancelHomework').hidden = true
    document.getElementById('findHomework').hidden = false
  }

  submit = () => {
    var username = this.props.user.username;
    var assignment = this.assignment;
    var content = document.getElementById("homework").value 
    this.submissionService.newSubmission(username, assignment, content).then(res => {
      console.log(res.data)
      this.props.dispatch({type: 'newSubmission'})
      window.alert('Submitted document for ' + assignment)
      this.hideAssignments()
    })
  }

  getRequirements = () => {
    this.hideAll();
    this.studentService.getRequirements(this.props.user.username).then(res => {
      console.log(res.data)
      this.props.dispatch({type: 'getRequirements', student: res.data})
      document.getElementById('hideGradReq').hidden = false
      document.getElementById('showGradReq').hidden = true
    })
  }

  hideRequirements = () => {
    console.log('Hide Requirements')
    this.props.dispatch( {type: 'getRequirements', student: []})
    document.getElementById('hideGradReq').hidden = true
    document.getElementById('showGradReq').hidden = false
  }

  hideAll = () => {
    this.hideAssignments();
    this.hideGrades();
    this.hideRequirements();
    this.hideScheduleForm();
    this.hideUpdateForm();
  }

  render() {
    console.log(this.props)
    if (this.props.user) {
      //A Student is logged in and display their grades or edit profile with buttons
      return (
        <>
          <center>
            <div id='title'><h1>Student</h1></div>
            <div id='content'>
              <div id='container'>
                Welcome back, {this.props.user.fullname}!<br/>
                
                {/* Grades button */}
                <button id="showGrades" onClick={this.showGrades}>Grades</button>
                  <button hidden='true' id="hideGrades" onClick={this.hideGrades}>Hide Grades</button>
                
                {/* edit Profile */}
                <button id="showEdit" onClick={this.updateForm}>Edit Profile</button>
                  <button hidden='true' id="hideEdit" onClick={this.hideUpdateForm}>Hide Profile</button>
                
                {/* edit schedule */}  
                <button id="showSchedule" onClick={this.scheduleForm}>Edit Schedule</button>
                  <button hidden='true' id="hideSchedule" onClick={this.hideScheduleForm}>Hide Schedule</button>
                
                {/* submit homework */}
                <button id='findHomework' onClick={this.getAssignments}>Submit Homework</button>
                  <button id='cancelHomework' hidden='true' onClick={this.hideAssignments}>Hide Homework</button>

                {/* check grad req */}
                <button id='showGradReq' onClick={this.getRequirements}>Check Graduation Requirements</button>
                  <button id='hideGradReq' hidden='true' onClick={this.hideRequirements}>Hide Graduation Requirements</button>

                <div>
                    {this.props.grades.map(grade => 
                      <p key={grade.class}>{grade.class} : {grade.grade}</p>
                    )}
                </div>
                <div>
                      <p hidden='true' id='usernameLabel'>Username</p>
                      <input hidden='true' type='text' id='username'></input>
                      <p hidden='true' id='passwordLabel'>Password</p>
                      <input hidden='true' type='text' id='password'></input>
                      <p hidden='true' id='addressLabel'>Address</p>
                      <input hidden='true' type='text' id='address'></input>
                      <p><button hidden='true' id='submitEdit' onClick={this.updateProfile}>Submit</button></p>
                </div>
                
                <div>
                      <p hidden='true' id='period1Label'>1st Period</p>
                      <input hidden='true' type='text' id='period1'></input>
                      <p hidden='true' id='period2Label'>2nd Period</p>
                      <input hidden='true' type='text' id='period2'></input>
                      <p hidden='true' id='period3Label'>3rd Period</p>
                      <input hidden='true' type='text' id='period3'></input>
                      <p hidden='true' id='period4Label'>4th Period</p>
                      <input hidden='true' type='text' id='period4'></input>
                      <p hidden='true' id='period5Label'>5th Period</p>
                      <input hidden='true' type='text' id='period5'></input>
                      <p><button hidden='true' id='submitSchedule' onClick={this.updateSchedule}>Submit</button></p>
                </div>

                <div id="assignments" hidden='true'>
                      { this.props.assignment_array.map(assignment =>
                      <>{assignment.name}<button onClick={this.select}>Select Assignment</button><br></br></>)}
                      <p id="thisAssignment"></p>
                      <textarea id="homework" hidden='true'></textarea>
                      <button id='submitHomework' hidden='true' onClick={this.submit}>Submit</button>
                </div><br/>
                { this.props.student.map(x =>
                    <>
                      <p>English: {x.english}/5</p><br></br><p>Math: {x.math}/5</p><br></br><p>Science: {x.science}/5</p><br></br><p>Social Studies: {x.social_studies}/5</p></>)}
              </div>
            </div>
          </center>
          
              </>
      );
    }
    else {
      //No user is logged in
      return (
        <h1>You are not a Student</h1>
      )
    }
  }
}

function mapStateToProps(state) {
  const {user, grades, assignment_array, schedule, student} = state;
  return {user: user, grades: grades, assignment_array: assignment_array, schedule: schedule, student: student}
}

export default connect(mapStateToProps)(Student);