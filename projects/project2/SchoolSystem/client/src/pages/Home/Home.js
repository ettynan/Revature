import React, { Component } from "react";
import { connect } from 'react-redux';
import Student from '../Student/Student';
import Teacher from '../Teacher/Teacher';
import Admin from '../Admin/Admin'
import Messager from '../Messager/messager.component'
import UserService from '../../service/user.service';

class Home extends Component {
  constructor(props){
    super(props);
    this.handleUsername = this.handleUsername.bind(this);
    this.handlePassword = this.handlePassword.bind(this);
    this.handleKeyDown = this.handleKeyDown.bind(this);
    this.login = this.login.bind(this);
    this.handleLogout = this.handleLogout.bind(this);
  }

  userService = new UserService()

  componentDidMount() {
    this.userService.checkLogin().then(
        (res) => {
            this.props.dispatch( { type: 'login', user: res.data })
        }
    )
}

  handleKeyDown(e) {
    if (e.key === 'Enter') {
        this.login();
    }
  }
  
  handleUsername(e) {
    console.log(this.props)
    this.props.dispatch( { type: 'handleUsername', username: e.target.value } )
  }

  handlePassword(e) {
    console.log(this.props)
    this.props.dispatch( { type: 'handlePassword', password: e.target.value } )
  }

  login = () => {
    console.log(this.props)
    this.userService.login(this.props.username, this.props.password).then(res => {
        console.log(res.data.role);
        console.log(res.data.username)
        console.log(res.data.password)
        this.props.dispatch( { type: 'login', username: res.data.username, user: res.data, password: res.data.password})
    }).catch(error => {
        window.alert("Username/Password do not match.")
    });
  };


  handleLogout = () => {
    console.log(this.props)
    this.userService.logout().then(res =>
      {
        this.props.dispatch({ type: 'logout', username: '', user: null, password: ''})
      })
  }


  render() {

    if (this.props.user) {
      if (this.props.user.role === 'student') {
        return (
          <>
            <p><button id="logout" onClick={this.handleLogout}>Logout</button></p>
            <Student/>
            <Messager/>
          </>
        )
      }
      else if (this.props.user.role === 'teacher') {
        return (
          <>
            <p><button id="logout" onClick={this.handleLogout}>Logout</button></p>
            <Teacher/>            
            <Messager/>
          </>
        )
      }
      else if (this.props.user.role === 'admin') {
        return (
          <>
            <p><button id="logout" onClick={this.handleLogout}>Logout</button></p>
            <Admin/>
            <Messager/>
          </>
        )
      }
      else {
        return (
          <>
            <h1>Something's Wrong</h1>
          </>
        )
      }
    }
    else {
      return (
        <center>
          <div id="title" style={{marginTop:54}}><h1>School System</h1></div>
          <div id="content">
            <p>Username</p>
            <input type="text" value={this.props.username}
            onChange={ this.handleUsername } onKeyDown={ (e) => this.handleKeyDown(e) }></input>
            <p>Password</p>
            <input type="password" name="password" 
            onChange={ this.handlePassword } onKeyDown={ (e) => this.handleKeyDown(e) }/><br></br>
            <button id="loginbutton" onClick={this.login}>Log In</button>
          </div>
        </center>
      );
    }
  }
}

function mapStateToProps(state) {
  const {user, username, password} = state;
  return {user: user,
          username: username,
          password: password}
}

export default connect(mapStateToProps)(Home);