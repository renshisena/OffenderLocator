//Declaration
var firstName = document.getElementById('inputFname');
var lastName = document.getElementById('inputLname');
var age = document.getElementById('inputAge');
var gender = document.getElementById('inputGender');
var offense = document.getElementById('inputOffense');
var casedetails = document.getElementById('inputCaseDetails');
var currentPassword = "admin";

//variables for forgot.html

var row = 1;
//Login Script
var login = document.getElementById("login");
login.addEventListener("click", validate);
//File Complaint
var entry = document.getElementById("fileComplaint");
entry.addEventListener("click", displayOffenders);

var resetPass = document.getElementById("resetPass");
resetPass.addEventListener("click", resetPassword())

function checkInputs(){
    var firstNameValue = firstName.value.trim()
    var lastNameValue = lastName.value.trim()
    var ageValue = age.value.trim()
    var genderValue = gender.value.trim()
    var offenseValue = offense.value.trim()
    var casedetailsValue = casedetails.value.trim()
}

function displayOffenders(){
    var oFirstName = document.getElementById("inputFname").value;
    var oLastName = document.getElementById("inputLname").value;
    var oAge = document.getElementById("inputAge").value;
    var oGender = document.getElementById("inputGender").value;
    var oOffense = document.getElementById(inputOffense).value;
    var oCaseDetails = document.getElementById("inputCaseDetails").value;

    if (!oFirstName || !oLastName || !oAge || !oGender || !oOffense || !oCaseDetails){
        alert("Please fill up empty fields!");
        return;
    }
    
    
    var offenderTable = document.getElementById("offenderTable");
    var newRow = offenderTable.insertRow(row);
    var cell1 = newRow.insertCell(0);
    var cell2 = newRow.insertCell(1);
    var cell3 = newRow.insertCell(2);
    var cell4 = newRow.insertCell(3);
    var cell5 = newRow.insertCell(4);
    var cell6 = newRow.insertCell(5);

    cell1.innerHTML = oFirstName;
    cell2.innerHTML = oLastName;
    cell3.innerHTML = oFirstName;
    cell4.innerHTML = oAge;
    cell5.innerHTML = oFirstName;
    cell6.innerHTML = oGender;
}

localStorage.setItem("currentPasswordValue",currentPassword);
function validate(){
    var inputLoginP = document.getElementById("inputLoginPassword").value;
    var inputLoginC = document.getElementById("inputLoginConfirm").value; 
    
    if (inputLoginP == currentPassword && inputLoginC == currentPassword){
        alert("Log-in Successfully");
        window.location.href = 'lookupAdmin.html'
        return false;
        }
        else{
            alert("Log-in Failed");

        }
    }

function resetPassword(){
    var inputResetP = document.getElementById("inputResetPassword").value;
    var inputResetC = document.getElementById("inputResetConfirm").value;
    
    if (!inputResetP || !inputResetC){
            alert("Fill up empty fields!");
            return;
        }
    if (inputResetC == currentPassword){
        alert("Cannot have same password as before!");
    }
    if (!inputResetC){
        alert("Fill up empty fields!")

    }
    if (!inputResetP){
        alert("Fill up empty fields!")
    }
    if (inputResetP == currentPassword === !inputResetC);{
        alert("You have set new a password.")
        window.location.href = 'login.html'
            return false;
    }
    
}
    
        