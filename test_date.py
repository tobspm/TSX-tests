#!usr/bin/env pyhton
# -*- coding: utf-8 -*-
#Modified date: 18/03/2016
#Nima
#
 
from TSX.date import Date

class TestDate:
    """Class testing the methods of class Date.

    """
    def test_vts(self):
	assert Date.vts(51880.745567) == 51880, 0.745567
