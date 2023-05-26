drf-dash
========

![publish workflow](https://github.com/wolfg1969/drf-dash/actions/workflows/publish.yml/badge.svg) Now build with GitHub Actions! 

Build Django REST framework docset for Dash (http://kapeli.com/dash/)

Dependencies
------------

- [pipenv](https://pipenv.readthedocs.io/en/latest/)

Instructions
------------

```
$ pipenv install mkdocs
$ pipenv shell
$ make run version=3.8.2
$ ls build
```
