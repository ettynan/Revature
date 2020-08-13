console.log('Hello from apply info')

window.onload = () => {
    console.log('in load function for apply')
    document.getElementById('submit_btn').addEventListener('click', event => {
        event.preventDefault();
        create_application();
        console.log('end apply function')
    })

}

loggedUser = null
function create_application(){
    let info = {}

    info['username'] = document.getElementById('username').value;
    info['firstname'] = document.getElementById('firstname').value;
    info['lastname'] = document.getElementById('lastname').value;
    info['age'] = document.getElementById('age').value;
    info['gender'] = document.getElementById('gender').value;
    info['ssn'] = document.getElementById('ssn').value;
    info['employer'] = document.getElementById('employer').value;
    info['title'] = document.getElementById('title').value;
    info['salary'] = document.getElementById('salary').value;
    info['expenses'] = document.getElementById('expenses').value;
    info['b_street'] = document.getElementById('b_street').value;
    info['b_state'] = document.getElementById('b_state').value;
    info['b_city'] = document.getElementById('b_city').value;
    info['b_zip'] = document.getElementById('b_zip').value;
    info['m_street'] = document.getElementById('m_street').value;
    info['m_state'] = document.getElementById('m_state').value;
    info['m_city'] = document.getElementById('m_city').value;
    info['m_zip'] = document.getElementById('m_zip').value;

    info['loan_type'] = document.getElementById('loan_type').value;


    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = applySuccess;
    xhr.open('POST', '/loans');
    console.log(info);
    // xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhr.send(JSON.stringify(info));

    function applySuccess() {
        console.log(xhr.readyState)
        console.log(xhr.status)
        if (xhr.readyState === 4 && xhr.status === 201) {
            console.log(xhr.responseText)
            loggedUser = JSON.parse(xhr.responseText)
            // document.getElementById('personHeader').innerHTML = "Hello, " + person['username'];
            console.log(loggedUser)
            // window.location = 'index'

        }
    }
}



