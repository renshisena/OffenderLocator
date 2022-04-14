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

var register = document.getElementById("register");
register.addEventListener("click", register)

var resetPass = document.getElementById("resetPass");
resetPass.addEventListener("click", resetPassword);

var searchAdmin = document.getElementById("searchAdminLookup");
searchAdmin.addEventListener("click",checkSearchAL);

var searchLookup = document.getElementById("searchOffenderBtn");
searchLookup.addEventListener("click",checkSearch);

function register(){
    window.location.href = '/registration'
    return;
}

localStorage.setItem("currentPasswordValue",currentPassword);
function validate(){
    var inputLoginP = document.getElementById("inputLoginPassword").value;
    var inputLoginC = document.getElementById("inputLoginConfirm").value; 
    
    if (inputLoginP == currentPassword && inputLoginC == currentPassword){
        alert("Logged-in Successfully");
        window.location.href = '/admin_lookup'
        return false;
        } if (inputLoginP != currentPassword || inputLoginC != currentPassword){
            alert("Incorrect password!")
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

  function logout(){
    let text = "Are you sure do you want to leave?";
  if (confirm(text) == true) {
    text = "Logging Out!";
    window.location.href = '/login'
    return;
  } else {
    text = "Canceled Operation";
    return;
  }

}
