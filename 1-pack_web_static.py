#!/usr/bin/python3
"""
Fabric script to genereate tgz archive
execute: fab -f 1-pack_web_static.py do_pack
"""

from fabric import task
from fabric.context_managers import lcd
from fabric.operations import local
import datetime
import os

@task
def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    All files in the folder web_static are added to the final archive.
    All archives are stored in the folder versions (this function creates the folder if it doesn’t exist).
    The name of the archive created is web_static_<year><month><day><hour><minute><second>.tgz.
    
    Returns:
        str: The path of the generated archive if successful, otherwise None.
    """
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Generate the filename for the archive
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{timestamp}.tgz"
    archive_path = os.path.join("versions", archive_name)

    # Create the .tgz archive
    with lcd("web_static"):
        result = local("tar -cvzf {} .".format(archive_path), capture=True)
        if result.succeeded:
            return archive_path
        else:
            return None
