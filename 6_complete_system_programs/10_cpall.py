""" 
    ########################################################################################################
    Usage: "Python pall.py dirFrom dirTo",
    Recursive copy of a directory tree. Works like a "cp -r dirFrom/* dirTo"
    Unix command, and assumes that dirFrom and dirTo are both directories.
    Was written to get around fatal error messages under Windows drga-and-drop
    copies (the first ad file ends the entire copy operation immediately),
    but also allows for coding more customized copy operations in Python.
    ########################################################################################################
"""

import os, sys 
maxfileload = 1000000
blksize = 1024 * 500

def copyfile(pathFrom, pathTo, maxfileload=maxfileload):
    """ 
        Copy one file pathFrom to pathTo, byte for byte;
        uses binary file modes to supress Unicode decode and endline transform
    """
    if os.path.getsize(pathFrom) <= maxfileload:
        bytesFrom = open(pathFrom, 'rb').read()         # read small file all at once
        open(pathTo, 'wb').write(bytesFrom)
    else:
        fileFrom = open(pathFrom, 'rb')                 # read big file in chunks
        fileTo = open(pathTo, 'wb')                     # need b mode for both
        while True:
            bytesFrom = fileFrom.read(blksize)          # get one block, less at end
            if not bytesFrom: break                     # empty after last chunk
            fileTo.write(bytesFrom)