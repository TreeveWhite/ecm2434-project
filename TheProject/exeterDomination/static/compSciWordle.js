'use strict'

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
let randomIndex = Math.floor(Math.random() * wordList.length)
let secret = wordList[randomIndex]

let currentAttempt = ''
let counter = 0
let green_counter = 0
let history = []
let score = 0
function startGame(){
    let grid = document.getElementById('grid')
    buildGrid()
    updateGrid()
    window.addEventListener('keydown', handleKeyDown)
}
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

function check_if_lost(){
  if (counter==6) {
    alert("Game lost, please restart")
  }
}
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


function updateGrid() {
  let row = grid.firstChild
  for (let attempt of history) {
    drawAttempt(row, attempt, false)
    row = row.nextSibling
  }
  drawAttempt(row, currentAttempt, true)
}

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
  if (green_counter==5){
    document.getElementById('claimButton').disabled = false;
  } else {
    green_counter=0
  }
}

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

let restartBtn = document.createElement('button');
restartBtn.id='restart';
restartBtn.innerHTML = "Restart"
restartBtn.addEventListener("click", function restartGame(){
    location.reload();
});
grid.append(restartBtn);

