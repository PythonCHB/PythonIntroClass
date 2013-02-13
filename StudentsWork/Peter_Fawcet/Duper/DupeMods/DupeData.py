#!/usr/bin/env python

import shelve


class DupeShelve(object):
    def __init__(self):
        pass

    def WriteDB(self, path, data):
        sf = shelve.open(path)
        for key in data:
            sf[key] = data[key]
        sf.close()

    def ReadDB(self, path):
        sf = shelve.open(path)
        data = {}
        for key in sf:
            data[key] = sf[key]
        sf.close()
        return data
