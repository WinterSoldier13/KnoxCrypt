function submit_workflow(){

    let password = document.getElementById("password_field").textContent;
    let re_password = document.getElementById("re_password").textContent;

    alert(password)

    if(password.length == 0 || re_password.length == 0){
        alert("this")
        return;
    }

    alert("if you are going for encrypt operation make sure you rememeber this password, or else you will loose your files forever");

    if(password != re_password){
        alert("Passwords do not match!")
    }
    else{
        // todo start the backend server and do the encryption
    }
}