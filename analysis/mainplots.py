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
	
	for row in dm:
		color = COLOR1 if row.c == 1 else COLOR2
		plt.plot(row[col], color=color, alpha=ALPHA)
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
	
	
def mainplots(dm):
		
	plot.new()
	dm.y2 = baseline.correct1(dm)
	dm.y3 = baseline.correct2(dm)
	dm.y4 = baseline.correct3(dm)
	plotall(dm, 'y', 0, title='No baseline correction')
	plotall(dm, 'y2', 1, title='Divide by baseline')
	plotall(dm, 'y4', 2, title='Subtrace baseline')
	if '--sim' in sys.argv:
		plot.save('main-sim')
	elif '--real' in sys.argv:
		plot.save('main-real')
