#!/usr/bin/python3
"""
Fabric script to genereate tgz archive
execute: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    making an archive on web_static folder
    """
    local('sudo mkdir -p versions')
    t = datetime.now()
    time = t.strftime("%Y%m%d%H%M%S")

    create = local(f'sudo tar -cvzf versions/web_static_{time}.tgz web_static')
