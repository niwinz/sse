# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = "sse",
    url = "https://github.com/niwibe/sse",
    author = "Andrei Antoukh",
    author_email = "niwi@niwi.be",
    version="1.2",
    description = "Server-Sent Events protocol implemetation.",
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
