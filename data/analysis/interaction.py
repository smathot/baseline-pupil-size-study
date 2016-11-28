# coding=utf-8

import numpy as np
from matplotlib import pyplot as plt
from datamatrix import series as srs
from datamatrix import DataMatrix
from datamatrix.rbridge import lme4
from analysis import data, baseline
from analysis.constants import *


def interactiontest(dm):
	
	dm.bl = baseline.baseline(dm)
	dm.test = srs.reduce_(srs.window(dm.y, start=-50, end=-1))
	
	lmdata = DataMatrix(length=len(dm)*2)
	lmdata.pupil = -1
	lmdata.time = -1
	lmdata.condition = -1
	lmdata.trialid = -1
	for i, row in enumerate(dm):
		lmdata.pupil[2*i] = row.bl
		lmdata.time[2*i] = 0
		lmdata.condition[2*i] = row.c
		lmdata.trialid[2*i] = i
		lmdata.pupil[2*i+1] = row.test
		lmdata.time[2*i+1] = 1
		lmdata.condition[2*i+1] = row.c
		lmdata.trialid[2*i+1] = i
	lm = lme4.lmer(lmdata, 'pupil ~ condition*time + (1|trialid)')
	print(lm.p[3])
	return lm.p[3] < ALPHA
