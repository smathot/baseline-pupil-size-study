#!/usr/bin/env python3
# coding=utf-8

import sys
from academicmarkdown import build, git
import myZoteroCredentials
import time
version = '1.2.1'
build.path += ['svg', 'md', 'tbl']
build.zoteroApiKey = myZoteroCredentials.zoteroApiKey
build.zoteroLibraryId = myZoteroCredentials.zoteroLibraryId
build.setStyle('apa')
build.docxRef = None
build.tableTemplate = 'pandoc'
build.pdfHeader = 'Manuscript in preparation [v%s; %s; %s]' % (version,
	time.strftime('%c'), git.commitHash().decode())
if '--snapshot' in sys.argv:
	git.exportFormats = 'pdf', 'docx'
	git.snapshot('md/__main__.md', msg=sys.argv[-1])
	build.DOCX('md/__coverletter__.md', 'latest-coverletter.docx')
else:
	build.PDF('md/__main__.md', 'latest-manuscript.pdf', lineNumbers=False)
	# build.setStyle('letter-classic')
	build.zoteroApiKey = None
	build.DOCX('md/__coverletter__.md', 'latest-coverletter.docx')
