#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by {{ cookiecutter.full_name }}
import os
import shutil
import subprocess
{%- if cookiecutter.command_line_interface|lower == "click" %}
import click


@click.group()
def cli():
    """ Main entry point for the CI infrastructure. """
    pass


@cli.command(name="create-suite")
def create_suite():
    """ Create all files needed for testing. """
    click.echo("Updating test files...")

    click.echo("Done.")


@cli.command(name="build")
def build():
    """ Build the package to be uploaded to PyPI. """
    dist_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "dist")

    if os.path.isdir(dist_dir):
        click.echo("Removing dist directory... ", nl=False)
        shutil.rmtree(dist_dir)
        os.makedirs(dist_dir)
        click.echo("Done.")

    click.echo("Building package...")
    subprocess.check_call(["python", "setup.py", "sdist", "bdist_wheel"])
    click.echo("Done.")


@cli.command(name="check")
def twine_check():
    """ Check the package using Twine. """
    click.echo("Checking package...")
    subprocess.check_call(["twine", "check", "dist/*"])
    click.echo("Done.")


@cli.command(name="upload")
@click.option("-u", "--username", default=None, help="PyPI username.")
@click.option("-p", "--password", default=None, help="PyPI password.")
def twine_upload(username, password):
    """ Upload the package to PyPI using Twine.

    Args:
        username: PyPI username (if not provided, twine will ask for it)
        password: PyPI password (if not provided, twine will ask for it)
    """
    cmd = ["twine", "upload"]
    if username:
        cmd.extend(["-u", username])
        if password:
            cmd.extend(["-p", password])
    cmd.append("dist/*")

    click.echo("Uploading package...")
    subprocess.check_call(cmd)
    click.echo("Done.")


if __name__ == '__main__':
    cli()
{%- endif %}
