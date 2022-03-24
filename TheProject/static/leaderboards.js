

function showDiv()
{
    document.getElementById("msg").textContent = ""
    selected = document.getElementById("leaderboardSelect").value;
    if (selected == "playersDiv") 
    {
        document.getElementById("playersDiv").style.display = "block"
        document.getElementById("teamsDiv").style.display = "none"
    }
    else
    {
        document.getElementById("playersDiv").style.display = "none"
        document.getElementById("teamsDiv").style.display = "block"
    }

}