# coding=utf-8

import sys
from matplotlib import pyplot as plt
from datamatrix import plot
from analysis.constants import *
from analysis import baseline


def plotmean(dm, col):
	
	plot.trace((dm.c == 1)[col], color=COLOR1)
	plot.trace((dm.c == 2)[col], color=COLOR2)
	plt.xlabel('Time (ms)')
	plt.ylabel('Pupil size')


def plotindividual(dm, col):

	# if col == 'y':
	# 	plt.ylim(0,3000)
	# elif col == 'y2':
	# 	plt.ylim(0,12)
	# elif col == 'y4':
	# 	plt.ylim(-2500,2000)
	for row in dm:
		if '--real' in sys.argv and row.bl < MIN_BASELINE:
			linestyle = ':'
		else:
			linestyle = '-'
		color = COLOR1 if row.c == 1 else COLOR2		
		plt.plot(row[col], color=color, alpha=ALPHA, linestyle=linestyle)
	plt.xlabel('Time (ms)')
	plt.ylabel('Pupil size')
		
		
def plotstd(dm, col):

	plt.plot((dm.c == 1)[col].std, color=COLOR1)
	plt.plot((dm.c == 2)[col].std, color=COLOR2)
	
	
def plotall(dm, col, i, title):
	
	plt.subplot(PLOTS,2,i*2+1)
	plotmean(dm, col)
	plt.subplot(PLOTS,2,i*2+2)
	plotindividual(dm, col)
	# plt.ylim(0, 1.1)
	
	
def mainplots(dm):
		
	plot.new()
	dm.bl = baseline.baseline(dm)
	dm.y2 = baseline.correct1(dm)
	dm.y4 = baseline.correct3(dm)
	plotall(dm, 'y', 0, title='No baseline correction')
	plotall(dm, 'y2', 1, title='Divide by baseline')
	plotall(dm, 'y4', 2, title='Subtrace baseline')
	if '--sim' in sys.argv:
		plot.save('main-sim')
	elif '--real' in sys.argv:
		plot.save('main-real')
		
		
def filteredplot(dm):

	dm.bl = baseline.baseline(dm)
	dm.y2 = baseline.correct1(dm)
	dm.y4 = baseline.correct3(dm)
	dm = dm.bl >= MIN_BASELINE
	plot.new(size=(8, 3))
	plt.subplot(121)
	plotmean(dm, 'y2')
	plt.subplot(122)
	plotmean(dm, 'y4')
	plot.save('filteredplot')


def histogram(dm):

	
	dm.bl = baseline.baseline(dm)		
	plot.new(size=(8,4))
	y, x = np.histogram(dm.bl, bins=50, range=(0,4000))
	x =.5*x[1:]+.5*x[:-1]
	plt.subplot(121)
	plt.xlabel('Baseline pupil size')
	plt.ylabel('N')	
	plt.fill_between(x, y)
	plt.xlim(0, 3000)
	plt.axvline(MIN_BASELINE, color='black', linestyle=':')
	plt.subplot(122)
	plt.xlabel('Baseline pupil size')
	plt.ylabel('log10(N)')
	plt.fill_between(x, np.log10(y))
	plt.xlim(0, 3000)	
	plt.axvline(MIN_BASELINE, color='black', linestyle=':')
	plot.save('baseline-hist')
	
