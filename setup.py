# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from setuptools import setup

description = """
"""

setup(
    name = "sse",
    url = "https://github.com/niwibe/sse",
    author = "Andrei Antoukh",
    author_email = "niwi@niwi.be",
    version="1.0",
    description = "Server Sent Events protocol implemetation.",
    install_requires=['distribute'],
    zip_safe=False,
    py_modules = ['sse'],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
)
