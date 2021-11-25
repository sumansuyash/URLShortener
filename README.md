# URL Shortener
URL Shortener Project

A simple URL shortener built with [Flask](http://flask.pocoo.org/) and [Pandas](https://pandas.pydata.org/)

## Getting Started

* [With Docker](#with-docker)
* [Without Docker](#without-docker)

### With Docker

#### Prerequisites

* [Docker](https://www.docker.com/)

#### Running

From your terminal/command prompt run:

```
docker-compose up
```

Then point your browser to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

### Without Docker

#### Installing Requirements

1. (Optional) Install [virtualenv](https://pypi.org/project/virtualenv/) and
[virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) and create a new environment.
2. Run `pip install -r requirements.txt`.

#### Configuration

The following properties can be configured:

| Name                    | Purpose                                                          | Default              |
| ----------------------- | ---------------------------------------------------------------- | -------------------- |
| `SECRET_USERNAME`       | A GitHub secret username to access Docker Hub.                   | `Docker-id`          |
| `SECRET_PASSWORD`       | A GitHub secret password to access Docker Hub.                   | `Docker-password`    |

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
