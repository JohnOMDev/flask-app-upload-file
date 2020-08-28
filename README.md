## Project Overview
Build a flask server with the following pages:
Index page
Uploader page where you can upload a file SMALLER THAN 1MB to an api
The API is hosted at https://patw1h5276.execute-api.eu-west-1.amazonaws.com/beta/upload and accepts POST requests only at the specified URL.
The server must manage checking the file size and only send it if it's smaller than 1MB.

### Project Tasks

Your project goal is to operationalize this working, machine learning microservice using [kubernetes](https://kubernetes.io/), which is an open-source system for automating the management of containerized applications. In this project you will:
* Test your project code using linting
* Complete a Dockerfile to containerize this application
* Deploy your containerized application using Docker and make a prediction
* Improve the log statements in the source code for this application
* Configure Kubernetes and create a Kubernetes cluster
* Deploy a container using Kubernetes and make a prediction
* Upload a complete Github repo with CircleCI to indicate that your code has been tested


## Setup the Environment
*  Clone the project repository `git clone https://github.com/udacity/DevOps_Microservices.git`
* Create a virtualenv
* Activate a virtual environment
* Installing dependencies via project Makefile : using 'make install'
* Lint Project files with `make lint`

##  Special Libraries must install before starting
* Docker - to Containerize your application
* Hadolint - to Lint the Dockerfile
* Virtual machine
* Kubernetes
* Minikube

### Running the project

1. Standalone:  `python app.py`
2. Run the Docker file:  `./run_docker.sh`
4. Run the make prediction file  `make_prediction.sh`
5. Run the Upload docker file:  `./upload_docker.sh`
