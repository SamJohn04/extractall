# EXTRACTALL

Extractall is a program to extract all files from a directory and inner subdirectories into another destination directory.


## Prerequisites

- Python


## Usage Guide

Execute the program with the necessary arguments.

```
python3 main.py [--src <source-path>] [--dest <destination-path>] [--re <regex>] [--min-depth <min-depth>] [--max-depth <max-depth>] [--preserve-metadata]
```


## Flags

- The source and destination paths must be valid paths.
- If a regex is provided, the file names will be searched for the regex, and will only be extracted if found.
- The min and max depths, if provided, are expected to be integers >= 0. Only files that are at a depth from min to max depth will be extracted.
- The preserve-metadata flag attempts to preserve all file metadata, such as creation date.

