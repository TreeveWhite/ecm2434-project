var jsFiles = ['/static/compSciWordle.js', '/static/rockPaperScissors.js', '/static/tictactoe.js']
var index = Math.floor(Math.random()*jsFiles.length);
var script = document.createElement('script');
script.src = jsFiles[index];
document.getElementById('gameContainer').appendChild(script)