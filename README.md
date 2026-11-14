
# water-column-sonar-ai
🌊 Water Column Sonar Machine Learning Workflow ⭐


# Setting up the Python Environment
> Python 3.12.11

# Installing Dependencies
```
source .venv/bin/activate

uv pip install --upgrade pip

uv pip install -r pyproject.toml --all-extras

uv run pre-commit install
```

# Pytest
```
uv run pytest tests -W ignore::DeprecationWarning
```
or
> pytest --cache-clear --cov=src tests/ --cov-report=xml

# Instructions
Following this tutorial:
https://packaging.python.org/en/latest/tutorials/packaging-projects/

# Pre Commit Hook
see here for installation: https://pre-commit.com/
https://dev.to/rafaelherik/using-trufflehog-and-pre-commit-hook-to-prevent-secret-exposure-edo
```
pip install pre-commit
uv run pre-commit install
```

# Black
https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/
```
Settings > Black
Execution mode: Package
Python Interpreter: .../.venv/bin/python
Use Black Formatter: X On Code reformat, X On Save
```

# Linting
Ruff
https://plugins.jetbrains.com/plugin/20574-ruff


# Test Coverage
TODO

# Tag a Release
Step 1 --> increment the semantic version in the zarr_manager.py "metadata" & the "pyproject.toml"
```commandline
git tag -a v26.11.1 -m "Releasing v26.11.1"
git push origin --tags
```

# To Publish To PROD
```commandline
uv build --no-sources
uv publish
```

# TODO:
add https://pypi.org/project/setuptools-scm/
for extracting the version

# Security scanning
> bandit -r water_column_sonar_ai/

# Data Debugging
Experimental Plotting in Xarray (hvPlot):
https://colab.research.google.com/drive/18vrI9LAip4xRGEX6EvnuVFp35RAiVYwU#scrollTo=q9_j9p2yXsLV

HB0707 Zoomable Cruise:
https://hb0707.s3.us-east-1.amazonaws.com/index.html


# UV Debugging
```
uv lock --check
uv lock
uv sync --extra dev
#uv run pytest tests
```
