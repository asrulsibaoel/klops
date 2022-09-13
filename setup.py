"""Python setup.py for klops package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("klops", "VERSION")
    '0.0.2'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    abs_file_path = os.path.join(os.getcwd(), path)
    return [
        line.strip()
        for line in read(abs_file_path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="klops",
    version=read("klops", "VERSION"),
    description="Awesome klops created by Koinworks Data Team",
    url="https://gitlab-engineering.koinworks.com/data-team/klops/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Koinworks Data Team",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=[
            "dvc",
            "google-cloud",
            "google-cloud-container",
            "google-cloud-storage",
            "google-auth",
            "hyperopt",
            "matplotlib",
            "scikit-learn",
            "mlflow",
            "seldon-core",
            "pandas",
            "numpy",
            "tqdm"
        ],
    extras_require={"test": [
            "pytest",
            "coverage",
            "flake8",
            "black",
            "isort",
            "pytest-cov",
            "codecov",
            "mypy",
            "gitchangelog",
            "mkdocs",
            "lazydocs",
            "build",
            "twine"
        ]},
)
