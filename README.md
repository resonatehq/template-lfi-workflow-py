# Two step local function invocation workflow template

This repository serves serves as a template to scaffold Resonate projects in Python.

You can use this template by installing the Resonate CLI:

```shell
brew install resonatehq/tap/resonate
```

Then use the project creation command and specify this template:

```shell
resonate project create --name <your-project-name> --template two-step-lfi-workflow-py
```

Check the `pyproject.toml` file to see which package versions this template is pinned to.

You can use any python environment and package manager with this template, however we do prefer working with [uv](https://docs.astral.sh/uv/) and recommend it.

To run this project with `uv`:

```shell
uv sync
uv run app
```
