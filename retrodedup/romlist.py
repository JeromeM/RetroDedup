# -*- coding: utf-8 -*-
import os


class RomList:
    def __init__(self, romset_dir):
        self.romset_dir = romset_dir

    def scandir(self, extension, directory=''):
        romfiles = []
        if directory == '':
            directory = self.romset_dir
        dirs = os.scandir(directory)
        for res in dirs:
            if res.is_dir() and res.name != 'medias':
                romfiles.extend(self.scandir(extension, res.path))

            if res.name.endswith('.xml'):
                continue

            if res.name == 'medias':
                continue

            if res.name.endswith(extension):
                romfiles.append((res.name, res.path))

        return romfiles
