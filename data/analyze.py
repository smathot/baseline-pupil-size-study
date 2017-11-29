#!/usr/bin/env python3
# coding=utf-8

from datamatrix import dispatch
from datamatrix._datamatrix._index import Index
from analysis import mainplots, data, power, interaction, reconstruct
import sys

if '--sim' in sys.argv:
	dm = data.generatedata(cacheid='data')
elif '--real' in sys.argv:
	dm = data.realdata()
else:
	raise Exception(
		'Please specify --sim for simulated data or --real for real data')
# Fix cached old-style datamatrix
if not isinstance(dm._rowid, Index):
	object.__setattr__(dm, '_rowid', Index(dm._rowid))

dispatch.dispatch(dm, modules=[mainplots, power, interaction, reconstruct])
