# coding=utf-8

import numpy as np
from datamatrix import series as srs
from analysis.constants import *


def baseline(dm):
	
	return srs.reduce_(
		srs.window(dm.y, start=BASELINE[0], end=BASELINE[1]),
		operation=REDUCEFNC)	


def correct1(dm):
	
	return srs.baseline(dm.y, dm.y, BASELINE[0], BASELINE[1],
		reduce_fnc=REDUCEFNC)


def correct2(dm):
	
	return (dm.y - baseline(dm)) / REDUCEFNC(dm.y[:,BASELINE[0]:BASELINE[1]])


def correct3(dm):
	
	return dm.y - baseline(dm)
	
