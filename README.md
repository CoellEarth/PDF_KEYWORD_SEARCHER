# PDF KEYWORD SEARCHER Usage Guideline

_This simple python script is developed by Coell Shen at ZJE Institute_

## Overview
PDF KEYWORD SEARCHER is a Python script designed to search for specific words within PDF documents located in a specified directory. The script extracts text from PDFs, searches for predefined patterns(keywords), and outputs the results to a text file. Additionally, it provides a summary of which patterns were found or not found in the documents and the number of patterns.

### How to Use

_1._ Down load the python script from my repo.

_2._ Set the directory, patterns, filepath... according to your specific needs.

_3._ Information about the matched keywords in the "pdf file tile" in a specific context(a part of the sentence) is output to the output file path which you can customize.

_4._ Information about how many and which of your wanted words to search, both matched and not matched is output to the console.

### Features
- Integrated with pymupdf[https://github.com/pymupdf/PyMuPDF].
- Extracts text from multiple PDF files in a directory.
- Searches for a list of predefined patterns within the extracted text.
- Outputs the results to a text file.
- Provides a summary of patterns found and not found in the documents.

## Requirements
- Python 3.x
- PyMuPDF (install using `pip install pymupdf`)
- re (regular expressions module, included in Python standard library)
- os (included in Python standard library)


