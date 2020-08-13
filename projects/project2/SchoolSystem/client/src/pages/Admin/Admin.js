import React, { Component } from "react";
import AdminService from '../../service/admin.service';
import StudentService from '../../service/student.service';
import TeacherService from '../../service/teacher.service';
import UserService from '../../service/user.service';
import { connect } from 'react-redux';

class Admin extends Component {
  constructor(props){
    super(props);
    this.getUsers = this.getUsers.bind(this);
    this.getStudents = this.getStudents.bind(this);
    this.getTeachers = this.getTeachers.bind(this);
    this.editAdmin = this.editAdmin.bind(this);
    this.person = '';
  };
  adminService = new AdminService();
  studentService = new StudentService();
  teacherService = new TeacherService();
  userService = new UserService();

  componentDidMount() {
  }

  style = {
    display: "none"
  }
  adminForm = {
    display: "none"
  }
  form = {
    display: "none"
  }
  studentForm = {
    display: 'none'
  }
  editForm = {
    display: 'none'
  }

  editAdmin() {
    var person = document.getElementById("currentUsername").innerHTML;
    var username;
    var password;
    var fullname;
    var address;
    if (document.getElementById("adminUsername").value.length > 0) {
        username = document.getElementById("adminUsername").value;
    }
    else {
        username = document.getElementById("currentUsername").innerHTML
    }
    if (document.getElementById("adminPassword").value.length > 0) {
      password = document.getElementById("adminPassword").value;
    }
    else {
      password = document.getElementById("currentPassword").innerHTML
    }
    if (document.getElementById("adminFullName").value.length > 0) {
      fullname = document.getElementById("adminFullName").value;
    }
    else {
      fullname = document.getElementById("currentFullname").innerHTML
    }
    if (document.getElementById("adminAddress").value.length > 0) {
      address = document.getElementById("adminAddress").value;
    }
    else {
      address = document.getElementById("currentAddress").innerHTML
    }

      this.adminService.editAdmin(person, username, password, fullname, address).then(res => {
      console.log(res.data)
      this.props.dispatch({type: 'editAdmin'})
      if (username) {
        this.userService.login(username, this.props.user.password).then(res => {

          console.log(res.data.role);
          console.log(res.data.username)
          this.props.dispatch( { type: 'login', username: res.data.username, user: res.data, password: this.props.password})
        });
      }
      else {
        this.userService.login(this.props.user.username, this.props.user.password).then(res => {

          console.log(res.data.role);
          console.log(res.data.username)
          this.props.dispatch( { type: 'login', username: res.data.username, user: res.data, password: this.props.password})
        });
      }
      
      window.alert('Profile Updated')
      this.hideAll()
    })
  }

  hideAll(){
    document.getElementById('users').style.display = 'none';
    document.getElementById('students').style.display = 'none';
    document.getElementById('teachers').style.display = 'none';
    document.getElementById("buttonRow").style.display = "none";
    document.getElementById("adminForm").style.display = "none";
    document.getElementById("form").style.display = "none";
    document.getElementById("studentForm").style.display = "none";
    document.getElementById("newAdmin").style.display = "none";
    document.getElementById("newStudent").style.display = "none";
    document.getElementById("newTeacher").style.display = "none";
    document.getElementById("editAdmin").style.display = "none";
    document.getElementById('edit').hidden = false
    document.getElementById('deleteuser').hidden = false
    document.getElementById('showSchedules').hidden = false
    document.getElementById('hideUpdates').hidden = true
    document.getElementById('showUpdates').hidden = false
    document.getElementById('showAssignTeacher').hidden = false
    document.getElementById("cancelUser").hidden = true
    document.getElementById("adduserbtn").hidden = false
    document.getElementById('cancelAssignTeacher').hidden = true
    document.getElementById('hideScheduleUpdates').hidden = true
    document.getElementById('hideUsers').hidden = true
    document.getElementById('updates').hidden = true
    document.getElementById("schedules").hidden = true
    document.getElementById('hideEdit').hidden = true
  }

  showButtons = () => {
    this.hideAll()
    document.getElementById('users').style.display = 'none';
    document.getElementById('students').style.display = 'none';
    document.getElementById('teachers').style.display = 'none';
    document.getElementById("adminForm").style.display = "none";
    document.getElementById("form").style.display = "none";
    document.getElementById("studentForm").style.display = "none";
    document.getElementById("newAdmin").style.display = "none";
    document.getElementById("newStudent").style.display = "none";
    document.getElementById("newTeacher").style.display = "none";
    document.getElementById("buttonRow").style.display = "block";
    document.getElementById("cancelUser").hidden = false
    document.getElementById("adduserbtn").hidden = true
  }

  showAdmin() {
    document.getElementById("adminForm").style.display = "block";
    document.getElementById("form").style.display = "block";
    document.getElementById("newAdmin").style.display = "block";
    document.getElementById("studentForm").style.display = "none";
    document.getElementById("newStudent").style.display = "none";
    document.getElementById("newTeacher").style.display = "none";
  }

  showStudent() {
    document.getElementById("form").style.display = "block";
    document.getElementById("studentForm").style.display = "block";
    document.getElementById("newStudent").style.display = "block";
    document.getElementById("newAdmin").style.display = "none";
    document.getElementById("newTeacher").style.display = "none";
  }

  showTeacher() {
    document.getElementById("form").style.display = "block";
    document.getElementById("newTeacher").style.display = "block";
    document.getElementById("studentForm").style.display = "none";
    document.getElementById("newAdmin").style.display = "none";
    document.getElementById("newStudent").style.display = "none";
  }

  user = (event) => {
    document.getElementById("user").innerHTML = event.target.innerText;
  }

  getUsers() {
    console.log(this.adminService)
    this.hideAll()
    document.getElementById('users').style.display = 'block';


    this.adminService.getUsers().then(res => {
      console.log(res.data)
      this.props.dispatch({type: 'getUsers', user_array: res.data})
      document.getElementById('deleteuser').hidden = true
      document.getElementById('hideUsers').hidden = false
    })
  }

  showForm = () => {
    this.hideAll()
    document.getElementById('editAdmin').style.display = 'block';
    document.getElementById('edit').hidden = true
    document.getElementById('hideEdit').hidden = false
  }

  getStudents() {
    this.hideAll()
    document.getElementById('students').style.display = 'block';
    console.log(this.studentService)
    this.studentService.getStudents().then(res => {
      console.log(res.data)
      this.props.dispatch({type: 'getStudents', student_array: res.data})
      document.getElementById('showAssignTeacher').hidden = true
      document.getElementById('cancelAssignTeacher').hidden = false
    })
  }

  getTeachers = (event) => {
    this.hideAll()
    document.getElementById('teachers').style.display = 'block';
    this.person = event.target.previousSibling.wholeText
    console.log(this.teacherService)
    this.teacherService.getTeachers().then(res => {
      console.log(res.data)
      this.props.dispatch({type: 'getTeachers', teacher_array: res.data})
    })
  }

  newAdmin = () => {
    console.log(document.getElementById("usernameValue").value)
    var username = document.getElementById("usernameValue").value
    var letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
    var one = letters[Math.floor(Math.random() * letters.length)];
    var two = letters[Math.floor(Math.random() * letters.length)];
    var three = letters[Math.floor(Math.random() * letters.length)];
    var four = letters[Math.floor(Math.random() * letters.length)];
    var five = letters[Math.floor(Math.random() * letters.length)];
    var six = letters[Math.floor(Math.random() * letters.length)];
    var seven = letters[Math.floor(Math.random() * letters.length)];
    var eight = letters[Math.floor(Math.random() * letters.length)];
    var password = one + two + three + four + five + six + seven + eight;
    var fullname = document.getElementById("fullnameValue").value
    var address = document.getElementById("addressValue").value
    this.userService.newAdmin(username, password, fullname, address).then(res => {
      alert("User's temporary password is " + password)
      console.log(res.data)
      this.props.dispatch({type: 'newAdmin'})
      this.hideAll()
    })
  };

  newStudent = () => {
    var username = document.getElementById("usernameValue").value;
    var letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
    var one = letters[Math.floor(Math.random() * letters.length)];
    var two = letters[Math.floor(Math.random() * letters.length)];
    var three = letters[Math.floor(Math.random() * letters.length)];
    var four = letters[Math.floor(Math.random() * letters.length)];
    var five = letters[Math.floor(Math.random() * letters.length)];
    var six = letters[Math.floor(Math.random() * letters.length)];
    var seven = letters[Math.floor(Math.random() * letters.length)];
    var eight = letters[Math.floor(Math.random() * letters.length)];
    var password = one + two + three + four + five + six + seven + eight;
    var fullname = document.getElementById("fullnameValue").value
    var address = document.getElementById("addressValue").value
    var age = document.getElementById("ageValue").value
    var grade = document.getElementById("gradeValue").value
    var period1 = document.getElementById("period1").value
    var period2 = document.getElementById("period2").value
    var period3 = document.getElementById("period3").value
    var period4 = document.getElementById("period4").value
    var period5 = document.getElementById("period5").value
    var current_schedule = {'period_1': period1, 'period_2': period2, 'period_3': period3, 'period_4': period4, 'period_5': period5}
    this.userService.newStudent(username, password, fullname, address, age, grade, current_schedule).then(res => {
      console.log(res.data)
      alert("User's temporary password is " + password)
      this.props.dispatch({type: 'newStudent'})
      this.hideAll()
    })
  };

  newTeacher = () => {
    console.log(document.getElementById("usernameValue").value)
    var username = document.getElementById("usernameValue").value
    var letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
    var one = letters[Math.floor(Math.random() * letters.length)];
    var two = letters[Math.floor(Math.random() * letters.length)];
    var three = letters[Math.floor(Math.random() * letters.length)];
    var four = letters[Math.floor(Math.random() * letters.length)];
    var five = letters[Math.floor(Math.random() * letters.length)];
    var six = letters[Math.floor(Math.random() * letters.length)];
    var seven = letters[Math.floor(Math.random() * letters.length)];
    var eight = letters[Math.floor(Math.random() * letters.length)];
    var password = one + two + three + four + five + six + seven + eight;
    var fullname = document.getElementById("fullnameValue").value
    var address = document.getElementById("addressValue").value
    this.userService.newTeacher(username, password, fullname, address).then(res => {
      console.log(res.data)
      alert("User's temporary password is " + password)
      this.props.dispatch({type: 'newTeacher'})
      this.hideAll()
    })

  };

  assign = (event) => {
    var teacherName = event.target.previousSibling.wholeText
    console.log(this.person)
    console.log(teacherName)
    this.userService.assignTeacher(this.person, teacherName).then(res => {
      console.log(res.data)
      this.props.dispatch({type: 'assignTeacher'})
      window.alert('Assigned ' + this.person + ' to ' + teacherName)
      this.hideAll()
    })
  };

  remove = (event) => {
    var name = event.target.previousSibling.wholeText
    console.log(name)
    this.adminService.remove(name).then(res => {
      console.log(res.data)
      this.props.dispatch({type: 'remove'})
      this.getUsers()
    })
  };

  showUpdates = () => {
    this.hideAll()
    console.log('Show Updates')
    this.adminService.getUpdates().then(res => {
      console.log(res.data)
      this.props.dispatch( { type: 'getUpdates', update_array: res.data})
    })
    document.getElementById('updates').hidden = false
    document.getElementById('hideUpdates').hidden = false
    document.getElementById('showUpdates').hidden = true
  }

  hideUpdates = () => {
    console.log('Hide Updates')
    this.props.dispatch( { type: 'getUpdates', update_array: []})
    document.getElementById('updates').hidden = true
    document.getElementById('hideUpdates').hidden = true
    document.getElementById('showUpdates').hidden = false
  }

  acceptUpdate = (event) => {
    var name = event.target.id
    console.log('Accept Update')
    console.log(name)
    this.studentService.updateProfile(name).then(res => {
      console.log(res.data)
      this.showUpdates()
    })
  }

  denyUpdate = (event) => {
    var name = event.target.id
    console.log('Deny Update')
    this.studentService.denyProfileUpdate(name).then(res => {
      console.log(res.data)
      this.showUpdates()
    })
  }

  showScheduleUpdates = () => {
    this.hideAll()
    console.log('Show Schedule Updates')
    this.adminService.getSchedules().then(res => {
      console.log(res.data)
      this.props.dispatch( { type: 'getSchedules', schedule_array: res.data})
    })
    document.getElementById('schedules').hidden = false
    document.getElementById('showSchedules').hidden = true
    document.getElementById('hideScheduleUpdates').hidden = false
  }

  hideScheduleUpdates = () => {
    console.log('Hide Schedule Updates')
    this.props.dispatch( { type: 'getSchedules', schedule_array: []})
    document.getElementById('schedules').hidden = true
    document.getElementById('hideScheduleUpdates').hidden = true
    document.getElementById('showSchedules').hidden = false
  }

  acceptScheduleUpdate = (event) => {
    var name = event.target.id
    console.log('Accept Schedule Update')
    console.log(name)
    this.studentService.updateSchedule(name).then(res => {
      console.log(res.data)
      this.showScheduleUpdates()
    })
  }

  denyScheduleUpdate = (event) => {
    var name = event.target.id
    console.log('Deny Schedule Update')
    this.studentService.denyScheduleUpdate(name).then(res => {
      console.log(res.data)
      this.showScheduleUpdates()
    })
  }

  render() {
    console.log(this.props)
    if (this.props.user) {

      return(

        <center>
           <div id="title"><h1>School System - Admin</h1></div>
           <div id="content">
            <div id="container">
              Welcome back, {this.props.user.fullname} <br/>
              <button id="adduserbtn" onClick={this.showButtons}>Add User </button>
              <button id="cancelUser" onClick={this.hideAll} hidden='true'>Cancel User</button>
              <button id="showAssignTeacher" onClick={this.getStudents}>Assign Student To Teacher</button>
              <button id="cancelAssignTeacher" onClick={this.hideAll} hidden='true'>Cancel Student To Teacher</button>
              <button id="showUpdates" onClick={this.showUpdates}>Check Profile Updates</button>
              <button hidden='true' id="hideUpdates" onClick={this.hideUpdates}>Hide Profile Updates</button>
              <button id="showSchedules" onClick={this.showScheduleUpdates}>Check Schedule Updates</button>
              <button hidden='true' id="hideScheduleUpdates" onClick={this.hideScheduleUpdates}>Hide Schedule Updates</button>
              <button id="deleteuser" onClick={this.getUsers}>Delete User</button>
              <button id='hideUsers' onClick={this.hideAll} hidden='true'>Hide Users</button>
              <button id="edit" onClick={this.showForm}>Edit Profile</button>
                <button id="hideEdit" onClick={this.hideAll} hidden='true'>Hide Profile</button>

              <div id="editAdmin" style={this.editForm}>
                <p id="currentFullname" style={{display: 'none'}}>{this.props.user.fullname}</p>
                <p>Full Name</p>
                <input id="adminFullName"></input>
                <p id="currentUsername" style={{display: 'none'}}>{this.props.user.username}</p>
                <p>Username</p>
                <input id="adminUsername"></input>
                <p id="currentPassword" style={{display: 'none'}}>{this.props.user.password}</p>
                <p>Password</p>
                <input id="adminPassword"></input>
                <p id="currentAddress" style={{display: 'none'}}>{this.props.user.address}</p>
                <p>Address</p>
                <input id="adminAddress"></input>
                <br></br><br></br>
                <button onClick={this.editAdmin}>Edit Profile</button><br/><br/>
              </div>

              <div id="users" style={{display: 'none'}}>
                  <p style={this.props.bold}>Users</p>
                    { this.props.user_array.map(user =>
                    <>{user.fullname}<button onClick={this.remove}>Delete</button><br/></>)}
              </div>
              <div id="students" style={{display: 'none'}}>
                  <p  style={this.props.bold}>Students</p>
                    { this.props.student_array.map(user =>
                    <>{user.username}<button onClick={this.getTeachers}>Get Teacher</button><br/></>)}
              </div>
              <div id="teachers" style={{display: 'none'}}>
                  <p style={this.props.bold}>Teachers</p>
                    { this.props.teacher_array.map(user =>
                    <>{user.username}<button onClick={this.assign}>Assign</button></>)}<br/><br/>
                  <button id="goBack" onClick={this.getStudents}>Back</button>
              </div>
              <div id="updates" hidden='true'>
                  <p style={this.props.bold}>Updates</p>
                  {this.props.update_array.map(update =>
                  <>
                    <h4>User: {update.username}</h4>
                    <li>Username: {update.update_info.username}</li>
                    <li>Password: {update.update_info.password}</li>
                    <li>Address: {update.update_info.address}</li>
                    <p><button id={update.username} onClick={this.acceptUpdate}>Accept</button>
                    <button id={update.username} onClick={this.denyUpdate}>Deny</button></p>
                  </>
                  )}
              </div>
              <div id="schedules" hidden='true'>
                  <p style={this.props.bold}>Schedules</p>
                  {this.props.schedule_array.map(sched =>
                  <>
                    <h4>User: {sched.username}</h4>
                    <li>Period 1: {sched.schedule.period_1}</li>
                    <li>Period 2: {sched.schedule.period_2}</li>
                    <li>Period 3: {sched.schedule.period_3}</li>
                    <li>Period 4: {sched.schedule.period_4}</li>
                    <li>Period 5: {sched.schedule.period_5}</li>
                    <p><button id={sched.username} onClick={this.acceptScheduleUpdate}>Accept</button>
                    <button id={sched.username} onClick={this.denyScheduleUpdate}>Deny</button></p>
                  </>
                  )}
              </div>
              <div id="buttonRow" style={this.style}><br/>
                  What sort of user? <br/><br/>
                  <button id="adminButton" onClick={this.showAdmin}>Admin</button>
                  <button id="studentButton" onClick={this.showStudent}>Student</button>
                  <button id="teacherButton" onClick={this.showTeacher}>Teacher</button>
              </div>
              <div id="adminForm" style={this.adminForm}>
                <button id="studentButton" onClick={this.showStudent} style={this.style}>Student</button>
                <button id="teacherButton" onClick={this.showTeacher} style={this.style}>Teacher</button>
              </div>
              <div id="form" style={this.form}>
                Username<br/>
                <input id="usernameValue"></input><br/>
                Full Name<br/>
                <input id="fullnameValue"></input><br/>
                Address<br/>
                <input id="addressValue"></input><br/>
              </div>
              <div id="studentForm" style={this.studentForm}>
                Age<br/>
                <input id="ageValue"></input><br/>
                Grade<br/>
                <input id="gradeValue"></input><br/>

                <h3>Current Schedule</h3>
                Period 1<br/>
                <input id="period1"></input><br/>
                Period 2<br/>
                <input id="period2"></input><br/>
                Period 3<br/>
                <input id="period3"></input><br/>
                Period 4<br/>
                <input id="period4"></input><br/>
                Period 5<br/>
                <input id="period5"></input><br/>

              </div>
              <center><br/>
                <button id="newAdmin" onClick={this.newAdmin}  style={{display: 'none'}}>Create Admin</button>
                <button id="newStudent" onClick={this.newStudent} style={{display: 'none'}}> Create Student</button>
                <button id="newTeacher" onClick={this.newTeacher} style={{display:'none'}}>Create Teacher</button>
              </center>
              </div>
          </div>
        </center>

      );
    } else {
      //No user is logged in
      return (
        <h1>You are not an Admin</h1>
      )
    }
  }
}

function mapStateToProps(state) {
  const {user, user_array, student_array, teacher_array, update_array, schedule_array, password, username} = state;
  return {user: user, user_array: user_array, student_array: student_array, teacher_array: teacher_array, update_array: update_array, schedule_array: schedule_array, password: password, username: username}
}

export default connect(mapStateToProps)(Admin);