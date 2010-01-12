#!/usr/bin/env python

# Import Psyco if available
try:
    import psyco
    psyco.full()
except ImportError:
    pass

from dbfpy.dbf import Dbf
from constants.extensions import CSV

import sys
import argv
import parser

input = argv.input(sys.argv)
output = argv.output(sys.argv)
page_size = argv.page_size(sys.argv)

db = Dbf()
db.openFile(input, readOnly = 1)

# TODO: Real error handling
#try:

record_count = db.recordCount()

# If no record number is specified write everything
if(page_size == 0):
    page_size = record_count
    
pages = record_count / page_size

for page in xrange(pages):
    
    # TODO: replace the magic number with a calculated one 
    file_name = (output + str(page).zfill(3) + CSV)
    file = open(file_name, 'w')
    parser.header(db, file)
    parser.records(db, file, page_size * page, page_size)
    file.close()
        
#except:

db.close()