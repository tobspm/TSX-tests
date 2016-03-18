#!usr/bin/env pyhton
# -*- coding: utf-8 -*-
#Modified date: 18/03/2016
#Nima
#

import numpy as np 
 
from TSX.position import Position

class TestPosition:
    """Class testing the methods of class Position.

    """
    def test_xyz(self):
	"""Tests the method xyz()."""
	array = np.array([45353255, 12547, 0.2225])
	assert array in Position.xyz()
    def test_latitude_longitude(self):
	pass
