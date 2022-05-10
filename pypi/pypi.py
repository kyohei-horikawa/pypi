import fire
import subprocess
import os
from pathlib import Path


class Cli:
    def get_new_path(self):
        paths = list(Path('./dist').glob(r'*.tar.gz'))
        paths.sort(key=os.path.getmtime)
        return paths[-1]

    def local(self):
        subprocess.call(['python3', 'setup.py', 'sdist'])
        subprocess.call(['pip3', 'install', self.get_new_path()])

    def upload(self, to):
        subprocess.call(['python3', 'setup.py', 'sdist', 'bdist_wheel'])
        subprocess.call(['python3', '-m', 'twine', 'upload', '-r', to, self.get_new_path(), '--verbose'])


def main():
    fire.Fire(Cli)
