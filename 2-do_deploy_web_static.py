#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""


from fabric.api import put, run, env
from os.path import exists
env.hosts = ['54.90.31.96', '100.26.156.63']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        filename = archive_path.split('/')[-1]
        foldername = filename.split('.')[0]
        release_path = '/data/web_static/releases/{}/'.format(foldername)
        run('mkdir -p {}'.format(release_path))
        run('tar -xzf /tmp/{} -C {}'.format(filename, release_path))
        run('rm /tmp/{}'.format(filename))
        run('rm -f /data/web_static/current')
        run('ln -s {} {}'.format(release_path, '/data/web_static/current'))

        return True

    except Exception as e:
        return False
