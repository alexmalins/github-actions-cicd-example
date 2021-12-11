[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](https://github.com/alexmalins/github-actions-cicd-example/blob/main/LICENSE)
[![Tests](https://github.com/alexmalins/github-actions-cicd-example/actions/workflows/1_tests.yml/badge.svg)](https://github.com/alexmalins/github-actions-cicd-example/actions/workflows/1_tests.yml)
[![codecov](https://codecov.io/gh/alexmalins/github-actions-cicd-example/branch/main/graph/badge.svg?token=EXFQHNBA9Z)](https://codecov.io/gh/alexmalins/github-actions-cicd-example)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/alexmalins/github-actions-cicd-example/actions/workflows/3_linting.yml)
[![Checked with mypy](https://img.shields.io/badge/mypy-checked-blue)](https://github.com/alexmalins/github-actions-cicd-example/actions/workflows/3_linting.yml)
[![Latest Documentation](https://img.shields.io/badge/docs-latest-brightgreen)](https://alexmalins.github.io/github-actions-cicd-example)


# Example repo: using GitHub Actions for CI/CD  for a Python project

This is a minimal repo demonstrating the use of GitHub Actions for Continuous
Integration (CI) & Continous Deployment (CD) for a Python project.

The GitHub Actions are:

1. **Tests:** Automatically unit test code using `unittest` from Python's
standard library.
2. **Code coverage:** Generate code coverage reports using
[coverage.py](https://github.com/nedbat/coveragepy). The reports are
automatically uploaded to [codecov](https://about.codecov.io/). The
@codecov-commenter bot adds a comment to PR on code coverage status.
3.  **Lint and format code:** Lint using [pylint](https://www.pylint.org/). Check code formatting using
[black](https://github.com/psf/black). Check type hints using
[mypy](http://mypy-lang.org/).
4. **Check docs build:** Check [Sphinx](https://www.sphinx-doc.org) docs build successfully.
5. **Deploy docs to GitHub pages:** Automatically deploy docs to a
[GitHub Pages repo](https://github.com/alexmalins/alexmalins.github.io)  upon
merges to `main` branch.
6. **Upload release to PyPI:** Publish the latest version of the package on
[PyPI](https://pypi.org/) when a new GitHub Release is created.

Each of these actions is stored in a YAML file in the
[.github/workflows](https://github.com/alexmalins/github-actions-cicd-example/tree/main/.github/workflows)
directory. 

## File system structure

TBA...

## Push Token for Deploying Docs

Action #5 requires setting up a Personal Access Token with full repo access via
the Developer Settings page. Store this token as an Actions secret under the
name `PUSH_TOKEN` in the main repo (i.e. the repo where the docs source code is
held). See more [here](https://stackoverflow.com/questions/65997950/how-let-github-actions-workflow-push-generated-documentation-to-other-repository).

## Useful resources on the topic

- mCoding's [YouTube video](https://www.youtube.com/watch?v=DhUpxWjOhME) on
using GitHub actions for automated testing (see associated
[code repo](https://github.com/mCodingLLC/SlapThatLikeButton-TestingStarterProject)).
- Alex Damiani's YouTube videos on automated testing
[[1](https://www.youtube.com/watch?v=oi94qEvi9Qo)],
[[2](https://www.youtube.com/watch?v=rY-igT2N8zU)] &
[[3](https://www.youtube.com/watch?v=OOZtW3iF0is)] and associated code repos:
[[1](https://github.com/alexanderdamiani/test_repo_pylinter_v1)]
[[2](https://github.com/alexanderdamiani/test_repo_pylinter_v2)], &
[[3](https://github.com/alexanderdamiani/pytester_test_repo)].
- [librosa](https://github.com/librosa/librosa) is a real-world example of
`pyproject.toml`, `setup.cfg` & `setup.py` working together.
- [Pharmpy](https://github.com/pharmpy/pharmpy) uses Actions for building docs
then deploying them to a separate GitHub Pages repo.
- Vinod Kurup's
[blog post](https://www.caktusgroup.com/blog/2021/02/11/automating-pypi-releases/)
on automating PyPI releases with GitHub Actions.
