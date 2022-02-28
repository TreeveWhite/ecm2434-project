/* The following program renders and runs a Wordle like game but with only Computer Science related words.
The idea of the game is to guess certain words and correct letters in the right position change to green 
and correct letters in the wrong position change to yellow. From this you have to guess the word. You have
to do this within 6 tries. 
At the moment the player keeps trying to win and when they do they can claim the building. The end product will involve a score system.
*/ 
'use strict'
//This is the word list used, to be expanded for the full version
let wordList = [
  'codes',
  'apple',
  'cache',
  'ascii',
  'click',
  'debug',
  'email',
  'input',
  'intel',
  'logic',
  'macro',
  'modem',
  'octal',
  'pixel',
  'query',
  'stack',
  'virus',
  'robot',
  'cable',
  'hacks',
  'buggy',
  'agile',
  'cloud',
  'cyber',
];
//selection of a random word
let randomIndex = Math.floor(Math.random() * wordList.length) 
let secret = wordList[randomIndex]

let currentAttempt = ''
let counter = 0
let green_counter = 0
let history = []
let score = 0
/**
 * @author Ethan Gallagher
 * This function initiates the grid on the page and adds a keyboard listener to the window
 */
function startGame(){
    let grid = document.getElementById('grid')
    buildGrid()
    updateGrid()
    window.addEventListener('keydown', handleKeyDown)
}
/**
 * @author Ethan Gallagher
 * @param {event} e the key pressed by the user
 * @returns null if the user presses enter before the word is finished or the word isn't in the word list
 * Checks which key is pressed and if its a letter enters it onto the grid
 * If the letter is enter or backspace then the word is checked or a letter is deleted respectively
 */
function handleKeyDown(e) {
  let letter = e.key.toLowerCase()
  if (letter === 'enter') {
    if (currentAttempt.length < 5) {
      return
    }
    if (!wordList.includes(currentAttempt)) {
      alert('Not in the word list')
      return
    }
    history.push(currentAttempt)
    counter+=1
    this.check_if_lost()
    currentAttempt = ''
  } else if (letter === 'backspace') {
    currentAttempt = currentAttempt.slice(0, currentAttempt.length - 1)
    updateGrid()
    //#region 
  } else if (letter === 'a') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 'b') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 'c') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 'd') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 'e') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 'f') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 'g') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 'h') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 'i') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 'j') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 'k') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 'l') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 'm') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 'n') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 'o') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 'p') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 'q') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 'r') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 's') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 't') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 'u') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 'v') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 'w') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 'x') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 'y') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  else if (letter === 'z') {
    if (currentAttempt.length < 5) {
      currentAttempt += letter
    }
  }
  //#endregion
  updateGrid()
}

/**
 * @author Ethan Gallagher
 * function checks if the user has had 6 attempts and still hasn't got the word
 */
function check_if_lost(){
  if (counter==6 && green_counter < 5) {
    alert("Game lost, please restart")
  }
}

/**
 * @author Ethan Gallagher
 * Function builds 6 rows and 6 columns with DOM
 */
function buildGrid() {
  for (let i = 0; i < 6; i++) {
    let row = document.createElement('div')
    for (let j = 0; j < 5; j++) {
      let cell = document.createElement('div')
      cell.className = 'cell'
      cell.textContent = ''
      row.appendChild(cell)
    }
    grid.appendChild(row)
  }
}

/**
 * @author Ethan Gallagher
 * Function puts the word onto the grid
 */
function updateGrid() {
  let row = grid.firstChild
  for (let attempt of history) {
    drawAttempt(row, attempt, false)
    row = row.nextSibling
  }
  drawAttempt(row, currentAttempt, true)
}

/**
 * @author Ethan Gallagher
 * @param {DOM Element} row the row being drawn
 * @param {String} attempt the string guessed
 * @param {Boolean} isCurrent checks whether the user is still guessing or the guess has finished
 * Function that puts the letters into each cell and also calls for the cells to be checked when a word is guessed
 */
function drawAttempt(row, attempt, isCurrent) {
  for (let i = 0; i < 5; i++) {
    let cell = row.children[i]
    if (attempt[i] !== undefined) {
      cell.textContent = attempt[i]
    } else {
    }
    if (isCurrent) {
      cell.style.backgroundColor = '#111'
    } else {
      cell.style.backgroundColor = getBgColor(attempt, i)
    }
  }
  //If statement to check if each letter is completely correct and if it is then the claim building button is enabled
  if (green_counter==5){
    document.getElementById('claimButton').disabled = false;
  } else {
    green_counter=0
  }
}

/**
 * @author Ethan Gallagher
 * @param {String} attempt the word being checked
 * @param {String} i the index letter guess of the word
 * @returns different colour codes for the cells to change to
 *          based on how correct the guess is
 * This function determines the color of the cell after a guess
 */
function getBgColor(attempt, i) {
  let correctLetter = secret[i]
  let attemptLetter = attempt[i]
  if (
    attemptLetter === undefined ||
    secret.indexOf(attemptLetter) === -1
  ) {
    return '#212121'
  }
  if (correctLetter === attemptLetter) {
    green_counter+=1
    return '#538d4e'
  }
  return '#b59f3b'
}


startGame();

//this section creates the restart button which reloads the window
let restartBtn = document.createElement('button');
restartBtn.id='restart';
restartBtn.innerHTML = "Restart"
restartBtn.addEventListener("click", function restartGame(){
    location.reload();
});
grid.append(restartBtn);

