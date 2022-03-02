
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.watchPosition(showPosition)
    }
    else {
        window.alert("Issue getting location.")
    }
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }

function showPosition(position) {
    var xhttp = new XMLHttpRequest();
    const csrftoken = getCookie('csrftoken');
    xhttp.open("POST", "/claim", true);
    xhttp.setRequestHeader("Content-type", "text/html");
    xhttp.setRequestHeader("X-CSRFToken", csrftoken);
    xhttp.send("long=50&lat=50");
}