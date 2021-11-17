[![Tests](https://github.com/alexmalins/actionsci/actions/workflows/tests.yml/badge.svg)](https://github.com/alexmalins/actionsci/actions/workflows/tests.yml)
[![Test Coverage](https://codecov.io/gh/alexmalins/actionsci/branch/master/graph/badge.svg)](https://codecov.io/gh/alexmalins/actionsci/)


# Example repo: using GitHub Actions for automated testing & code coverage

This is a minimal Python repo demonstrating the use of GitHub Actions for
automated testing & generating code coverage reports.

Testing is with `unittest` from Python's standard library.

Code coverage reports are generated using
[coverage.py](https://github.com/nedbat/coveragepy) and uploaded automatically
to [codecov](https://about.codecov.io/).

Useful resources on the topic:

- mCoding's [YouTube video](https://www.youtube.com/watch?v=DhUpxWjOhME) on
using GitHub actions for automated testing (see also the
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
