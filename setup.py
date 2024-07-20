import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="trex",
    version="0.0.1",
    author="Mahesh Natamai, Govind Gnanakumar",
    author_email="founders@automorphic.ai",
    description=(
        "Trex transforms your unstructured to structured data—just specify a regex or context free grammar and we'll intelligently ensure your data conforms."
    ),
    license="MIT",
    keywords="unstructured ETL, llms, gpt, regex, context free grammar, lark",
    # url = "http://packages.python.org/an_example_pypi_project",
    packages=["trex"],
    install_requires=["requests"],
    long_description=read("README.md"),
)
