from setuptools import find_packages, setup

with open('requirements.txt', 'r') as file:
    requires = file.readlines()

setup(name="flask-microservices",
      version="0.1.0",
      description="Example of Microservices using Flask",
      author="Prasad Borkar",
      license="BSD",
      packages=find_packages(),
      install_requires=requires,
      )