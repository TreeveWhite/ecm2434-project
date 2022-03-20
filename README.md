# GROUP SOFTWARE ENGINEERING PROJECT GROUP 1 - EXETER DOMINATION
# SPRINT 2

Note from faris:
    Make it clear that adding a user to the Game Masters group automatically adds them to staff, and removing them from the Game Masters group will automatically remove them from the staff.



# SPRINT 1

# The Idea

Exeter Domination is a fun, interactive game which encourages exploration and interactivity on the beautiful Streatham Campus. Walk (or run!) around campus and go to different buildings, then play a fun game and try to be the first to capture the point. Once you have captured it other players can try to take the building off of you. Your strategy is up to you; either stay and fight to maintain control, or leave and take control of another building. In the final version, the aim will be to take control of as much as campus as possible with a constantly updating scoreboard.

# Prerequisites
You need to install the following software and packages in order to run our software

## Software to install
- Python version 3.7 and above. The download can be found on the Download section on https://www.python.org
- PostgreSQL - The download can be found at https://www.postgresql.org/. Follow the steps on the launcher and when in the application there a couple of requirements. First, any passwords set need to be set to the same password as the one set in settings.py. You then need to make a database called exeterDomination (or whatever is set in settings.py)
- Mozille Firefox - this is used to run the testing. This can be found at https://www.mozilla.org/en-GB/firefox/new/
- Geckdriver version 30- this is used in the testing and can be found at https://github.com/mozilla/geckodriver/releases with all releases for each system. Once installed, if the installation is compressed, double-click it and decompress it so that the executable file is available.
 ## Packages to install
- Django - to install this go to your command prompt and enter :
```
pip install django
```
- psycopg2 - to install this go to your command prompt and enter :
```
pip install psycopg2
```
- On Macs you may need to install the binary version which can be done by entering the following into the command prompt:
```
pip install psycopg2-binary
```
- Selenium - to install this go to your command prompt and enter the following:
```
pip install selenium
```

# How to install and deploy
## Installation
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

## How to play Exeter Domination

When you have followed the above steps you should be on the homepage.
From here you can either log in or sign-up depending on whether or not you are an existing user with the links in the top right corner
In the current version, click the Play button and it will take you to the Game Page. Here, you can play 'Codle', a Wordle inspired game where you can guess Computer Science related words. Once you beat the game you can claim the building where you are located. 

# Testing
To run the tests enter the directory in which the django commands were typed above. It should be along the lines of /ecm2434-project/TheProject.
## Testing Prerequisites
The software is linked above but you need to ensure that Firefox, Selenium and Geckodriver are all installed. In the test_integrationWithSelenium.py file you need to change the pathToGeckoDriver variable to the path where your Geckodriver executable is.
## Running the tests
Once all of the prerequisites are met then enter the following command:
```
python manage.py test
```
All the tests should pass at the moment.

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
