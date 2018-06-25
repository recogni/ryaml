from setuptools import setup
from setuptools import find_packages

packages = find_packages()
packages.append("ryaml")

setup(name="ryaml",
      version="0.0.1",
      description="!include supported python yaml loader",
      url="https://github.com/recogni/yaml",
      author="sabhiram",
      install_requires=[
        "pyyaml",
      ],
      packages=packages)
