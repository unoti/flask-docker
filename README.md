# Flask_docker
Experiment to get a minimal web app running with Flask and Docker.

## Contents
This project contains the following folders:
* **Web**. Back Flask app for getting started with docker.
   * This is a basic flask app, based on on ChloeCodesThings [github chloe_flask_docker_demo](https://github.com/ChloeCodesThings/chloe_flask_docker_demo/tree/master/web).  It's great for getting started, but has a few important shortcomings:
   * Builds a very fat docker image
   * Not suited for quick iterative development, and doesn't talk about getting a local sql server going.
* **Iterative**. More advanced setup overcoming the above shortcomings based on the Hackernoon Blob Post above [efficient development with docker and docker compose](https://hackernoon.com/efficient-development-with-docker-and-docker-compose-e354b4d24831).

# Web

## Operations
Here's how to do basic things without using ```docker compose```.

 * **Build docker image**
    ```
    docker build -t flask-sample:latest .
    ```
 * **Run container**
    ```
    docker run -d -p 5000:5000 flask-sample
    ```
 * **Determine what's running**
    ```
    docker ps -a
    ```
 * **See stdout**
    1. Determine the name of the service using ```docker ps -a``` and look at NAMES column
    2. View logs:
        ```
        docker logs {service_name}
        ```
The real way to run it is with ```docker-compose```:
   Run it with the last image.  This will only build the docker image if it doesn't yet exist:
   ```
   docker-compose up
   ```

   Rebuild and run:
   ```
   docker-compose up --build
   ```


# Iterative
This section is based on this HackerNoon [blog post](https://hackernoon.com/efficient-development-with-docker-and-docker-compose-e354b4d24831) using this [github code](https://github.com/larsderidder/docker-compose-development-env).

We'll have local environments used for development, and remote environments (test and prod) where we'll deploy.  Setup for these is composed as follows:
   * **docker-compose.common.yml** Contains setup common to both the local environment and remote environments.



## FAQ
* When I started my flask app, it exited.  I can tell because ```docker ps -a``` shows that ```python app.py``` immediately exited.  How can I see what the problem was?
   * ```docker logs {service_name}```
   * [Docker docs: View logs for a container or service](https://docs.docker.com/config/containers/logging/)
* When I do a ```docker build``` and ```docker run```, where does it store the image and retrieve the image?
   * Commands for working with images:
      * ```docker``` lists commands, and many relate to images:
      * ```docker images``` lists images
      * ```docker rmi {image}``` removes an image
* What's the deal with docker compose?

## Next steps
 * Meaning of the ports and other flags
 * Convert command line flags to long ```--``` versions
 * **Pare down image**.  That docker image is massive, and includes a a full Ubuntu and zillion things that I don't need, such as the entire world of perl, gcc, and countless other things.  Take a look at this blog post regarding [Building minimal python docker images](https://blog.realkinetic.com/building-minimal-docker-containers-for-python-applications-37d0272c52f3).
 * Convert from Python 2.7 to Python 3
 * **Fast iterative development**.  Make it so that we don't need to build a new docker file for every file change. Auto-detect changes during development.  Use a local sql during development, but cloud-hosted managed sql in production.
   * See this blog post on [Efficient development with docker and docker compose](https://hackernoon.com/efficient-development-with-docker-and-docker-compose-e354b4d24831) as a starting point.

## References
 * [Blog: Hello Whale: Docker + Flask](https://codefresh.io/docker-tutorial/hello-whale-getting-started-docker-flask/)
  * ChloeCodesThings [github chloe_flask_docker_demo](https://github.com/ChloeCodesThings/chloe_flask_docker_demo/tree/master/web) which I brazenly stole from
  * HackerNoon [Efficient development with Docker and Docker-Compose](https://hackernoon.com/efficient-development-with-docker-and-docker-compose-e354b4d24831)