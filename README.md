# Project

## Introduction

In the contemporary world, internet access has become a necessity for human beings. It is totally common for people to access news sites, social networks at any time of the day, whether to learn about the latest pronouncements of national or international politics, or to get in touch with that loved one who is far away. The fact is that the internet in addition to providing moments of fun and leisure, it is also a crucial tool for accessing information. Although it seems a trivial thing to do for people without disabilities, this simple act of seeking information can become a real complication if the person has a disability, whether physical or mental.

Thus, this project aims to assist in a minimal part of the development of software products, focusing on the web part that uses Hypertext Markup Language (HTML), so that it is possible to carry out tests, in a development environment to ensure that a minimum quantity accessibility is achieved by this product.

## Objective

Create a tool capable of carrying out accessibility tests, simple, on pages with the HTML language, that is integrated into the DevOps pipeline.


# Technology

The package was created using the python programming language on version 3 or higher

## Dependencies

The package dependencies that will be installed automatically are:
- beautifulsoup4 ~= 4.9; 
- py-w3c ~= 0.3

# Installation

There are two ways to install and use the package, the first being installing directly from the pip repository using the command: pip install -i https://test.pypi.org/simple/ automated-accessibility-testing==1.0.0

The second form of installation would be from this repository needing to perform the clone and install locally from this command: git clone https://github.com/TCC2-Romeu/automated_accessibility_testing.git

# Use

To use the package you can call the check_accessibility function and pass the html as a string, this way the package will perform all tests of the package in terms of accessibility in addition to a static validation of the html according to w3c, in case the user does not want to run some of the functions it can pass a list to the check_accessibility method where the listed functions will be ignored.
At the end the user will receive a list of objects with the errors pointed out

# License

The project license is: GPL3