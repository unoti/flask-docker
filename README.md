# Flask_docker
Experiment to get a minimal web app running with Flask and Docker.

## Operations
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

## FAQ
* When I started my flask app, it exited.  I can tell because ```docker ps -a``` shows that ```python app.py``` immediately exited.  How can I see what the problem was?
* [Docker docs: View logs for a container or service](https://docs.docker.com/config/containers/logging/)
* When I do a ```docker build``` and ```docker run```, where does it store the image and retrieve the image?

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