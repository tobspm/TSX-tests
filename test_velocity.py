#!usr/bin/env pyhton
# -*- coding: utf-8 -*-
#Modified date: 18/03/2016
#Nima
#
 
from TSX.velocity import Velocity

class TestVelocity:
    """Class testing the methods of class Velocity.

    """
    def test_vxvyvz(self):
	"""Tests the method vxvyvz()."""
	v_list = []
	assert Velocity.test_vxvyvz() == v_list
