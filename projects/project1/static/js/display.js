console.log('Hello from display')

window.onload = () => {
    managerLoansToView();
    console.log('in index page')
}

loans_list = []

function managerLoansToView(){
    console.log('manager')
    xhr = new XMLHttpRequest();
    xhr.onreadystatechange = mgrProcessResponse;
    xhr.open('GET', '/loans');
    xhr.send();

    function mgrProcessResponse() {
        console.log(xhr.readyState)
        console.log(xhr.status)
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log('See loans success!')
            //console.log(JSON.parse(xhr.responseText))
            loans_for_manager = JSON.parse(xhr.responseText) //parse thru each object in that JSON
            populateMgrTable(loans_for_manager)
        }
    }
}

bttn_dict = {'loan_type': '', 'risk_score': '', 'credit_score': ''}

function populateMgrTable(loan_list){
    console.log('In manager populate table')
    table = document.getElementById('loans')
    for (loan of loan_list) {
        console.log(loan)
        tr = document.createElement('tr');
        table.appendChild(tr)
        addTableDef(tr, loan.loan_type)
        addTableDef(tr, loan.risk_score)
        addTableDef(tr, loan.credit_score)
        addTableDef(tr, loan.status)
        bttn_dict['loan_type'] = loan.loan_type
        bttn_dict['risk_score'] = loan.risk_score
        bttn_dict['credit_score'] = loan.credit_score
        addLoanApproveButton(tr)
        addLoanDenyButton(tr)
    }
}

function addTableDef(tr, value) {
    td = document.createElement('td')
    td.innerHTML=value
    tr.appendChild(td)
}

function addLoanApproveButton(tr){
    td = document.createElement("td");
    bttn = document.createElement("button");
    bttn.id = bttn.dict
    bttn.type = "button";
    bttn.className = "btn btn-primary";
    bttn.innerHTML = "Approve loan";
    bttn.addEventListener("click", approveLoan);
    td.appendChild(bttn);
    tr.appendChild(td);
}

function approveLoan(){
    bttn_dict['status'] = 'Approved'
    console.log('In approveLoan: ')
    xhr = new XMLHttpRequest()
    xhr.onreadystatechange = processApproveResponse
    xhr.open('POST', '/loans/' + bttn_dict['loan_type'])
    xhr.send(JSON.stringify(bttn_dict))
    function processApproveResponse() {
        if(xhr.readystate === 4 && xhr.status === 200) {
            console.log('Loan approved')
        }
    }
}

function addLoanDenyButton(tr){
    td = document.createElement("td");
    bttn = document.createElement("button");
    bttn.type = "button";
    bttn.id = bttn.dict
    bttn.className = "btn btn-primary";
    bttn.innerHTML = "Deny loan";
    bttn.addEventListener("click", denyLoan);
    td.appendChild(bttn);
    tr.appendChild(td);
}

function denyLoan(){
    bttn_dict['status'] = 'Denied'
    console.log('In denyLoan: ')

    xhr = new XMLHttpRequest()
    xhr.onreadystatechange = processDenyResponse
    xhr.open('POST', '/loans/' + bttn_dict['loan_type'])
    xhr.send(JSON.stringify(bttn_dict))
    function processDenyResponse() {
        if(xhr.readystate === 4 && xhr.status === 200) {
            console.log('In denyLoan')
        }
    }
}

// function customerLoans(){
//     console.log('manager')
//     xhr = new XMLHttpRequest();
//     xhr.onreadystatechange = customerLoansViewSuccess;
//     xhr.open('GET', '/loans/' + person['username']);
//     xhr.send();

//     function customerLoansViewSuccess() {
//         console.log(xhr.readyState)
//         console.log(xhr.status)
//         if (xhr.readyState === 4 && xhr.status === 200) {
//             console.log('login success!')
//             loans_for_manager = JSON.parse(xhr.responseText)
//             populateCustomerLoans(loans_for_customer)
//         }
//     }


// function populateCustomerLoans(loan_list){
//     console.log('client')
//     table = document.getElementById(loans)
//     for (loan of loan_list) {
//         tr = document.createElement('tr')
//         table.appendChild(tr)
//         addTableDef(tr, loan.loan_type)
//         addTableDef(tr, loan.status)
//     }
// }

