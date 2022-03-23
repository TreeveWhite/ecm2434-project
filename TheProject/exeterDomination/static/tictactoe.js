//getting the grid from gamePage.html by Id
let grid = document.getElementById('grid');

//Getting a paragraph from gamePage.html by Id and editing the text
var paragraph = document.getElementById("gameText");
paragraph.innerHTML = "Defeat our TicTacToe Bot!";

//Adding in the 3x3 board into the grid div along with css for styling
grid.innerHTML+="<div class='Game ticTacToeGrid'>"+
        "<div id='0' class='Cell ticTacToeBox' cellIndex='0'></div>"+
        "<div id='1' class='Cell ticTacToeBox' cellIndex='1'></div>"+
        "<div id='2' class='Cell ticTacToeBox' cellIndex='2'></div>"+
        "<div id='3' class='Cell ticTacToeBox' cellIndex='3'></div>"+
        "<div id='4' class='Cell ticTacToeBox' cellIndex='4'></div>"+
        "<div id='5' class='Cell ticTacToeBox' cellIndex='5'></div>"+
        "<div id='6' class='Cell ticTacToeBox' cellIndex='6'></div>"+
        "<div id='7' class='Cell ticTacToeBox' cellIndex='7'></div>"+
        "<div id='8' class='Cell ticTacToeBox' cellIndex='8'></div>"+
    "</div>";

//If any of the cells on the board are clicked a function is called as long as that
//cell is not oppcupied
document.querySelectorAll('.Cell').forEach(Cell => Cell.addEventListener('click', handleCellClick));

//Boolean to declare if the game is still being played
let gameActive = true;

//Character to determine which player's move it currently is
let currentPlayer = "X";

//The current state of the board - which character has played in which cell
let gameState = ["", "", "", "", "", "", "", "", ""];

//an array to determine wether the bot has blocked a combination of cells
//to stop the player from winning
let winningBlocked = [
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false
];

/**
 * Changes the current game state to where the player has made a move and
 * displays this on screen
 * @param {*} clickedCell 
 * @param {*} clickedCellIndex 
 */
function handleCellPlayed(clickedCell, clickedCellIndex) {
    gameState[clickedCellIndex] = "X";
    clickedCell.innerHTML = "X";
}

/**
 * Changes the current player making the move
 */
function handlePlayerChange() {
    if (currentPlayer == "X") {
        currentPlayer = "O";
    } else if (currentPlayer == "O") {
        currentPlayer = "X";
    }
}

/**
 * Checks if there is a winning combination
 * if there is the game ends and displays who has won
 * else the game proceeds
 * @returns 
 */
function handleResultValidation() {
    //A 2D array with the combination of cells that can win a game
    const winningConditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ];
    let roundWon = false;
    //iterates through 8 times as this is the number of combinations a player use to win
    for (let i = 0; i <= 7; i++) {
        var a = gameState[winningConditions[i][0]];
        var b = gameState[winningConditions[i][1]];
        var c = gameState[winningConditions[i][2]];
        //if any cell is blank continue
        if (a === '' || b === '' || c === '') {
            continue;
        }
        //if all cells are equal a player has won
        if (a === b && b === c) {
            if (currentPlayer == "X") {
                roundWon = true;
                gameActive = false;
                alert("You have won!");
                document.getElementById('isGameWon').checked = true;
                break;
            } else {
                gameActive = false;
                alert("You have lost better luck next time!");
                location.reload();
                break;
            }
            
        }
    }
    //game is no longer in process if a player has won
    if (roundWon) {
        gameActive = false;
        return;
    }

    //if all cells have been used the game ends in a draw
    let roundDraw = !gameState.includes("");
    if (roundDraw && gameActive) {
        alert("Game has ended a draw");
        location.reload();
        gameActive = false;
        return;
    }
    handlePlayerChange();
}

/**
 * function is called if a cell is clicked
 * changes who owns that cell and calls a function for the bot to make a move
 * @param {*} clickedCellEvent 
 * @returns 
 */
function handleCellClick(clickedCellEvent) {
    const clickedCell = clickedCellEvent.target;
    const clickedCellIndex = parseInt(clickedCell.getAttribute('cellIndex'));

    if (gameState[clickedCellIndex] !== "" || !gameActive) {
        return;
    }

    handleCellPlayed(clickedCell, clickedCellIndex);
    handleResultValidation();
    if (gameActive) {
        computerMakeMove(grid);
    }
}

/**
 * function to make the bot choose a cell
 * it will either block a winning combination from the other player
 * choose a cell in order to win
 * if none of the above are an option choose a random cell
 */
function computerMakeMove() {
    //A 2D array with the combination of cells that can win a game
    const winningConditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ];
    let moveMade = false;
      //iterates through 8 times as this is the number of combinations a player use to win
    for (let i = 0; i <= 7; i++) {
        let a = gameState[winningConditions[i][0]];
        let b = gameState[winningConditions[i][1]];
        let c = gameState[winningConditions[i][2]];
        //first checks if a move can be made for the bot to win
        if (a == b && a == "O" && c == "") {
            gameState[winningConditions[i][2]] = "O";
            document.getElementById(winningConditions[i][2]).innerHTML = "O";
            moveMade = true;
            break;
        }
        if (a == c && a == "O" && b == "") {
            gameState[winningConditions[i][1]] = "O";
            document.getElementById(winningConditions[i][1]).innerHTML = "O";
            moveMade = true;
            break;
        }
        if (b == c && b == "O" && a == "") {
            gameState[winningConditions[i][0]] = "O";
            document.getElementById(winningConditions[i][0]).innerHTML = "O";
            moveMade = true;
            break;
        }  
    }
      //iterates through 8 times as this is the number of combinations a player use to win
    for (let i = 0; i <= 7; i++) {
        let a = gameState[winningConditions[i][0]];
        let b = gameState[winningConditions[i][1]];
        let c = gameState[winningConditions[i][2]];
        //then checks if the player will win in its next move to block
        if (a == b && a == "X" && c == "") {
            if (winningBlocked[i] == false) {
                winningBlocked[i] = true;
                gameState[winningConditions[i][2]] = "O";
                document.getElementById(winningConditions[i][2]).innerHTML = "O";
                moveMade = true;
                break;
            }
        }
        if (a == c && c == "X" && b == "") {
            if (winningBlocked[i] == false) {
                winningBlocked[i] = true;
                gameState[winningConditions[i][1]] = "O";
                document.getElementById(winningConditions[i][1]).innerHTML = "O";
                moveMade = true;
                break;
            }
        }
        if (b == c && b == "X" && a == "") {
            if (winningBlocked[i] == false) {
                winningBlocked[i] = true;
                gameState[winningConditions[i][0]] = "O";
                document.getElementById(winningConditions[i][0]).innerHTML = "O";
                moveMade = true;
                break;
            }
        }
    }
    //otherwise make a random move
    if (!moveMade) {
        let index = Math.floor(Math.random() * 9)
        if (gameState.includes("")) {
            while (gameState[index] != "") {
                index = Math.floor(Math.random() * 9);
            }
            gameState[index] = "O";
            document.getElementById(index).innerHTML = "O";
        }
    }
    //check if the bot has won
    handleResultValidation();
}