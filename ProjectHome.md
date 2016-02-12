Simple python script used to convert dbf files to csv.

Usage:
python dbf2csv.py INPUT.dbf OUTPUT.csv PAGE\_SIZE

PAGE\_SIZE is optional
Number of records to include in each file.

This can be used to avoid very large files.

It splits the output in multiple files named OUTPUT.0.csv, OUTPUT.1.csv, OUTPUT.2.csv, OUTPUT.3.csv, etc..