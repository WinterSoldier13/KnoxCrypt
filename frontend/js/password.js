function submit_workflow(){
    alert("if you are going for encrypt operation make sure you rememeber this password, or else you will loose your files forever");

    let password = document.getElementById("password").textContent;
    let re_password = document.getElementById("re_password").textContent;

    if(password != re_password){
        alert("Passwords do not match!")
    }
    else{
        // todo start the backend server and do the encryption
    }
}