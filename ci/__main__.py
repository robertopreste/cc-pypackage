#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import shutil
import subprocess
import click


@click.group()
def cli():
    """ Main entry point for the CI infrastructure. """
    pass


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
def twine_upload():
    """ Upload the package to PyPI using Twine. """
    click.echo("Uploading package...")
    subprocess.check_call(["twine", "upload", "dist/*"])
    click.echo("Done.")


if __name__ == '__main__':
    cli()
