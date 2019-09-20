# iReporter-2
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.

[![Build Status](https://travis-ci.org/e-ian/iReporter-2.svg?branch=ch_test_edge_cases)](https://travis-ci.org/e-ian/iReporter-2)
[![Coverage Status](https://coveralls.io/repos/github/e-ian/iReporter-2/badge.svg?branch=ft_challenge_3)](https://coveralls.io/github/e-ian/iReporter-2?branch=ft_challenge_3)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c9c629399bf34ec6bd998d28fb6a55d3)](https://www.codacy.com/app/e-ian/iReporter-2?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=e-ian/iReporter-2&amp;utm_campaign=Badge_Grade)
## Getting started.
These instructions will help you set and run the application on your local machine.

## Prerequisites
The following are required to enable you get started!

* Serverside Framework: Flask Python Framework
* Testing Framework: Pytest
* API development environment: Postman
* GIT
* IDE/Text editor(Vs Code preferred)
* Python 3.6

# Project links:

## User interface:
* The project user interface pages are hosted on gh-pages and can be accessed on this link: (https://e-ian.github.io/iReporter/UI/index.html)
* The code for the UI templates can be accessed using this link: (https://github.com/e-ian/iReporter/tree/gh-pages/UI)

## API endpoints:
* The code for the endpoints can be accessed using this link: (https://github.com/e-ian/iReporter-2/tree/develop)

# Installation:
* Clone the remote repository to your local machine using this command:

``` git clone https://github.com/e-ian/iReporter-2.git ```

* Create a virtual environment.

``` virtualenv venv ```

* Activate your virtual environment.

``` venv\Scripts\activate ```

* Install dependencies.
To install all required dependencies for the project, use the command:

``` pip install -r requirements.txt ```

* Install Postman

# Project features/ functionality

## Interface
* Users can create an account and log in.
* Users can create a ​red-flag ​record (An incident linked to corruption).
* Users can create ​intervention​ record​ ​(a call for a government agency to intervene e.g
repair bad road sections, collapsed bridges, flooding e.t.c).
* Users can edit their ​red-flag ​or ​intervention ​records.
* Users can delete their ​red-flag ​or ​intervention ​records.
* Users can add geolocation (Lat Long Coordinates) to their ​red-flag ​or ​intervention
records​.
* Users can change the geolocation (Lat Long Coordinates) attached to their ​red-flag ​or
intervention ​records​.
* Admin can change the ​status​ of a record to either ​under investigation, rejected ​(in the
event of a false claim)​ ​or​ resolved ​(in the event that the claim has been investigated and
resolved)

## API Endpoints

|Method | Route | Functionality|
|-------|:-----:|-------------:|
|GET| "api/v1/redflags" | Fetches all redflags |
|GET| "api/v1/redflags/<int:flagid>" | Fetches a specific redflag |
|POST| "api/v1/redflags" | Creates a redflag |
|PATCH| "api/v1/redflags/<int:flagid>/location" | Edits the location of a redflag|
|PATCH| "api/v1/redflags/<int:flagid>/comment" | Edits the comment of a redflag|
|DELETE| "api/v1/redflags/<int:flagid>" | Delete a specific redflag record |

* The above endpoints have the same functionality as interventions, you have to change the routes to "api/v1/interventions" and follow through like in the redflags

# Running unittests.

* Install pytest from terminal

    `pip install pytest`

* Test your endpoints in the terminal

    `pytest tests/test_api.py`

* To run tests and get coverage report

    `pytest tests --cov=api --cov-report term-missing`

## Postman data should be in this format

    ``` creating a redflag
    {
    "incident_type" : "redflag",
    "location" : "ntinda",
    "status" : "resolved",
    "image" : "image",
    "comment" : "corruption"} ```

# To run the API, type the command:

``` python run.py ```

# Deployment

The app has been hosted on heroku and can be accessed using the following link (https://eian-ireporter.herokuapp.com/)

# Author:

Emmanuel Ogwal
