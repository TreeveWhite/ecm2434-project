/* The following program renders and runs a Wordle like game but with only Computer Science related words.
The idea of the game is to guess certain words and correct letters in the right position change to green 
and correct letters in the wrong position change to yellow. From this you have to guess the word. You have
to do this within 6 tries. 
At the moment the player keeps trying to win and when they do they can claim the building. The end product will involve a score system.
*/ 
'use strict'
//This is the word list used, to be expanded for the full version
//answerList
let wordList = [
  'codes',
  'apple',
  'debug',
  'admin',
  'cache',
  'click',
  'email',
  'input',
  'logic',
  'mouse',
  'pixel',
  'queue',
  'reset',
  'robot',
  'abort',
  'write',
  'proxy',
  'micro',
  'lines',
  'https',
  'merge',
  'tests',
  'login',
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
 * This function initiates the grid on the page and adds a keyboard listener to the window
 */
function startGame(){
    buildGrid()
    createKeyboard()
    updateGrid()
    window.addEventListener('keypress', handleKeyDown)
    const wrapper = document.getElementById('keyboard-cont');
    wrapper.addEventListener('click', (event)=>{
      const isButton = event.target.nodeName === 'BUTTON';
      if (!isButton){
        return;
      }
      onScreenInput(event.target);
    })
}
function createKeyboard(){
  grid.innerHTML+="<div id='keyboard-cont'><div class='first-row'><button class='keyboard-button'>q</button><button class='keyboard-button'>w</button>"+
  "<button class='keyboard-button'>e</button>"+
      "<button class='keyboard-button'>r</button>"+
      "<button class='keyboard-button'>t</button>"+
      "<button class='keyboard-button'>y</button>"+
      "<button class='keyboard-button'>u</button>"+
      "<button class='keyboard-button'>i</button>"+
      "<button class='keyboard-button'>o</button>"+
      "<button class='keyboard-button'>p</button></div><div class='second-row'>"+
      "<button class='keyboard-button'>a</button>"+
      "<button class='keyboard-button'>s</button>"+
      "<button class='keyboard-button'>d</button>"+
      "<button class='keyboard-button'>f</button>"+
      "<button class='keyboard-button'>g</button>"+
      "<button class='keyboard-button'>h</button>"+
      "<button class='keyboard-button'>k</button>"+
      "<button class='keyboard-button'>l</button>"+
      "</div>"+
      "<div class='third-row'>"+
      "<button class='keyboard-button'>backspace</button>"+
      "<button class='keyboard-button'>z</button>"+
      "<button class='keyboard-button'>x</button>"+
      "<button class='keyboard-button'>c</button>"+
      "<button class='keyboard-button'>v</button>"+
      "<button class='keyboard-button'>b</button>"+
      "<button class='keyboard-button'>n</button>"+
      "<button class='keyboard-button'>m</button>"+
      "<button class='keyboard-button'>enter</button>"+
      "</div>",
    "</div>"
}

  


function onScreenInput(e){
  let letter = e.innerHTML
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
  } else if(letter.match(/[a-z]/gi)){
    if (letter.length==1){
      if (currentAttempt.length < 5){
        currentAttempt+=letter
      }
    }
  }
  updateGrid()
}
/**
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
  } else if(letter.match(/[a-z]/gi)){
    if (letter.length==1){
      if (currentAttempt.length < 5){
        currentAttempt+=letter
      }
    }
  }
  updateGrid()
}

/**
 * function checks if the user has had 6 attempts and still hasn't got the word
 */
function check_if_lost(){
  if (counter==6 && green_counter < 5) {
    alert("Game lost. The word was: " + secret +". The page will now reload.")
    location.reload();
  }
}

/**
 * Function builds 6 rows and 6 columns with DOM
 */
function buildGrid() {
  var paragraph = document.getElementById("gameText");
  paragraph.style.textAlign = "center";
  paragraph.innerHTML = "Please enter Computer Science related words until you get the correct answer. <br> Only then will you be able to claim the building.";

  for (let i = 0; i < 6; i++) {
    let row = document.createElement('div')
    for (let j = 0; j < 5; j++) {
      let cell = document.createElement('div');
      // cell.setAttribute("type", "text");
      // cell.style.color = "white"
      cell.className = 'cell'
      cell.textContent = ''
      row.appendChild(cell)
    }
    grid.appendChild(row)
  }
  //grid.appendChild(createKeyboard())
}

/**
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
      cell.textContent = ""
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