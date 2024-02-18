#!/usr/bin/python3
# makes tgz archive

from fabric import task
from fabric.context_managers import lcd
from fabric.operations import local
import datetime
import os

@task
def do_pack():
    # Create the versions directory if it doesn't exist
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
