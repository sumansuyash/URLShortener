
A simple URL shortener built with [Flask](http://flask.pocoo.org/), [Pandas](https://pandas.pydata.org/) and [Docker](https://www.docker.com/). The CI pipeline, GitHub workflow uses Docker Image CI to generate the docker image and push it to Docker hub.

## Getting Started

* [With Docker](#with-docker)
* [Without Docker](#without-docker)

### With Docker

#### Prerequisites

* [Docker](https://www.docker.com/)

#### Running

From your terminal/command prompt run:

```
docker pull sumansuyash/myrepo1:latest
docker run -p 5000:5000 -e FLASK_APP=main.py -e FLASK_RUN_HOST=0.0.0.0 sumansuyash/myrepo1
```

To validate - run below cURL command (The following command will make a POST API call to the flask application inside the docker container and returns a shortened URL as response)
```
curl -X POST 'http://127.0.0.1:5000/' --form 'url=http://web.whatsapp.com'
```

### Without Docker (Running the flask application locally without docker) (Requires python 3)

#### Setup steps

1. Clone the repository contents to a local folder.
2. Install [virtualenv](https://pypi.org/project/virtualenv/) and create a new environment.
2. Run `pip install -r requirements.txt` to install all the dependencies.

#### Running

From your terminal/command prompt run:

```
python main.py
```

To validate - run below cURL command
```
curl -X POST 'http://127.0.0.1:5000/' --form 'url="http://web.whatsapp.com"'
```

#### Configuration for Docker Image CI (for GitHub workflow)

The following properties must be configured in GitHub Secrets to build docker image and push to docker hub repository:

| Name                    | Purpose                                                          | Default              |
| ----------------------- | ---------------------------------------------------------------- | -------------------- |
| `DOCKER_USER`           | A GitHub secret username to access Docker Hub.                   | `Docker-id`          |
| `DOCKER_PASSWORD`       | A GitHub secret password to access Docker Hub.                   | `Docker-password`    |

## Technology Used

For those of you that are interested, the technology used in this project includes:

* [Python 3.9](https://www.python.org/downloads/release/python-390/)
* [Flask](http://flask.pocoo.org/) (Microframework)
* [Docker](https://www.docker.com/)
