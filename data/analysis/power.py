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
	return p < ALPHA and t < 0, p < ALPHA and t > 0


@cached
def power(dummy, blfilter=BLFILTER, **kwargs):
	
	hits1 = np.zeros(NSIM)
	hits2 = np.zeros(NSIM)
	hits4 = np.zeros(NSIM)
	spurious1 = np.zeros(NSIM)
	spurious2 = np.zeros(NSIM)
	spurious4 = np.zeros(NSIM)
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
		hits1[i], spurious1[i] = ttest(dm, 'y')
		hits2[i], spurious2[i] = ttest(dm, 'y2')
		hits4[i], spurious4[i] = ttest(dm, 'y4')	
	print('Y1: power = ', hits1.mean())
	print('Y2: power = ', hits2.mean())
	print('Y4: power = ', hits4.mean())
	print('Y1: spurious = ', spurious1.mean())
	print('Y2: spurious = ', spurious2.mean())
	print('Y4: spurious = ', spurious4.mean())
	return (hits1.mean(), hits2.mean(), hits4.mean(),
		spurious1.mean(), spurious2.mean(), spurious4.mean())
	
	
def powersummary(dummy):
	
	plot.new()
	for i, blinksinbaseline in enumerate((True, False)):
		l1 = []
		l2 = []
		l4 = []
		ls1 = []
		ls2 = []
		ls4 = []
		effectsizes = range(0, 501, 50)
		for effectsize in effectsizes:
			kwargs = {
				'effectsize' : effectsize,
				'blfilter' : False,
				'blinksinbaseline' : blinksinbaseline				
				}
			cid = 'power-%(effectsize)s-%(blfilter)s-%(blinksinbaseline)s' % kwargs
			p1, p2, p4, s1, s2, s4 = power(None, cacheid=cid, **kwargs)
			l1.append(p1)
			l2.append(p2)
			l4.append(p4)
			ls1.append(s1)
			ls2.append(s2)
			ls4.append(s4)
		plt.subplot(2,2,i*2+1)
		if i == 0:
			plt.title('With blinks during baseline')
		else:
			plt.title('No blinks during baseline')		
		plt.axhline(.025, color='black', linestyle=':')
		plt.xlim(effectsizes[0]-10, effectsizes[-1]+10)
		plt.ylim(-.05, 1.05)
		plt.xlabel('True effect size')
		plt.ylabel('Proportion correct detections')
		plt.plot(effectsizes, l1, 'o-', label='No baseline correction',
			color=COLORNOCORRECT)
		plt.plot(effectsizes, l2, 'o-', label='Divide by baseline',
			color=COLORDIVIDE)
		plt.plot(effectsizes, l4, 'o-', label='Subtract baseline',
			color=COLORSUBTRACT)
		plt.subplot(2,2,i*2+2)
		plt.title('Spurious')
		plt.axhline(.025, color='black', linestyle=':')
		plt.xlim(effectsizes[0]-10, effectsizes[-1]+10)
		plt.ylim(-.05, 1.05)
		plt.xlabel('True effect size')
		plt.ylabel('Proportion spurious detections')		
		plt.plot(effectsizes, ls1, 'o-', label='No baseline correction',
			color=COLORNOCORRECT)
		plt.plot(effectsizes, ls2, 'o-', label='Divide by baseline',
			color=COLORDIVIDE)
		plt.plot(effectsizes, ls4, 'o-', label='Subtract baseline',
			color=COLORSUBTRACT)
		if i == 3:
			plt.legend(frameon=False, loc='lower right')
	plot.save('powersummary')
