# coding=utf-8

import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
from datamatrix import series as srs
from datamatrix import cached, plot
from analysis import data, baseline, interaction
from analysis.constants import *

	
def ttest(dm, col):
	
	a1 = srs.reduce_(srs.window((dm.c == 1)[col], start=-50, end=-1))
	b1 = srs.reduce_(srs.window((dm.c == 2)[col], start=-50, end=-1))
	t, p = stats.ttest_ind(a1, b1)
	return p < ALPHA and t < 0


@cached
def power(dummy, blfilter=BLFILTER, **kwargs):
	
	hits1 = np.zeros(NSIM)
	hits2 = np.zeros(NSIM)
	hits4 = np.zeros(NSIM)
	for i in range(NSIM):
		print(i)
		dm = data.generatedata(**kwargs)
		if blfilter:
			dm.bl = baseline.baseline(dm)
			minbl = dm.bl.mean - BLSTDTHR * dm.bl.std
			maxbl = dm.bl.mean + BLSTDTHR * dm.bl.std
			dm = (dm.bl > minbl) & (dm.bl < maxbl)
		dm.y2 = baseline.correct1(dm)
		dm.y4 = baseline.correct3(dm)
		hits1[i] = ttest(dm, 'y')
		hits2[i] = ttest(dm, 'y2')
		hits4[i] = ttest(dm, 'y4')	
	print('Y1: power = ', hits1.mean())
	print('Y2: power = ', hits2.mean())
	print('Y4: power = ', hits4.mean())
	return hits1.mean(), hits2.mean(), hits4.mean()
	
	
def powersummary(dummy):
	
	plot.new()
	for i, blfilter, blinksinbaseline in (
		(1, False, 2), (2, True, 2), (3, False, 0)
		):
		l1 = []
		l2 = []
		l4 = []
		effectsizes = range(0, 501, 50)
		for effectsize in effectsizes:
			kwargs = {
				'effectsize' : effectsize,
				'blfilter' : blfilter,
				'blinksinbaseline' : blinksinbaseline				
				}
			cid = 'power-%(effectsize)s-%(blfilter)s-%(blinksinbaseline)s' % kwargs
			p1, p2, p4 = power(None, cacheid=cid, **kwargs)
			l1.append(p1)
			l2.append(p2)
			l4.append(p4)
		plt.subplot(3,1,i)
		if i == 1:
			plt.title('With blinks during baseline, without outlier removal')
		elif i == 2:
			plt.title('With blinks during baseline, with outlier removal')
		else:
			plt.title('No blinks during baseline')
		
		plt.axhline(.05, color='black', linestyle=':')
		plt.xlim(effectsizes[0]-10, effectsizes[-1]+10)
		plt.ylim(-.05, 1.05)
		plt.plot(effectsizes, l1, 'o-', label='No baseline correction',
			color=COLORNOCORRECT)
		plt.plot(effectsizes, l2, 'o-', label='Divide by baseline',
			color=COLORDIVIDE)
		plt.plot(effectsizes, l4, 'o-', label='Subtract baseline',
			color=COLORSUBTRACT)
		if i == 3:
			plt.legend(frameon=False, loc='lower right')
	plot.save('powersummary')
