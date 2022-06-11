$(".search-btn").click(function () {
    $(".wrapper").addClass("active");
    $(this).css("display", "none");
    $(".search-data").fadeIn(500);
    $(".close-btn").fadeIn(500);
    $(".search-data .line").addClass("active");
    setTimeout(function () {
        $("input").focus();
        $(".search-data label").fadeIn(500);
        $(".search-data span").fadeIn(500);
    }, 800);
});

$(".close-btn").click(function () {
    $(".wrapper").removeClass("active");
    $(".search-btn").fadeIn(800);
    $(".search-data").fadeOut(500);
    $(".close-btn").fadeOut(500);
    $(".search-data .line").removeClass("active");
    $("input").val("");
    $(".search-data label").fadeOut(500);
    $(".search-data span").fadeOut(500);
});

document.getElementById("folder_picker").addEventListener("change", function(event){
    let files = document.getElementById("folder_picker").files;
    console.log(typeof files)
    
    let file_abosolute_path = files[0].path;
    let folder_abosolute_path = file_abosolute_path.substring(0, file_abosolute_path.lastIndexOf('/'));
    console.log(folder_abosolute_path);
    document.getElementById("folder_path").textContent = folder_abosolute_path;
}, false);

function continueButtonWorkflow(){
    setValueInLocalStorage();
    let selector_page = "file:///Users/ayush/code/KnoxCrypt/frontend/options.html"
    document.location.href = selector_page;
    console.log(
        "continue button"
    )
}
function setValueInLocalStorage(){
    folder_abosolute_path = document.getElementById("folder_path").textContent;
    localStorage.setItem("folder_path", folder_abosolute_path);
}
