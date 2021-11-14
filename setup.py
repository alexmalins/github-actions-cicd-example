from setuptools import setup

if __name__ == "__main__":
    with open("actions-ci-test/__init__.py", "r") as file:
        for line in file:
            if line.startswith("__version__"):
                version = line.strip().split()[-1][1:-1]
                break

    setup(version=version)
