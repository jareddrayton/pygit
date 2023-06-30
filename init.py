"""Module for initialising a git repository"""

from pathlib import Path

DESCRIPTION = "Unnamed repository; edit this file 'description' to name the repository."
CONFIG = """[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true"""
HEAD = "ref: refs/heads/master"


class Init:
    def __init__(self, directory=None):

        if directory == None:
            directory = Path("/home/jared/test")
            directory.mkdir()

        self.directory = Path(directory / '.git')

        self.create_directories()
        self.create_files()

    def create_directories(self):
        directories = {
            "branches",
            "hooks",
            "info",
            "objects/info",
            "objects/pack",
            "refs/heads",
            "refs/tags",
        }

        for directory in directories:
            Path(self.directory / directory).mkdir(parents=True, exist_ok=True)

    def create_files(self):
        template = {
            "description": DESCRIPTION,
            "config": CONFIG,
            "HEAD": HEAD,
        }

        for filename, content in template.items():
            with open(self.directory / filename, 'w') as fh:
                fh.write(content)
