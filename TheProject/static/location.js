
function getLocation() {
    if (document.getElementById("isGameWon").checked) {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                function (position) {
                    var xhttp = new XMLHttpRequest();

                    const value = `; ${document.cookie}`;
                    const parts = value.split(`; ${'csrftoken'}=`);
                    if (parts.length === 2) {
                        var csrftoken =  parts.pop().split(';').shift();
                    }
                
                    xhttp.open("POST", "/claim", true);
                    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                    xhttp.setRequestHeader("X-CSRFToken", csrftoken);
                
                    xhttp.onreadystatechange = function() {
                        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
                            if (confirm(xhttp.responseText)) {
                                window.location.reload();
                            }
                            else {
                                window.location.reload();
                            }
                        }
                    }
                
                    xhttp.send("long="+position.coords.longitude+"&lat="+position.coords.latitude);
                },
                function (error) {
                    alert(error.code + ": " + error.message);
                },
                {
                    enableHighAccuracy: true,
                    maximumAge: 10000,
                    timeout: 5000
                }
            );
        }
        else {
            window.alert("Issue getting location.")
        }
    }
    else {
        window.alert("You have not completed the game. Complete the game to claim the building.")
    }
}
