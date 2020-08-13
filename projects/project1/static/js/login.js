console.log('Hello from login')

window.onload = () => {
    console.log('in load function')
    document.getElementById('login_button').addEventListener('click', event => {
        event.preventDefault();
        authenticate();
        console.log('end login function')
    })
    document.getElementById('register_button').addEventListener('click', event => {
        event.preventDefault();
        registration();
        console.log('end registration function')
        window.location = ('apply')
    })
}

loggedUser = null
customer_loans = []
manager_loans = []
function authenticate(){
    let person = {}
    person['username'] = document.getElementById('username1').value;
    person['password'] = document.getElementById('password1').value;
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = loginSuccess;
    xhr.open('POST', '/users/' + person['username']);
    xhr.send(JSON.stringify(person));

    function loginSuccess() {
        console.log(xhr.readyState)
        console.log(xhr.status)
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log('login success!')
            loggedUser = JSON.parse(xhr.responseText)
            document.getElementById('personHeader').innerHTML = "Hello, " + person['username'];
            console.log('logged user', loggedUser)
            clientDirection(loggedUser);
        }
    }
}

function clientDirection(loggedUser){
    if (loggedUser['role'] == 'manager'){
        window.location = ('index')
    } else if (loggedUser['role'] == 'customer'){
        window.location = ('apply')
    }
}

function registration(){
    let newPerson = {}
    newPerson['firstname'] = document.getElementById('firstname').value;
    newPerson['lastname'] = document.getElementById('lastname').value;
    newPerson['username'] = document.getElementById('username').value;
    newPerson['password'] = document.getElementById('password').value;
    newPerson['role'] = document.getElementById('selectRole').value;
    console.log(newPerson)
    username = newPerson['username']
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = processResponse;
    xhr.open('POST', '/users');
    console.log(newPerson)
    xhr.send(JSON.stringify(newPerson));

    function processResponse() {
        console.log(xhr.readyState)
        console.log(xhr.status)
        if(xhr.readyState === 4 && xhr.status === 201){
            loggedUser = JSON.parse(xhr.responseText)
            console.log("Successful Registration")
            document.getElementById('personHeader').innerHTML = "Hello, " + username;
            console.log('logged user', loggedUser)
        } else{
            console.log("Unsuccessful Registration")
        }
    }
}

