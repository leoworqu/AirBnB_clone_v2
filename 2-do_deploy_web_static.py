#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""
from fabric import task, env
from fabric.context_managers import cd
from fabric.operations import put, run
import os

# Define the web server IPs
web_servers = ['<IP web-01>', '<IP web-02>']

# Set the hosts using env.hosts
env.hosts = web_servers

@task
def do_deploy(archive_path):
    """Distributes an archive to web servers and deploys it."""
    # Check if the archive file exists
    if not os.path.exists(archive_path):
        print(f"Archive file '{archive_path}' does not exist.")
        return False

    # Extract the archive filename without extension
    archive_filename = os.path.basename(archive_path)
    archive_name = os.path.splitext(archive_filename)[0]

    try:
        # Upload the archive to /tmp/ directory on web servers
        put(archive_path, '/tmp/')

        # Create the directory /data/web_static/releases/<archive_name>
        run(f'mkdir -p /data/web_static/releases/{archive_name}')

        # Uncompress the archive to /data/web_static/releases/<archive_name>
        with cd('/data/web_static/releases/'):
            run(f'tar -xzf /tmp/{archive_filename} -C {archive_name}')

        # Delete the archive from the web servers
        run(f'rm /tmp/{archive_filename}')

        # Remove the symbolic link /data/web_static/current
        run('rm -f /data/web_static/current')

        # Create a new symbolic link /data/web_static/current
        run(f'ln -s /data/web_static/releases/{archive_name} /data/web_static/current')

        print("New version deployed successfully.")
        return True
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
