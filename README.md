# ADDAFAT

# CI/CD Pipeline for Python Script using GitHub Actions

To implement a CI/CD pipeline for a Python script with the given scenario, we can use GitHub Actions. GitHub Actions is a powerful CI/CD platform provided by GitHub that allows you to automate your software development workflows.

Here's how you can create a workflow that runs on push to the `main` branch, installs dependencies using `pip install`, and runs `pylint` to check code quality:

1. In your Python project repository on GitHub, create a new directory named `.github/workflows/` if it doesn't already exist.

2. Inside the `workflows` directory, create a new YAML file, e.g., `python-lint.yml`, with the following content:


## Workflow YAML


```yaml
name: Python Lint

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
        
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pylint
        
    - name: Lint with pylint
      run: |
        pylint **/*.py

```
## YAML File Breakdown

- `name: Python Lint`: Name of the workflow.
- `on: push: branches: [main]`: Specifies that the workflow will run on every push to the `main` branch.
- `on: pull_request: branches: [main]`: Specifies that the workflow will run on every pull request from the `main` branch.
- `jobs: lint:`: Defines a job named `lint`.
- `runs-on: ubuntu-latest`: Specifies that the job will run on the latest Ubuntu runner provided by GitHub Actions.
- `steps:`: Defines the steps that the job will execute.
  - `uses: actions/checkout@v3`: Checks out your repository's code.
  - `name: Set up Python`: Sets up the Python environment using the `actions/setup-python` action.
  - `name: Install dependencies`: Installs the latest version of `pip` and the `pylint` package using `pip install`.
  - `name: Lint with pylint`: Runs the `pylint` command on all Python files in your repository (`**/*.py`).

## Usage

1. Commit the `python-lint.yml` file to your repository's `main` branch.
2. Whenever you push changes to the `main` branch, the workflow will automatically run, installing the required dependencies (`pip install`) and running `pylint` on your Python code to check for code quality issues.
3. View the workflow run and its results by going to the "Actions" tab in your repository on GitHub. If there are any issues detected by `pylint`, they will be displayed in the workflow logs.

