# Data Models Workshop


1. [Setup](#setup)
2. [Testing](#testing)
    1. [Unit Testing](#unit-testing)
    2. [Integration Testing](#integration-testing)
    3. [Manual Testing](#manual-testing)
3. [CI/CD](#cicd)
    1. [CI](#ci)
4. [Code Structure](#code-structure)


## Setup

- It is recommended to use [pyenv](https://github.com/pyenv/pyenv), a CLI tool that allows multiple versions of Python to be
  installed separately. Follow the [installation instructions](https://github.com/pyenv/pyenv#installation)
  for your platform and run:

  ```
  pyenv install
  ```

- This will download and install Python **3.10.11** which is specified in the `.project-version` file which in turn is created by the command `pyenv local 3.10.11`. This use of pyenv ensures the pinning and usage of the specified Python version.

  > Note: pyenv downloads and compiles the version of Python you install, which means you may need
  > to also install some libraries if not present in your system, please follow the
  > [common build problems wiki](https://github.com/pyenv/pyenv/wiki/Common-build-problems) for
  > your platform.
  > 
  > If you already have Python 3.10.11 installed you do not need to reinstall it and pyenv should automatically use the correct version due to the pinning file `.project-version`

- Create a virtualenv:

  ```bash
    python -m venv .venv
    source .venv/bin/activate
  ```
  This virtualenv now has the version of Python which was set by pyenv and the .project-version file.
  
  > Note: the rest of these instructions assume you've activated the virtualenv as does the Makefile. You may want to use a virtualenv tool like
  > [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) or
  > [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv).
  
- Install dependencies via:
  ```bash
    make install-dev
  ```
- Please do not use pip by hand as the makefile contains the explicit activation of pre-commit hooks which will be necessary.

- Then run docker-compose up to start the deployment so that you can run the tests .
 ```bash
    make build-image
  ```

### Setup operational event database

Change the environment variable OPERATIONAL_DB_URL to point to the proper PostgreSQL database. By default points to the one
used for integration testing, in [docker-compose-test.yaml](docker-compose-test.yaml) as 

```text
postgresql://postgres:example@localhost:5432/postgres
```

If there are special character in password/username like the ones provided by AWS, you need to url encode them
through some service , e.g. [here](https://www.urlencoder.org/).


## Testing

### Unit Testing
Tested with python 3.10.11.

```bash
  pip install -r requirements.txt
```

- Run all tests with:
```bash
  make unit
 ```

### Integration Testing

Part of the automated tests. If you need to test manually, it is as easy as executing
```bash
  make integration
```

or specifically

```bash
    docker compose -f docker-compose-test.yaml up -d --wait

	echo "Running integration tests"
	pytest -v -s tests/integration --no-header -vv || (make integration-teardown && exit 1)
	echo "Tearing down environment"
	docker-compose -f docker-compose-test.yaml down -v

	echo "Clearing caches"
	make clear
```

The integration tests need a running environment consisting of:

- An operational events postgres database    

The test is trying to add an object in DB and retrieve it. These test roles are already present in [docker-compose-test.yaml](docker-compose-test.yaml)


To run both unit and integration together run:

```bash
  make test
```


### Manual Testing

Here we run manually the steps leading to the integration tests. This can be useful for debugging purposes and local development.
To create a local environment with prepopulated test data you can run:

```bash
  make create-dev
```

You can find 

- the postgres database on localhost:5432, username is `myuser` and password `mypassword`

(if you need things to be stateful, uncomment postgres and mssql volumes on the [docker-compose-test.yaml](docker-compose-test.yaml) file)


## CI/CD

The CI/CD pipeline is configured in the [GitHub actions](.github/workflows) files. 

### CI
The CI pipeline is configured in the [GitHub actions](.github/workflows/ci.yml) file. 
- It is triggered on every push to the main branch and in every pull request(pr).
- It runs  unit testing and the integration testing.
- It also runs the pre-commit hooks to ensure that the code is formatted correctly and that the tests pass before pushing to the main branch.
- Fails if any of the tests fail.


## Code Structure

```
.
├── Dockerfile                   # Docker configuration for building a containerized application
├── LICENSE.txt                  # The license under which the software is released
├── Makefile                     # Contains commands to automate common development tasks
├── README.md                    # Repository documentation with introduction, usage, etc.
├── app                          # Main application code
├── app                          # Main application code
├── artifacts                    # Supplementary files that support the application, including docs and test queries
├── data                         # Directory for data-related files (potentially seed data, migrations, etc.)
├── docker-compose-test.yaml     # Docker Compose configuration specifically for testing environment
├── docker-compose.yaml          # Docker Compose configuration for local development and deployment
├── pyproject.toml               # Configuration and metadata for Python projects, often used with poetry
├── pytest.ini                   # Configuration file for pytest (testing framework)
├── requirements.txt             # List of Python dependencies
├── setup.cfg                    # General configuration file for Python tools and setup
└── tests                        # Test suite for the application     
```