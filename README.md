## Project Overview
Build a flask server with the following pages:
Index page
Uploader page where you can upload a file SMALLER THAN 1MB to an api
The API is hosted at https://patw1h5276.execute-api.eu-west-1.amazonaws.com/beta/upload and accepts POST requests only at the specified URL.
The server must manage checking the file size and only send it if it's smaller than 1MB.

### Project Tasks



## Setup the Environment
* Create a virtualenv
* Activate a virtual environment
* Installing dependencies via project Makefile : using 'make all'

##  Special Libraries must install before starting
* Docker - to Containerize your application
* Hadolint - to Lint the Dockerfile
* Virtual machine

### Running the project

1. Standalone:  `python app.py`
