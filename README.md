# cc-pypackage  

[![Updates](https://pyup.io/repos/github/robertopreste/cc-pypackage/shield.svg)](https://pyup.io/repos/github/robertopreste/cc-pypackage/)

[![Python 3](https://pyup.io/repos/github/robertopreste/cc-pypackage/python-3-shield.svg)](https://pyup.io/repos/github/robertopreste/cc-pypackage/)

[![Build Status](https://travis-ci.com/robertopreste/cc-pypackage.svg?branch=master)](https://travis-ci.com/robertopreste/cc-pypackage)


My custom [Cookiecutter] template for a Python package.

* GitHub repo: [https://github.com/robertopreste/cc-pypackage](https://github.com/robertopreste/cc-pypackage)  
* Documentation: [https://cc-pypackage.readthedocs.io](https://cc-pypackage.readthedocs.io)  
* Free software: BSD license  

## Features  

* Testing setup with `unittest` and `python setup.py test` or `pytest` (used by default)  
* [Travis-CI]: Ready for Travis Continuous Integration testing
* [Tox] testing: Setup to easily test for Python 3.4, 3.5, 3.6
* [Sphinx] docs: Documentation ready for generation with, for example, [ReadTheDocs]
* [Bumpversion]: Pre-configured version bumping with a single command
* Auto-release to [PyPI] when you push a new tag to master (optional)
* Command line interface using Click (optional)


## Build Status  

Linux:

[![Build Status](https://travis-ci.com/robertopreste/cc-pypackage.svg?branch=master)](https://travis-ci.com/robertopreste/cc-pypackage)

Windows:

[![Build status](https://ci.appveyor.com/api/projects/status/0rao47b8wcw705do?svg=true)](https://ci.appveyor.com/project/robertopreste/cc-pypackage)


## Quickstart  

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/robertopreste/cc-pypackage.git

Then:

* Create a repo and put it there.
* Add the repo to your [Travis-CI] account.
* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
* [Register] your project with PyPI.
* Run the Travis CLI command `travis encrypt --add deploy.password` to encrypt your PyPI password in Travis config
  and activate automated deployment on PyPI when you push a new tag to master branch.
* Add the repo to your [ReadTheDocs] account + turn on the ReadTheDocs service hook.
* Release your package by pushing a new tag to master.
* Add a `requirements.txt` file that specifies the packages you will need for
  your project and their versions. For more info see the [pip docs for requirements files].
* Activate your project on [pyup.io].


[Register]: https://packaging.python.org/distributing/#register-your-project
[pip docs for requirements files]: https://pip.pypa.io/en/stable/user_guide/#requirements-files

For more details, see the [cookiecutter-pypackage tutorial].

[cookiecutter-pypackage tutorial]: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html

## References  

This Cookiecutter was adapted for my personal needs from the original [Cookiecutter-PyPackage] by [audreyr].  

[Cookiecutter-PyPackage]: https://github.com/audreyr/cookiecutter-pypackage
[audreyr]: https://github.com/audreyr

[Cookiecutter]: https://github.com/audreyr/cookiecutter
[Travis-CI]: http://travis-ci.com/
[Tox]: http://testrun.org/tox/
[Sphinx]: http://sphinx-doc.org/
[ReadTheDocs]: https://readthedocs.io/
[pyup.io]: https://pyup.io/
[Bumpversion]: https://github.com/peritus/bumpversion
[Punch]: https://github.com/lgiordani/punch
[PyPi]: https://pypi.python.org/pypi
