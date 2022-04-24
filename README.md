# Borrow Something!
This project is a Django based website that allows users to register and request to borrow an item (e.g.: A lawnmower, paint stripper etc.) from someone nearby.  
Other users can view requests and choose to respond with details about what they are able to lend to the requester.  
The requester can then review responses and choose to accept or reject them.  
Once a borrowing has been completed, the lender can rate the borrower to let other users know if the borrowing went OK.  
The site can be viewed at [Heroku Deployment](https://borrow-something.herokuapp.com/)

## Table of Contents
* [Design](#design)
* [Features](#features)
* [Testing](#testing)
* [Validation](#validation)
* [Deployment](#deployment)
* [Credits](#credits)
## Deployment
- Clone the repository
- Create a new Python virtual environment:
  - `python3 -m venv venv`
  - `source venv/bin/activate`
- Install requirements:
  -  `pip3 install requirements.txt`
-  Create .env file
  -  Add steps here
-  Login to Heroku `heroku login`
-  Create Heroku app 
   -  Add steps
-  Set Heroku as remote repository `heroku git:remote -a APP_NAME`
-  Push code to Heroku `git push heroku main`