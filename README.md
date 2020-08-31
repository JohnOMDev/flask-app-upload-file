[![CircleCI](https://circleci.com/gh/JohnOMDev/flask-app-upload-file.svg?style=svg)](https://circleci.com/gh/JohnOMDev/flask-app-upload-file)


## Project Overview
This is a simple custom flask app for file upload to an API that accept post request with any payload format. The project directory contains app.py which is the main flask file, circle which contain config.yml file for CI/CD, Dockerfile for building docker image and requirement.txt for automatically installing all the depencies that works for the app.

## Project Tasks
Build a flask server with the following pages:
* Index page
* Uploader page where you can upload a file SMALLER THAN 1MB to an api
The API is hosted at https://patw1h5276.execute-api.eu-west-1.amazonaws.com/beta/upload and accepts POST requests only at the specified URL. The server must manage checking the file size and only send it if it's smaller than 1MB.

## Setup the Environment
* Create a virtualenv
* Activate a virtual environment
* Installing dependencies via project Makefile

##  Special Libraries must install before starting
* Docker - to Containerize your application
* Hadolint - to Lint the Dockerfile
* Virtual machine

### Running the project

1. Installing dependencies via project Makefile `make all`
2. Run the Docker file:  `./run_docker.sh`
3. Run the Upload docker file:  `./upload_docker.sh`
4. Standalone:  `python app.py`
5. Delete all the setup  `./delete.sh`

### Yet to be done
* pytest