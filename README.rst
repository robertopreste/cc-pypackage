============
cc-pypackage
============

.. image:: https://travis-ci.com/robertopreste/cc-pypackage.svg?branch=master
    :target: https://travis-ci.com/robertopreste/cc-pypackage
    :alt: Build status

.. image:: https://ci.appveyor.com/api/projects/status/0rao47b8wcw705do?svg=true
    :target: https://ci.appveyor.com/project/robertopreste/cc-pypackage
    :alt: Build status

.. image:: https://pyup.io/repos/github/robertopreste/cc-pypackage/shield.svg
     :target: https://pyup.io/repos/github/robertopreste/cc-pypackage/
     :alt: Updates

.. image:: https://pyup.io/repos/github/robertopreste/cc-pypackage/python-3-shield.svg
     :target: https://pyup.io/repos/github/robertopreste/cc-pypackage/
     :alt: Python 3

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
   :target: https://saythanks.io/to/robertopreste

My custom Cookiecutter_ template for a Python package.

* GitHub repo: https://github.com/robertopreste/cc-pypackage/
* Documentation: https://cc-pypackage.readthedocs.io/
* Free software: BSD license

Features
--------

* Testing setup with ``unittest`` and ``python setup.py test`` or ``pytest`` (used by default)
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 3.4, 3.5, 3.6
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_
* Bumpversion_: Pre-configured version bumping with a single command
* Auto-release to PyPI_ when you push a new tag to master (optional)
* Command line interface using Click (optional)

.. _Cookiecutter: https://github.com/audreyr/cookiecutter

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/robertopreste/cc-pypackage.git

Then:

* Create a repo and put it there.
* Add the repo to your Travis-CI_ account.
* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
* Register_ your project with PyPI.
* Run the Travis CLI command `travis encrypt --add deploy.password` to encrypt your PyPI password in Travis config
  and activate automated deployment on PyPI when you push a new tag to master branch.
* Add the repo to your ReadTheDocs_ account + turn on the ReadTheDocs service hook.
* Release your package by pushing a new tag to master.
* Add a `requirements.txt` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`_.
* Activate your project on `pyup.io`_.

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files
.. _Register: https://packaging.python.org/distributing/#register-your-project

For more details, see the `cc-pypackage tutorial`_.

.. _`cc-pypackage tutorial`: https://cc-pypackage.readthedocs.io/en/latest/tutorial.html

Credits
-------

This Cookiecutter was adapted for my personal needs from the original `Cookiecutter-PyPackage`_ by audreyr_.

.. _`Cookiecutter-PyPackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _audreyr: https://github.com/audreyr


.. _Travis-CI: http://travis-ci.com/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.io/
.. _`pyup.io`: https://pyup.io/
.. _Bumpversion: https://github.com/peritus/bumpversion
.. _Punch: https://github.com/lgiordani/punch
.. _PyPi: https://pypi.python.org/pypi
