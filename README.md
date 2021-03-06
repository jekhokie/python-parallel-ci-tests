# Python Parallel CI Tests

This project is intended to enable development of a CI pipeline to design and test parallel CI tests
using Docker (or other agents) and aggregating the results in a Jenkins pipeline. The idea is to provide
a framework for splitting massive tests into smaller test agents to speed up feedback timings.

This repository contains the material to accompany the blog post
[Parallelized Jenkins Jobs using Docker](https://jekhokie.github.io/ci/cd/jenkins/virtualbox/vm/infrastructure/docker/ansible/parallel/2019/05/16/parallelized-jenkins-docker-tests.html).

## Prerequisites

Install easy_install, pip and virtualenv. Then, clone this repository and navigate to this example:

```bash
$ git clone https://<git_location>/python-parallel-ci-tests.git
$ cd scriptbox/python-parallel-ci-tests
```

Install the required environment and libraries:

```bash
$ virtualenv --no-site-packages --distribute .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```

## Testing

You can test the application locally by running the PyTest Unit test suite (which is what a CI pipeline
in Jenkins or some other CI tool would use):

```bash
$ python -m pytest tests/
```

## Usage

To start the Flask application, simply run the `run.py` script:

```bash
$ python run.py
```

You can now open a browser and navigate to `http://<SERVER_IP>:8000/?job_id=5` to see the Hello World Flask
basic website which shows the "job_id" passed in the URL.

## Docker

There is a Dockerfile within the repository which bakes the Python tools required for this repository to work
with a Jenkins Docker slave image. You can build the Docker image like so:

```bash
$ docker build -t jenkins/ssh-slave-modified .
```

Once the build completes, run the command `docker image ls` and you should see your new image in place.

## License

All content within created by the author are licensed under the LICENSE.txt contents unless specified otherwise.
