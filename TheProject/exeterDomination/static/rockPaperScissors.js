var winCounter = 0;
var totalCounter = 0;
var computerScore = 0;

function loadGame(){
    var paragraph = document.getElementById('gameText');
    paragraph.innerHTML = "Please play Rock, Paper, Scissors against the computer in a Best of 5 fashion until you win <br> Only then will you be able to claim the building.";
    var playerCount = document.getElementById('playerScore')
    playerCount.innerHTML = "Player score: " + winCounter
    var computerScoreP = document.getElementById('computerScore');
    computerScoreP.innerHTML = "Computer score: " + computerScore;
    var totalMoves = document.getElementById('totalMoves')
    totalMoves.innerHTML = "Total moves: " + totalCounter;
    var rock = document.createElement('button')
    rock.id = 'rock'
    rock.innerHTML = "Rock";
    var paper = document.createElement('button')
    paper.innerHTML = "Paper"
    paper.id = 'paper'
    var scissors = document.createElement('button')
    scissors.innerHTML = "Scissors"
    scissors.id='scissors'
    document.getElementById('grid').appendChild(playerCount);
    document.getElementById('grid').appendChild(computerScoreP);
    document.getElementById('grid').appendChild(totalMoves);
    document.getElementById('grid').appendChild(rock);
    document.getElementById('grid').appendChild(paper);
    document.getElementById('grid').appendChild(scissors);
}

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

function game(element){
    var playerCount = document.getElementById('playerScore');
    var computerScoreText = document.getElementById('computerScore');
    var totalMoves = document.getElementById('totalMoves');
    if (totalCounter==5){
        if (winCounter > computerScore){
            alert("YOU HAVE WON! CLAIM THE BUILDING")
            document.getElementById('claimButton').disabled = false;
        } else if (computerScore > winCounter){
            alert("YOU HAVE LOST. THE PAGE WILL RELOAD AND YOU CAN TRY AGAIN");
            location.reload();
        } else {
            alert("YOU HAVE DRAWN. THE PAGE WILL RELOAD AND YOU CAN TRY AGAIN");
            location.reload();
        }
    } else {
        var computerMoves = ['Rock', 'Paper', 'Scissors']
        var index = Math.floor(Math.random()*computerMoves.length);
        var computerMove = computerMoves[index];
        if (element==computerMove){
            totalCounter++;
            totalMoves.innerHTML = "Total moves: " + totalCounter;
            alert("Draw")
        } else if (element=='Rock'){
            if(computerMove=='Paper'){
                alert("Lost");
                totalCounter++;
                totalMoves.innerHTML = "Total moves: " + totalCounter;
                computerScore++;
                computerScoreText.innerHTML = "Computer score: " + computerScore;
                
            } else {
                alert("Won")
                winCounter++;
                playerCount.innerHTML = "Player score: " + winCounter
                totalCounter++;
                totalMoves.innerHTML = "Total moves: " + totalCounter;
            }
        } else if (element=='Paper'){
            if(computerMove=='Scissors'){
                alert("Lost");
                totalCounter++;
                totalMoves.innerHTML = "Total moves: " + totalCounter;
                computerScore++;
                computerScoreText.innerHTML = "Computer score: " + computerScore;
            } else {
                alert("Won")
                winCounter++;
                playerCount.innerHTML = "Player score: " + winCounter
                totalCounter++;
                totalMoves.innerHTML = "Total moves: " + totalCounter;
            }
        } else if (element=='Scissors'){
            if(computerMove=='Rock'){
                alert("Lost");
                totalCounter++;
                totalMoves.innerHTML = "Total moves: " + totalCounter;
                computerScore++;
                computerScoreText.innerHTML = "Computer score: " + computerScore;
            } else {
                alert("Won")
                winCounter++;
                playerCount.innerHTML = "Player score: " + winCounter
                totalCounter++;
                totalMoves.innerHTML = "Total moves: " + totalCounter;
            }
        }
    }
}
loadGame()
buttonPress()