This project is Assignment-5, where a Flask backend and a Node.js (Express) frontend work together using Docker and Docker Compose.
The Flask backend handles form submissions and stores the data in MongoDB Atlas, while the Node.js frontend displays the form and sends data to the backend using Axios.

Both services are fully containerized using individual Dockerfiles and are connected on a single network using docker-compose.yml.
The code follows a clean folder structure with separate backend and frontend directories for better organization.

Docker Hub images for this project:
Backend Image → https://hub.docker.com/r/siddhi002/assignment-5-docker

Frontend Image → https://hub.docker.com/r/siddhi002/assignment-5-docker

This assignment includes complete setup, containerization, networking, and deployment of both services.
