<h1 align="center">Difference generator</h1>

### Hexlet tests and linter status:
[![Actions Status](https://github.com/bloodywd/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/bloodywd/python-project-50/actions)
[![Github Actions Status](https://github.com/bloodywd/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/bloodywd/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/19f27d4b55055c9f553c/maintainability)](https://codeclimate.com/github/bloodywd/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/19f27d4b55055c9f553c/test_coverage)](https://codeclimate.com/github/bloodywd/python-project-50/test_coverage)

## Project setup

```
poetry publish --dry-run
python3 -m pip install --user dist/*.whl
```

## How to start

```
gendiff -h # See help page for usage
```

## About the project.

A difference generator is a program that determines the difference between two data structures.
Utility features:
Supports different input formats: yaml, json
Generating a report in the form of plain text, stylish and json

## System requirements

- Python v3.10 or higher

## Exaple of usage

[![asciicast](https://asciinema.org/a/XHuigUFdN1jBEpFXM8ivyhCsD.svg)](https://asciinema.org/a/XHuigUFdN1jBEpFXM8ivyhCsD)