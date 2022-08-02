"""Read the Python requirement from the pyproject.toml file."""
from __future__ import annotations

from typing import Any


def requires_python_pypa(pyproject_toml: dict[str, Any]) -> str | None:
    """Read the requires_python field when using PyPA standards.

    See:
    https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html
    """
    try:
        return pyproject_toml["project"]["requires-python"]
    except KeyError:
        return None


def requires_python_poetry(pyproject_toml: dict[str, Any]) -> str | None:
    """Read the requires_python field when using Poetry.

    See:
    https://python-poetry.org/docs/pyproject/#dependencies-and-dev-dependencies
    """
    try:
        return pyproject_toml["tool"]["poetry"]["dependencies"]["python"]
    except KeyError:
        return None
