# Borrow Something!
This project is a Django based website that allows users to register and request to borrow an item (e.g.: A lawnmower, paint stripper etc.) from someone nearby.  
Other users can view requests and choose to respond with details about what they are able to lend to the requester.  
The requester can then review responses and choose to accept or reject them.  
Once a borrowing has been completed, the lender can rate the borrower to let other users know if the borrowing went OK.  
The site can be viewed at [Heroku Deployment](https://borrow-something.herokuapp.com/)

# Table of Contents
- [Borrow Something!](#borrow-something)
- [Table of Contents](#table-of-contents)
- [Design](#design)
  - [User Stories](#user-stories)
  - [Site Wireframes](#site-wireframes)
    - [Index Page](#index-page)
- [Features](#features)
- [Testing](#testing)
- [Validation](#validation)
- [Deployment](#deployment)
  - [Prerequisites](#prerequisites)
  - [Instructions](#instructions)
- [Credits](#credits)

#  Design
## User Stories
- __As a user of the website I want to:__
  - Be able to sign up to the site.
    - After registering, login to the site with the same credentials on subsequent visits.
  - Manage requests to borrow something:
    - Create a new request, detailing:
      - What I want to borrow.
      - When I want to borrow it.
      - How long I want to borrow it for.
    - Accept responses to my requests to let the other user know I'd like to borrow their item.
    - Cancel my requests if I no longer need them.
  - View requests posted by other users.
  - Respond to requests from other users and let them know what I can lend them.
  - Rate a borrowing transaction so other users know if the requester is trustworthy.

## Site Wireframes
### Index Page
![Index Page Wireframe](readme-assets/site_layout_index.png)


# Features

# Testing

# Validation

# Deployment
## Prerequisites
- This project requires you to have [Python](https://www.python.org/) installed on your local PC.  
  - You will also need [pip](https://pip.pypa.io/en/stable/installation/) installed to allow installation of modules the application uses.  
- Generate a [Django secret key](https://miniwebtool.com/django-secret-key-generator/) 
## Instructions
- Create a local copy of the GitHub repository, by following one of the 2 processes below:
    - Download code:
        - Go to the [GitHub Repo](https://github.com/SiJiL82/borrow_something) page.
        - Click the `Code` button and download the ZIP file containing the project.
        - Extract the ZIP file to a location on your PC.
    - Clone the repository:
        - Open a terminal to the location you wish to run the application from.
        - Run the command `git clone https://github.com/SiJiL82/borrow_something.git`
- Create a new Python virtual environment:
  - `python3 -m venv venv`
  - `source venv/bin/activate`
- Install requirements:
  -  `pip3 install requirements.txt`
- Create .env file
  - Add steps here
- Create a [Heroku](https://www.heroku.com) account if you don't already have one.
- Create a new Heroku application
- Add environment variables to Heroku config vars:
  - Add steps here
- In a terminal inside your copy of the project repository:
  - Login to Heroku `heroku login`
  - Set Heroku as remote repository `heroku git:remote -a APP_NAME`
  - Push code to Heroku `git push heroku main`

# Credits