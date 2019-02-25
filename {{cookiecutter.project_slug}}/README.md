{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}

# {{ cookiecutter.project_name }}  

{% if is_open_source %}
[![](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}) [![](https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg?branch=master)](https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}) [![](https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest)](https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest)  
{% endif %}

{% if cookiecutter.add_pyup_badge == 'y' %}
[![Updates](https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/shield.svg)](https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/) [![Python 3](https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/python-3-shield.svg)](https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/)
{% endif %}

{{ cookiecutter.project_short_description }}  

{% if is_open_source %} 
* Free software: {{ cookiecutter.open_source_license }}  
* Documentation: [https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io](https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io).  

## Features  

TODO  

## Credits  

This package was create with [Cookiecutter] and the [robertopreste/cc-pypackage] project template.  

[Cookiecutter]: https://github.com/audreyr/cookiecutter 
[robertopreste/cc-pypackage]: https://github.com/robertopreste/cc-pypackage 
