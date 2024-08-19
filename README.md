**PDF Compressor Using Ghostscript**

**Overview**

This project provides an automated solution for compressing PDF files using Ghostscript. The script traverses through a specified directory, identifies PDF files, and compresses them to reduce their file size, making it easier to store and share large PDF documents.

**Features**

Automated PDF Compression: Compresses all PDF files in a specified directory automatically.

Ghostscript Integration: Leverages Ghostscript for high-quality PDF compression with configurable settings.

Batch Processing: Handles multiple PDF files in a directory, compressing each one and saving the output to a specified location.

Customizable Compression Level: Uses Ghostscript's /ebook setting by default, but this can be adjusted for different levels of compression.

**Prerequisites**

Python 3.x installed on your system.
Ghostscript installed on your system.
Download and install Ghostscript from here.

**Installation**
Clone the Repository:

sh
Copy code
git clone url
cd pdf-compressor
Set Up Ghostscript:

Ensure that the Ghostscript executable (gswin64c.exe) is correctly installed and accessible from the specified path in the script.
Directory Structure:

Place the PDF files you want to compress in the pdfsfiles directory.
The compressed PDFs will be saved in the compressed directory.
Usage
Run the PDF Compression Script:

sh
Copy code
python pdf_compressor.py
Process Overview:

The script will traverse the pdfsfiles directory, identify all PDF files, compress them using Ghostscript, and save the compressed files to the compressed directory.
Customization:

Modify the -dPDFSETTINGS parameter in the Ghostscript command for different compression levels:
/screen — low-resolution output similar to screen-view.
/ebook — medium-resolution output similar to eBook.
/printer — high-resolution output similar to printing.
/prepress — output similar to prepress quality.
File Structure
graphql
Copy code
pdf-compressor/

│

├── pdf_compressor.py        # Main script for compressing PDF files

├── pdfsfiles/               # Directory containing PDFs to compress

├── compressed/              # Directory to store compressed PDFs

├── README.md                # This readme file

└── requirements.txt         # List of Python dependencies (if applicable)

**Benefits**

Efficiency: Quickly compresses multiple PDF files to reduce storage space.

Quality Control: Offers different levels of compression to balance file size and quality.

Automation: Automates the process of PDF compression, making it easy to handle large batches of files.
