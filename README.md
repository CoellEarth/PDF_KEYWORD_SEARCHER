# PDF KEYWORD SEARCHER Usage Guideline

_This simple python package is developed by Coell Shen at ZJE Institute_

## Overview
PDF KEYWORD SEARCHER is a Python script designed to search for specific words within PDF documents located in a specified directory. The script extracts text from PDFs, searches for predefined patterns(keywords), and outputs the results to a text file. Additionally, it provides a summary of which patterns were found or not found in the documents and the number of patterns.

## Features
- Integrated with [pymupdf](https://github.com/pymupdf/PyMuPDF).
- Extracts text from multiple PDF files in a directory.
- Searches for a list of predefined patterns within the extracted text.
- Outputs the results to a text file.
- Provides a summary of patterns found and not found in the documents.

## Requirements
- Python 3.x
- PyMuPDF (install using `pip install pymupdf`)
- re (regular expressions module, included in Python standard library)
- os (included in Python standard library)

## How to Use

### Installation in Mac (command line in terminal)

```ruby
pip3 install git+https://github.com/CoellEarth/PDF_KEYWORD_SEARCHER.git
```

### Update in Mac (command line in terminal)

```ruby
pip3 install --upgrade git+https://github.com/CoellEarth/PDF_KEYWORD_SEARCHER.git
```

### Usage (in python)

```ruby
from PDF_KEYWORD_SEARCHER import search_in_pdfs, analyze_results

# Define the dir in which you store all the pdf files that include the keywords of interest
directory = "/Users/coellearth/Desktop/Cute Dogs"

# Define the output txt file path
output_file_path = "/Users/coellearth/Desktop/output.txt"

# Define the list of keywords you want to search
patterns = ["Golden Retriever", "BEAGLE", "border collie"]

# Standard codeline which you do not need to change
results = search_in_pdfs(directory, patterns)
analyze_results(results, output_file_path, patterns)
```

