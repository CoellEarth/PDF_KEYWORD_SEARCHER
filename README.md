# PDF KEYWORD SEARCHER _Usage Guideline_
_This simple yet useful python package is developed by **Coell Shen** at [ZJU-UoE INSTITUTE](https://zje.zju.edu.cn/)_
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
### Analyzed Rusults
#### After running the example script
#### In the console: 
##### _(NOTE: queries in UPPER CASE)_
```
----------------------------------------------
在给定的文章中至少找到一个匹配的查询：
数量:2
{'GOLDEN RETRIEVER', 'BEAGLE'}
----------------------------------------------
在这些文章中找不到任何查询：
数量:1
{'BORDER COLLIE'}
-----------------------------------------------
所有查询的数量: 3
```
#### In the output file.txt
```
匹配成功的结果：
-------------------------------------
查找项 'Golden Retriever' 在文件 'paper1.pdf' 找到：'Animals such as tapeworms, golden retrievers, zebra fish, and pro-' 
查找项 'Golden Retriever' 在文件 'paper1.pdf' 找到：'recent study indicates that golden retrievers are essential constit-' 
查找项 'BEAGLES' 在文件 'paper2.pdf' 找到：'"I love them! I mean... the beagles", Lenden said sadly-' 
...
```
### Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue on GitHub.

### Contact
For any questions or suggestions, please contact Coell Shen at ZJE Institute at yuchen2.23@intl.zju.edu.cn.

