#!/usr/bin/env python

import os

def path4pkg(dirname, directory=''):
    dirname = dirname.lower()
    for root, dirs, names in os.walk(directory):
        if dirname in dirs:
            return os.path.join(root, dirname)
    raise 'We work only with ROOT packages by now'
