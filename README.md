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

  - version 3.1.0
  ```
  $ git clone git@github.com:wolfg1969/django-rest-framework.git
  $ cd django-rest-framework
  $ git checkout -b 3.1-docs origin/3.1-docs
  $ mkdocs build
  ```
  

  - For version 3.0.x
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
  ```
  $ cp -R ../django-rest-framework/site/* django-rest-framework-3.1.0.docset/Contents/Resources/Documents/
  ```

- Generate the docsets

  - For version 3.1.0
  ```
  $ python drfdoc2set.py 3.1.0
  ```

  - For version 3.0
  ```
  $ python drfdoc2set.py 3.0
  ```
  
  - For version 2.4.x
  ```
  $ python drfdoc2set.py 2.4
  ```
  