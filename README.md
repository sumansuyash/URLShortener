
A simple URL shortener built with [Flask](http://flask.pocoo.org/), [Pandas](https://pandas.pydata.org/) and [Docker](https://www.docker.com/) with Docker Image CI as GitHub workflow.

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
docker run myrepo1
```

Then point your browser to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

### Without Docker

#### Installing Requirements

1. (Optional) Install [virtualenv](https://pypi.org/project/virtualenv/) and
[virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) and create a new environment.
2. Run `pip install -r requirements.txt`.

#### Configuration for Docker Image CI

The following properties must be configured in GitHub Secrets to build docker image and push to docker hub repository:

| Name                    | Purpose                                                          | Default              |
| ----------------------- | ---------------------------------------------------------------- | -------------------- |
| `DOCKER_USER`           | A GitHub secret username to access Docker Hub.                   | `Docker-id`          |
| `DOCKER_PASSWORD`       | A GitHub secret password to access Docker Hub.                   | `Docker-password`    |

#### Running

From your terminal/command prompt run:

```
./main.py
```

Then point your browser to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Technology Used

For those of you that are interested, the technology used in this project includes:

* [Python 3.9](https://www.python.org/downloads/release/python-390/)
* [Flask](http://flask.pocoo.org/) (Microframework)
* [Docker](https://www.docker.com/)
