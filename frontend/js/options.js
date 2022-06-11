window.onload = function () {
    let folder_path = localStorage.getItem("folder_path");
    document.getElementById("folder_path").textContent = folder_path;
}