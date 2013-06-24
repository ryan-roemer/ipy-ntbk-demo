"""Fabric file.

For a full list of command, type::

    fab -list
"""
import os

from fabric.api import task, local

###############################################################################
# Validation
###############################################################################
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
if os.path.abspath(os.getcwd()) != ROOT_DIR:
    abort("Fabric must be run from root directory \"%s\"." % ROOT_DIR)

###############################################################################
# Server
###############################################################################
@task
def server():
    """Notebook server."""
    local("ipython notebook")
