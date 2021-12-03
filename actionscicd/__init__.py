"""actionscicd is a small & useless Python package created as an example to
show automated CI/CD, code coverage and linting, docs deployment to GitHub
Pages, and releasing to PyPI, all with GitHub actions."""

__version__ = "0.0.1"

from actionscicd.somecode import add_arrays, load_datafile

__all__ = ["add_arrays", "load_datafile"]
