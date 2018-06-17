""" A Path4pkg class
Experiments on trying to generate package for ROOT PM
"""
import os

class Path4pkg(object):
    """docstring for Path4pkg."""
    def __init__(self, arg=None):
        super(Path4pkg, self).__init__()
        self.arg = arg

    def path4pkg(self, dirname, directory=''):
        dirname = dirname.lower()
        for root, dirs, names in os.walk(directory):
            if dirname in dirs:
                return os.path.join(root, dirname)
        raise 'We work only with ROOT packages by now'
