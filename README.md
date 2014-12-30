drf-dash
========

Django REST framework docset for Dash (http://kapeli.com/dash/)

Instructions
------------
- Checkout source codes of Django REST framework

```
$ git clone git@github.com:tomchristie/django-rest-framework.git
$ cd django-rest-framework
```

- Generate the html docs

  - For version 3.0
  ```
  $ git checkout tags/3.0.2
  $ git apply ../drf-dash/3.0.patch
  $ mkdocs build
  ```
  
  - For version 2.4.x
  ```
  $ git checkout tags/2.4.4
  $ git apply ../drf-dash/2.4.patch
  $ python mkdocs.py
  ```
  
- Copy the html docs to docsets

- Generate the docsets

  - For version 3.0
  ```
  $ python drfdoc2set.py
  ```
  
  - For version 2.4.x
  ```
  $ python drfdoc2set.py --v2
  ```
  