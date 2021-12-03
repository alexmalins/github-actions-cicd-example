[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](https://github.com/alexmalins/github-actions-cicd-example/blob/main/LICENSE)
[![Tests](https://github.com/alexmalins/github-actions-cicd-example/actions/workflows/1_tests.yml/badge.svg)](https://github.com/alexmalins/github-actions-cicd-example/actions/workflows/1_tests.yml)
[![codecov](https://codecov.io/gh/alexmalins/github-actions-cicd-example/branch/main/graph/badge.svg?token=EXFQHNBA9Z)](https://codecov.io/gh/alexmalins/github-actions-cicd-example)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](https://img.shields.io/badge/mypy-checked-blue)](http://mypy-lang.org/)
[![Latest Documentation](https://img.shields.io/badge/docs-latest-brightgreen)](https://alexmalins.github.io/github-actions-cicd-example)


# Example repo: using GitHub Actions for Python Project CI/CD

This is a minimal repo demonstrating the use of GitHub Actions for CI/CD on a
Python project.

The workflows are:

1. Automated testing using `unittest` from Python's standard library.
2. Generate code coverage reports using
[coverage.py](https://github.com/nedbat/coveragepy). The reports are
automatically uploaded to [codecov](https://about.codecov.io/). The
@codecov-commenter bot adds a comment to PR on code coverage status.
3.  Lint using [pylint](https://www.pylint.org/). Check code formatting using
[black](https://github.com/psf/black). Check type hints using
[mypy](http://mypy-lang.org/).
4. Check [Sphinx](https://www.sphinx-doc.org) docs build successfully.
5. Automatically deploy docs to a [GitHub Pages repo]()  upon merges to `main`
branch (COMING SOON).
6. Upload package to [PyPI](https://pypi.org/) when a new release is created on
GitHub (COMING SOON).



## File system structure

TBA...

## Useful resources on the topic

- mCoding's [YouTube video](https://www.youtube.com/watch?v=DhUpxWjOhME) on
using GitHub actions for automated testing (see associated
[code repo](https://github.com/mCodingLLC/SlapThatLikeButton-TestingStarterProject)).
- Alex Damiani's YouTube videos on the same topic
[[1](https://www.youtube.com/watch?v=oi94qEvi9Qo)],
[[2](https://www.youtube.com/watch?v=rY-igT2N8zU)] &
[[3](https://www.youtube.com/watch?v=OOZtW3iF0is)] and associated code repos:
[[1](https://github.com/alexanderdamiani/test_repo_pylinter_v1)]
[[2](https://github.com/alexanderdamiani/test_repo_pylinter_v2)], &
[[3](https://github.com/alexanderdamiani/pytester_test_repo)].
- [librosa](https://github.com/librosa/librosa) is a real-world example of
`pyproject.toml`, `setup.cfg` & `setup.py` working together.
