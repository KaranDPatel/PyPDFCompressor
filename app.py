from __future__ import print_function
import os
import subprocess
for root, dirs, files in os.walk("D:\PDF_Compressor\pdfsfiles"):
    for file in files:
        print(file)
        if file.endswith(".pdf"):
            filename = os.path.join(root, file)
            print(filename)
            arg1= "compressed_"+ file
            print(arg1)
            p = subprocess.Popen(['C:/Program Files/gs/gs9.56.1/bin/gswin64c.exe', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4', '-dPDFSETTINGS=/ebook', '-dNOPAUSE', '-dBATCH',  '-dQUIET', "-sOUTPUTFILE=D:\PDF_Compressor\compressed\{}".format(arg1), filename], stdout=subprocess.PIPE,shell=True)
            print (p.communicate())
            print('end/...')