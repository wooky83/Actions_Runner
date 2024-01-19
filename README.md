# AWS Runner for Shell Script and Python Tests

This project uses AWS runner to run shell script checks and Python tests.

## Description

This project automates shell script checks and Python tests using AWS runner. By running shell script checks and Python tests in a CI/CD pipeline configured with AWS runner, this project helps maintain code quality, and quickly find and fix errors.

## Installation

To use this project, you first need to set up AWS runner. For detailed information on setting up AWS runner, refer to the [AWS official documentation](https://docs.aws.amazon.com/codebuild/latest/userguide/runner.html).

Also, to run Python tests, you need the respective environment. The required Python packages are specified in the `requirements.txt` file:

```bash
pip install -r requirements.txt