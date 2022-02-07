//Declaration
var firstName = document.getElementById('inputFname');
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

var resetPass = document.getElementById("resetPass");
resetPass.addEventListener("click", resetPassword);

var searchAdmin = document.getElementById("searchAdminLookup");
searchAdmin.addEventListener("click",checkSearchAL);

var searchLookup = document.getElementById("searchOffenderBtn");
searchLookup.addEventListener("click",checkSearch);

function checkInputs(){
    var firstNameValue = firstName.value.trim()
    var ageValue = age.value.trim()
    var genderValue = gender.value.trim()
    var offenseValue = offense.value.trim()
    var casedetailsValue = casedetails.value.trim()
}

localStorage.setItem("currentPasswordValue",currentPassword);
function validate(){
    var inputLoginP = document.getElementById("inputLoginPassword").value;
    var inputLoginC = document.getElementById("inputLoginConfirm").value; 
    
    if (inputLoginP == currentPassword && inputLoginC == currentPassword){
        window.location.href = '/admin_lookup'
        return false;
        } if (inputLoginP != currentPassword || inputLoginC != currentPassword){
            alert("Type correct password!");
        }
    }

function resetPassword(){
    var inputResetP = document.getElementById("inputResetPassword").value;
    var inputResetC = document.getElementById("inputResetConfirm").value;
    
    if (inputResetC == currentPassword){
        alert("Cannot have same password as before!");
        return false;
    }
    if (inputResetP == currentPassword === !inputResetC);{
        alert("You have set new a password.")
        window.location.href = '/login'
            return false;
    }
    
}

function checkSearch(){
  var inputName,filter,table, tr, td, i, txtValue;
  inputName = document.getElementById("searchName");
  table = document.getElementById("lookupTable");
  filter = inputName.value.toUpperCase();
  tr = table.getElementsByTagName("tr");
  
  
  for (i = 0; 1 < tr.length; i++){
      td = tr[i].getElementsByTagName("td")[0];
      if (td) {
          txtValue = td.textContent || td.innerText;
          if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
          } else {
            tr[i].style.display = "none";
          }
        }       
      }
    }

function checkSearchAL(){
  var inputName,filter,table, tr, td, i, txtValue;
  inputName = document.getElementById("searchALname");
  table = document.getElementById("adminTable");
  filter = inputName.value.toUpperCase();
  tr = table.getElementsByTagName("tr");
  
  
  for (i = 0; 1 < tr.length; i++){
      td = tr[i].getElementsByTagName("td")[0];
      if (td) {
          txtValue = td.textContent || td.innerText;
          if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
          } else {
            tr[i].style.display = "none";
          }
        }       
      }
    }