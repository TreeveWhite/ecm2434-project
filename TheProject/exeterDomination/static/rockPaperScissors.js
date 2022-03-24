var winCounter = 0;
var totalCounter = 0;
var computerScore = 0;

/**
 * Function to update the game text to tell the user what the game is
 * as well as the latest scores
 * @param {int} winCounter Player win counter
 * @param {int} computerScore Computer win counter
 * @param {int} totalCounter Total moves
 */
function updateText(winCounter, computerScore, totalCounter) {
    var paragraph = document.getElementById("gameText");
    paragraph.style.textAlign = "center";
    paragraph.innerHTML = "";
    paragraph.innerHTML += "Please play Rock, Paper, Scissors against the computer in a Best of 5 fashion until you win. Only then will you be able to claim the building.";
    paragraph.innerHTML += "<br><br>";
    paragraph.innerHTML += "Player score: " + winCounter;
    paragraph.innerHTML += "<br>";
    paragraph.innerHTML += "Computer score: " + computerScore;
    paragraph.innerHTML += "<br>";
    paragraph.innerHTML += "Total moves: " + totalCounter;
}

/**
 * Method to create the buttons the user clicks
 */
function loadGame(){
    updateText(winCounter, computerScore, totalCounter);
    var rock = document.createElement('button');
    rock.className = "gameButton"
    rock.id = 'rock'
    rock.innerHTML = "Rock";
    var paper = document.createElement('button');
    paper.className = "gameButton"
    paper.innerHTML = "Paper"
    paper.id = 'paper'
    var scissors = document.createElement('button');
    scissors.className = "gameButton"
    scissors.innerHTML = "Scissors"
    scissors.id='scissors'
    document.getElementById('grid').appendChild(rock);
    document.getElementById('grid').appendChild(paper);
    document.getElementById('grid').appendChild(scissors);
}

/**
 * Method to allow the buttons to be pressed and the parsing the 
 * inner HTML to the game function
 */
function buttonPress(){
    if (winCounter==3&&totalCounter<=5){
        alert("YOU HAVE WON! CLAIM THE BUILDING")
        document.getElementById('claimButton').disabled = false;
    } else if (winCounter<3 && totalCounter==5){
        alert("You have lost, the page will now reload and you can try again.");
        location.reload();
    }
    var rock = document.getElementById('rock')
    var paper = document.getElementById('paper')
    var scissors = document.getElementById('scissors')
    rock.onclick = function(){
        game(rock.innerHTML)
    }
    paper.onclick = function(){
        game(paper.innerHTML)
    }
    scissors.onclick = function(){
        game(scissors.innerHTML)
    }
}

/**
 * Method to run the main game functionality
 * @param {String} element inner HTML of button clicked
 */
function game(element){
    //checking win conditions
    if (totalCounter==5){
        if (winCounter > computerScore){
            document.getElementById('isGameWon').checked = true;
            alert("YOU HAVE WON! CLAIM THE BUILDING")
        } else if (computerScore > winCounter){
            alert("YOU HAVE LOST. THE PAGE WILL RELOAD AND YOU CAN TRY AGAIN");
            location.reload();
        } else {
            alert("YOU HAVE DRAWN. THE PAGE WILL RELOAD AND YOU CAN TRY AGAIN");
            location.reload();
        }
    } else {
        //Choosing a random computer move
        var computerMoves = ['Rock', 'Paper', 'Scissors']
        var index = Math.floor(Math.random()*computerMoves.length);
        var computerMove = computerMoves[index];
        //Draw conditon adds 1 to total moves
        if (element==computerMove){
            totalCounter++;
            alert("Draw")
        } else if (element=='Rock'){
            if(computerMove=='Paper'){
                alert("Lost");
                totalCounter++;
                computerScore++;
                
            } else {
                alert("Won")
                winCounter++;
                totalCounter++;
            }
        } else if (element=='Paper'){
            if(computerMove=='Scissors'){
                alert("Lost");
                totalCounter++;
                computerScore++;
            } else {
                alert("Won")
                winCounter++;
                totalCounter++;
            }
        } else if (element=='Scissors'){
            if(computerMove=='Rock'){
                alert("Lost");
                totalCounter++;
                computerScore++;
            } else {
                alert("Won")
                winCounter++;
                totalCounter++;
            }
        }
    updateText(winCounter, computerScore, totalCounter); //Updating the text on screen based on what happened
    }
}
loadGame()
buttonPress()