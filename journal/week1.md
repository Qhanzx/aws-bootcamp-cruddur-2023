# Week 1 — App Containerization
Ran 'python3 -m flask run --host=0.0.0.0 --port=4567' on the backend-flask folder

Ran 'npm i' on th efrontend-react-js folder
![image]https://github.com/Qhanzx/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1/npm.PNG

Pushed and tag image on Dockerhub by building the image and running from my local machine
![image] https://github.com/Qhanzx/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1/Docker%20hub.PNG

The multistage dockerfile buid was done with th edocker-compose.yml file and composed up

Tried this code for healthcheck in the Docker compose file:
healthcheck:
      test: curl --fail http://localhost || exit 1
      interval: 60s
      retries: 5
      start_period: 20s
      timeout: 10s
      
Some of the best practices found and implemented:
Create ephemeral containers
Pipe Dockerfile through stdin
Use multi-stage builds


used 'docker build -t getting-started .' to build container 
Ran it with 'docker run -d -p 80:80 docker/getting-started'
![image] https://github.com/Qhanzx/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1/Docker%20local%20Machine.PNG

Launched an EC2 instance and updated the installed package with
sudo yum update -y

Installed most recent Docker engine with
sudo amazon-linux-extras-install docker
![image] https://github.com/Qhanzx/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1/aws-docker.PNG

Started docker service
sudo service docker start

add user to docker group with
sudo usermod -a -G docker user

verify user is added 
docker info

Created a Dockerfile and built a Docker image with
docker build -t hello-world .
docker run -tip 80:80 hello-world

Documented the notification endpoint for openAI document
Wrote a Flask backend endpoint for notification
Wrote a react page for Notification
Ran the DynamoDB local container and it worked creating a folder in the main
Ran Postgres container and added a connection using the database explorer
