========================
RadiumIT Project
========================

This is a Python project that downloads files from a repository and calculates their SHA256 hashes. It also includes tests for the downloader and hasher.

Project Structure
=================

.. code-block:: text

    Radium/
    ├── scripts/
    │   ├── file.py
    │   └── run.py
    ├── test/
    │   └── test.py
    ├── venv/
    ├── .editorconfig
    ├── .flake8
    ├── .gitignore
    ├── .wemake_python_styleguide
    ├── Makefile
    ├── poetry.lock
    ├── pyproject.toml
    ├── pytest.ini
    ├── README.rst
    └── .pre-commit-config.yaml

Setup
=====

To set up the project, follow these steps:

1. Clone the repository:
   .. code-block:: bash

       git clone https://github.com/atabekdemurtaza/Radium.git
       cd Radium

2. Install the dependencies:
   .. code-block:: bash

       make install

3. Install pre-commit hooks:
   .. code-block:: bash

       make pre-commit

Usage
=====

To run the main script that downloads files and calculates their hashes:
.. code-block:: bash

    make run

Testing
=======

To run tests with coverage:
.. code-block:: bash

    make test

To generate an HTML coverage report:
.. code-block:: bash

    make coverage

Cleaning Up
===========

To clean up the project directory:
.. code-block:: bash

    make clean

Pre-commit Hooks
================

This project uses pre-commit hooks to ensure code quality. The hooks will automatically run on every commit to check for issues such as trailing whitespace, missing end-of-file newlines, and code formatting.

To manually run the pre-commit hooks on all files:
.. code-block:: bash

    pre-commit run --all-files

Project Configuration
======================

- **.editorconfig**: Defines the coding style for different file types.
- **.flake8**: Configuration file for Flake8, a linting tool for Python.
- **.wemake_python_styleguide**: Configuration for the wemake-python-styleguide.
- **Makefile**: Contains commands for setting up and managing the project.
- **pyproject.toml**: Configuration for Poetry and project dependencies.
- **pytest.ini**: Configuration for pytest, the testing framework.
- **.pre-commit-config.yaml**: Configuration for pre-commit hooks.

Contributing
============

If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.
