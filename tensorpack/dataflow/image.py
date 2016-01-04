#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
# File: image.py
# Author: Yuxin Wu <ppwwyyxx@gmail.com>

import numpy as np
import cv2
from .base import DataFlow

__all__ = ['ImageFromFile']

class ImageFromFile(DataFlow):
    """ generate rgb images from files """
    def __init__(self, files, channel=3, resize=None):
        """ files: list of file path
            channel: 1 or 3 channel
            resize: a (h, w) tuple. If given, will force a resize
        """
        assert len(self.files)
        self.files = files
        self.channel = int(channel)
        self.resize = resize

    def size(self):
        return len(self.files)

    def get_data(self):
        for f in self.files:
            im = cv2.imread(
                f, cv2.IMREAD_GRAYSCALE if self.channel == 1 else cv2.IMREAD_COLOR)
            if self.channel == 3:
                im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
            if self.resize is not None:
                im = cv2.resize(im, self.resize[::-1])
            yield [im]
