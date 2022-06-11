window.onload = function () {
    let folder_path = localStorage.getItem("folder_path");
    document.getElementById("folder_path").textContent = folder_path;

    var url = document.location.href;
    var params = url.split('?')[1];

    if(params == 'encrypt'){
        document.getElementById("operation_type").textContent = "Encryption Operation";
    }
    else if(params == 'decrypt'){
        document.getElementById("operation_type").textContent = "Decryption Operation";
    }
    else{
        document.getElementById("operation_type").textContent = "IN VALID OPERATION";
    }

}

window.post = function(url, data) {
    return fetch(url, {method: "POST", headers: {'Content-Type': 'application/json'}, body: JSON.stringify(data)});
  }
  

function submit_workflow(){

    let password = document.getElementById("password_field").value;
    let re_password = document.getElementById("re_password").value;
    let folder_path = localStorage.getItem("folder_path");

    if(password.length == 0 || re_password.length == 0){
        return;
    }
    if(password != re_password){
        alert("Passwords do not match!")
        return;
    }
    
    if(document.getElementById("operation_type").textContent == "Encryption Operation"){
        alert("you are going for encryption operation make sure you rememeber this password, or else you will loose your files forever");
        out = post("http://127.0.0.1:8000/encrypt", {current_path : folder_path, password : password})
        console.log(out)
    }
    else if (document.getElementById("operation_type").textContent == "Decryption Operation"){
        post("http://127.0.0.1:8000/decrypt", {"current_path" : folder_path, "password" : password})
    }

}