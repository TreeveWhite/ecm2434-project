# GROUP SOFTWARE ENGINEERING PROJECT GROUP 1 - EXETER DOMINATION

# The Idea

Exeter Domination is a fun, interactive game which encourages exploration and interactivity on the beautiful Streatham Campus. Walk (or run!) around campus and go to different buildings, then play a fun game and try to be the first to capture the point. Once you have captured it other players can try to take the building off of you. Your strategy is up to you; either stay and fight to maintain control, or leave and take control of another building. In the final version, the aim will be to take control of as much as campus as possible with a constantly updating scoreboard.

# Prerequisites
You need to install the following software and packages in order to run our software, depending on what you want to do. Here, we have included details for using our live site, deploying to Digital Ocean and also deploying to localhost.

# Using our site
The easiest thing to do is use our site as it is. It is live at https://exeterdomination.live and the instructions on how to run the page can be found below.

# Deploying to Digital Ocean

To deploy to Digital Ocean you first need the correct file structure for Digital Ocean. This can be found by cloning the latest deployment branch from the GitHub repository. The instructions for cloning are below. You should then follow the software and package installation instructions, then finally follow their documentation to guide you through their deployment.

## Software to install
- Python version 3.7 and above. The download can be found on the Download section on https://www.python.org
- PostgreSQL - The download can be found at https://www.postgresql.org/. Follow the steps on the launcher and when in the application there a couple of requirements. First, any passwords set need to be set to the same password as the one set in settings.py. You then need to make a database called exeterDomination (or whatever is set in settings.py)
- Mozille Firefox - this is used to run the testing. This can be found at https://www.mozilla.org/en-GB/firefox/new/
- Geckdriver version 30- this is used in the testing and can be found at https://github.com/mozilla/geckodriver/releases with all releases for each system. Once installed, if the installation is compressed, double-click it and decompress it so that the executable file is available.
 ## Packages to install

The packages can be installed easily by cloning the deployment branch into your desired directory (follow the instructions below) and then going into the new subdirectory which contains 'requirements.txt'. You can then enter the following command into the terminal:
```
pip install requirements.txt
```

# Deploying to localhost
 To deploy to localhost you first need the correct file structure. This can be found by cloning the main branch from the GitHib repository. The instructions for cloning are below

## Software to install
- Python version 3.7 and above. The download can be found on the Download section on https://www.python.org
- PostgreSQL - The download can be found at https://www.postgresql.org/. Follow the steps on the launcher and when in the application there a couple of requirements. First, any passwords set need to be set to the same password as the one set in settings.py. You then need to make a database called exeterDomination (or whatever is set in settings.py)
- Mozille Firefox - this is used to run the testing. This can be found at https://www.mozilla.org/en-GB/firefox/new/
- Geckdriver version 30- this is used in the testing and can be found at https://github.com/mozilla/geckodriver/releases with all releases for each system. Once installed, if the installation is compressed, double-click it and decompress it so that the executable file is available.
 ## Packages to install

The packages can be installed easily by cloning the main branch into your desired directory (follow the instructions below) and then going into the new subdirectory which contains 'requirements.txt'. You can then enter the following command into the terminal:
```
pip install requirements.txt
```

## Deployment

To deploy the code follow these steps:
1. Go to your command line application based on your machine and navigate to the cloned directory
2. Type the following command to change into the necessary subdirectory
```
cd TheProject
```
3. Type the following command to create the migrations of the changes
```
python manage.py makemigrations
```
4. Type the following command to initiate the migration changes
```
python manage.py migrate
```
5. Populate the database with location and coordinate data by typing the following commands in the required order
```
python manage.py loaddata coordinates
```
then
```
python manage.py loaddata locations
```
## Starting the application

To start the application stay in the directory where the commands above were typed, the enter the following command:
```
python manage.py runserver
```
The server will start and a localhost link will be shown. Copy this and enter the link into your desired browser which will take you onto the home page.


# Cloning the code
To install the code onto your machine you need to use your terminal. This depends on the system:

Windows:
1. Open Git Bash
2. Change the working directory to the desired location where you want the cloned directory to be made
3. Use the command below and press enter
```
$ git clone https://github.com/TreeveWhite/ecm2434-project.git
```
OS X and Linux:
1. Open Terminal
2. Change the working directory to the desired location where you want the cloned directory to be made
3. Use the command below and press enter
```
$ git clone https://github.com/TreeveWhite/ecm2434-project.git
```
Or using an IDE:
1. Navigate to your desired IDEs Version Control tab
2. Go to Git > Clone
3. Use the link shown below to clone the repository
```
https://github.com/TreeveWhite/ecm2434-project.git
```

# How to play Exeter Domination

## Logging in / Signing up
When you first load up the website (through any method described above) you will be taken to the homepage. Navigate to the navigation bar at the top and select log in/sign up depending on if you are a pre-existing user or not. Here you can enter new/existing credentials as well as create a team or join an existing one. You can then enter the site (you can also do all of this as an admin or superuser).

## Playing your first game and capturing a building

When you have followed the above steps you should be on the game page. Here you can play one of three games, where if you win you can capture the building on campus where you currently are. The games are Codle (a Wordle inspired game with only Computer Science related words), Rock Paper Scissors and Tic Tac Toe. Once you have captured a building navigate to the leaderboard or locations page which can be found in the navigation bar at the top.

## Leaderboard and Locations
The leaderboard page shows you how much of campus is claimed. You can choose between people and teams and the site will then show who owns what percentage. You can then navigate to the Locations page. Here you can see a 3D map of campus, where certain buildings have a marker which says the location name and who is currently claiming that building.

## About Page
This page contains all of the details about the project as well as the Privacy Policy and GDPR compliance.

## Types of users


# Testing
To run the tests enter the directory in which the django commands were typed above. It should be along the lines of /ecm2434-project/TheProject.
## Testing Prerequisites
The software is linked above but you need to ensure that Firefox, Selenium and Geckodriver are all installed. 
## Running the tests
Once all of the prerequisites are met then enter the following command:
```
python manage.py test
```
If the prerequisites are followed correctly then the tests will pass.

# Authors
- Treeve White
- Ethan Gallagher
- Dan Owen
- Faris Kapes
- Rory Smith
- Tom Osmond

This project was conducted as part of the ECM2434 Group Software Engineering Project module at the University of Exeter.

# License
 MIT License Copyright (c) 2022 Ethan Gallagher, Rory Smith, Treeve White, Faris Kapes, Dan Owen, Tom Osmond. Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
