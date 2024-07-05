from setuptools import setup, find_packages

setup(
    name='PDF_KEYWORD_SEARCHER',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'PyMuPDF',
    ],
    entry_points={
        'console_scripts': [
            'pdf-keyword-search = PDF_KEYWORD_SEARCHER.core:main',
        ],
    },
)

