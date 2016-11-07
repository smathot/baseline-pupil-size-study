#!/usr/bin/env python3
# coding=utf-8

from datamatrix import dispatch
from analysis import mainplots, data, power, interaction
import sys

if '--sim' in sys.argv:
	dm = data.generatedata(cacheid='data')
elif '--real' in sys.argv:
	dm = data.realdata()
else:
	raise Exception('Please specify --sim for simulated data or --real for real data')
dispatch.dispatch(dm, modules=[mainplots, power, interaction])
