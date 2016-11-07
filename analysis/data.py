# coding=utf-8

import numpy as np
from datamatrix import cached, DataMatrix, SeriesColumn, IntColumn, io
from analysis.constants import *

a = np.loadtxt('data/trace.txt')

@cached
def generatedata(effectsize=EFFECTSIZE, blinksinbaseline=BLINKSINBASELINE,
	**kwargs):

	dm = DataMatrix(length=TRACES)
	dm.c = IntColumn
	dm.c[:TRACES//2] = 1
	dm.c[TRACES//2:] = 2
	dm.y = SeriesColumn(depth=TRACELEN)
	dm.y.setallrows(a)
	dm.y += np.random.randint(NOISERANGE[0], NOISERANGE[1], TRACES)
	dm.y[TRACES//2:] += np.linspace(0, effectsize, TRACELEN)
	# Inroduce blinks
	for i, row in enumerate(dm):
		blinklen = np.random.randint(BLINKLEN[0], BLINKLEN[1], BLINKS)
		if i < blinksinbaseline:
			blinkstart = np.array([1])
		else:
			blinkstart = np.random.randint(BASELINE[1], TRACELEN, BLINKS)
		blinkend = blinkstart+blinklen
		for start, end in zip(blinkstart, blinkend):
			end = min(TRACELEN-1, end)
			if end-start < 2 * BLINKMARGIN:
				continue
			row.y[start:start+BLINKMARGIN] = \
				np.linspace(row.y[start-1], 0, BLINKMARGIN)
			row.y[end-BLINKMARGIN:end] = \
				np.linspace(0, row.y[end], BLINKMARGIN)
			row.y[start:end] = np.random.randint(0, 100, end-start)
	return dm
	
	
def realdata():
		
	dm = io.readpickle('data/real-data.pkl')
	print(len(dm))
	return dm
