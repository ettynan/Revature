import React, { Component } from "react";
import { connect } from 'react-redux';
import '../../App.css';
import TeacherService from '../../service/teacher.service';
import UserService from '../../service/user.service';
import SubmissionService from '../../service/submission.service';
import AddAssignment from './AddAssignment.component.js';


class Teacher extends Component {
  constructor(props){
    super(props);
    this.URI = 'http://localhost:5000';
    this.user_ref = React.createRef();
    this.getSubmissions = this.getSubmissions.bind(this);
    this.to_assign = this.to_assign.bind(this);
    this.props.dispatch({type: 'toggleAssignHW', isAssigning: false})
    };
  teacherService = new TeacherService();
  userService = new UserService();
  submissionService = new SubmissionService();

  componentDidMount() {
  }
  editForm = {
    display: 'none'
  }

  to_assign = () => {
    this.hideAll();
    this.props.dispatch({type: 'toggleAssignHW', isAssigning: true})
    document.getElementById('to_assign').hidden = true
    document.getElementById('hideAssign').hidden = false
  }

  hideAssign = () => {
    this.props.dispatch({type: 'toggleAssignHW', isAssigning: false})
    document.getElementById('to_assign').hidden = false
    document.getElementById('hideAssign').hidden = true
  }

  editProfile = () => {
    this.hideAll();
    let userName = this.props.user.username;
    let password = this.props.user.password;
    let address = this.props.user.address;

    document.getElementById("usernameTitle").hidden = false;
    document.getElementById("username").hidden = false;
    document.getElementById("username").value = userName;
    document.getElementById("passwordTitle").hidden = false;
    document.getElementById("password").hidden = false;
    document.getElementById("password").value = password;
    document.getElementById("addressTitle").hidden = false;
    document.getElementById("address").hidden = false;
    document.getElementById("address").value = address;
    document.getElementById("submit").hidden = false;
    document.getElementById("hide").hidden = false;
    document.getElementById("show").hidden = true;
  }


  hideProfileForm = () => {
    document.getElementById("usernameTitle").hidden = true;
    document.getElementById("username").hidden = true;
    document.getElementById("passwordTitle").hidden = true;
    document.getElementById("password").hidden = true;
    document.getElementById("addressTitle").hidden = true;
    document.getElementById("address").hidden = true;
    document.getElementById("submit").hidden = true;
    document.getElementById("hide").hidden = true;
    document.getElementById("show").hidden = false;
  }

  grade = (event) => {
    var teacherName = event.target.nextSibling.wholeText
    console.log(teacherName)
    console.log(document.getElementById("letterGrade").value)
    this.submissionService.grade(teacherName, event.target.nextSibling.nextSibling.value).then(res => {
      console.log(res.data)
      this.props.dispatch({type: 'grade'})
    })
  };


  updateTeacher = () => {
    let newUsername = document.getElementById('username').value
    let newPassword = document.getElementById('password').value
    let newAddress = document.getElementById('address').value
    let updateProfileForm = {'username': newUsername, 'password': newPassword, 'address': newAddress}
    this.teacherService.updateTeacherProfile(this.props.user.username, updateProfileForm).then(res=> {
      console.log(res.data);
      window.alert('Profile Updated')
    });
  }

  getSubmissions = () => {
    this.hideAll();
    document.getElementById('myGrading').style.display='block';
    console.log(this.props.user.username)
    this.submissionService.getSubmissions(this.props.user.username).then(res => {
      console.log(res.data)
      this.props.dispatch({type: 'getSubmissions', submission_array: res.data})
      document.getElementById('showHomework').hidden = true
      document.getElementById('hideHomework').hidden = false
    });
  }

  hideSubmissions = () => {
    document.getElementById('myGrading').style.display='none';
    this.props.dispatch({type: 'getSubmissions', submission_array: []})
    document.getElementById('showHomework').hidden = false
    document.getElementById('hideHomework').hidden = true
  }

  hideAll() {
    this.hideProfileForm();
    this.hideAssign();
    this.hideSubmissions();
    document.getElementById('myGrading').style.display='none';
    this.props.dispatch({type: 'toggleAssignHW', isAssigning: false})
  }

  render() {
    console.log(this.props.user)
    if (this.props.user) {
      return (
        <center>
          <div id='title'><h1>Teacher</h1></div>
          <div id='content'>
            <div id='container'>
            <p>Welcome back, {this.props.user.fullname}!</p>

            {/* Edit Profile */}
            <button id="show" onClick={this.editProfile}>Edit Profile</button>
                <button hidden='true' id="hide" onClick={this.hideProfileForm}>Hide Profile</button>

            {/* Add Assingment */}
            <button id="to_assign" onClick={this.to_assign}>Add Assignment</button>
            <button id="hideAssign" onClick={this.hideAssign} hidden="true">Hide Assignment</button>

            {/* Grade Homework */}
            <button id="showHomework" onClick={this.getSubmissions}>Grade Homework</button>
            <button id="hideHomework" onClick={this.hideSubmissions} hidden="true">Hide Homework</button>

                <p hidden='true' id='usernameTitle'>Username</p>
                <input hidden='true' type='text' id='username'></input>
                <p hidden='true' id='passwordTitle'>Password</p>
                <input hidden='true' type='text' id='password'></input>
                <p hidden='true' id='addressTitle'>Address</p>
                <input hidden='true' type='text' id='address'></input>
                <p><button hidden='true' id='submit' onClick={() => {this.updateTeacher();
                                                                    this.hideProfileForm();}} >Submit</button></p>
 

          <div id='myGrading' style={{display:'none'}}>
            { this.props.submission_array.map(user =>
            <><button onClick={this.grade}>Grade</button>{user._id}<input id="letterGrade"></input>{user.student} {user.content} <br></br></>
            )}
          </div>

          
          
          <AddAssignment/>
          </div>
        </div>
          
        </center>
      );
    } else {
      return (
        <h1>Cannot find you as a teacher</h1>

      )
    }
  }

}


function mapStateToProps(state) {
  const {user, submission_array, isAssigning} = state;
  return {user: user, submission_array: submission_array, isAssigning: isAssigning}
}

export default connect(mapStateToProps)(Teacher);