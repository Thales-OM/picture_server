# Image Display Website

## Overview
This project is a web server that displays images on a stylish website. It utilizes Docker to create a seamless environment for serving images, making it easy to deploy and manage.

## Prerequisites
- Docker
- Docker Compose

## Installation
- Clone this repository or download the project files to your local machine.
- Navigate to the directory where the docker-compose.yml file is located.

## Building and Running the Application
- To build and run the web server, execute the following command:
```bash
docker-compose up --build
```
This command will build the containers as specified in the docker-compose.yml file and start the services.

## Accessing the Application
Once the application is running, you can access it via your web browser:
- Production Server: http://localhost
- Test Server: http://localhost:8000

## Stopping the Application
To stop the running containers, you can use the following command:
```bash
docker-compose down
```
