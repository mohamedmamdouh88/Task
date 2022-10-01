# Task

Nodejs App with container workflow:

    1- Make changes to the application source code.
    2- The code change is committed to a GitHub repository.
    3- Start the continuous integration (CI) process, a GitHub webhook triggers a Jenkins project build.
    4- The Jenkins build job uses a Docker agent to perform a container build process.
    5- A container image is created from the code in source control and is then pushed to an DockerHub Container Registry.
    6- Using the process of continuous deployment (CD), Jenkins deploys an updated container image to the Kubernetes cluster.
