from os.path import join, dirname

import yaml


def path(*paths):
    """Get full path to local resource."""
    return join(dirname(__file__), *paths)


def lsystems():
    """Load lsystem configs."""
    p = path("lsystems.yml")
    with open(p, "r") as file:
        return yaml.load(file, Loader=yaml.FullLoader)
