# Python Parallel CI Tests

This project is intended to enable development of a CI pipeline to design and test parallel CI tests
using Docker (or other agents) and aggregating the results in a Jenkins pipeline. The idea is to provide
a framework for splitting massive tests into smaller test agents to speed up feedback timings.

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

You can now open a browser and navigate to h`ttp://<SERVER_IP>:8000/?job_id=5` to see the Hello World Flask
basic website which shows the "job_id" passed in the URL.

## License

All content within created by the author are licensed under the LICENSE.txt contents unless specified otherwise.
