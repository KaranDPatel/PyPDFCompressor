from __future__ import print_function
import os
import subprocess

for root, dirs, files in os.walk("C:\comp"):
    for file in files:
        if file.endswith(".pdf"):
            filename = os.path.join(root, file)
            print (filename)
            arg1= '-sOutputFile=' + "c" +  file #added a c to the filename
            p = subprocess.Popen(['C:/Program Files/gs/gs9.56.1/bin/gswin64c.exe',
                                  '-sDEVICE=pdfwrite', 
                                  '-dCompatibilityLevel=1.4', 
                                  '-dPDFSETTINGS=/screen', '-dNOPAUSE', 
                                  '-dBATCH', '-dQUIET', str(arg1), filename], 
                                 stdout=subprocess.PIPE)
            print (p.communicate())