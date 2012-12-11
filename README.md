CodeMash Django Precompiler
===========================

Getting up and running
----------------------
You need a virtualenv to get started:

    python3 virtualenv.py django-precompiler
    source django-precompiler/bin/activate

Then install django 1.5:

    pip install https://www.djangoproject.com/download/1.5b2/tarball/

Then do the syncdb/runserver dance:

    ./manage.py syncdb
    ./manage.py runserver
