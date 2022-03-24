//The array of the game files
var jsFiles = ['/static/compSciWordle.js', '/static/rockPaperScissors.js', '/static/tictactoe.js']
var index = Math.floor(Math.random()*jsFiles.length);
var script = document.createElement('script');
//Creates new script with the random source
script.src = jsFiles[index];
//Appends the HTML container with the random script source
document.getElementById('gameContainer').appendChild(script)