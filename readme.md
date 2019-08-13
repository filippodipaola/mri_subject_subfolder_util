# Subject Subdirectory Utilities for MRI Analysis
This short script is used to help generated subject folders for MRI analysis results. The idea is prevent having an indiviual from having to manually create mutliple folders, in the correct format, for each of there subject analysis.
## Requirements
1. Python2.7 or higher (including Python3)

## Installation
* download or clone this whole repository into your machine, run the command and supply the correct arguments.

## Usage
```bash
usage: subdir_utils.py [-h] [-v] directory starting_number ending_number

Generates folder structure for results for different analysis

positional arguments:
  directory        Directory in which to create sub-xx folders
  starting_number  Starting value of x e.g. 3 inclusive
  ending_number    Ending value of x, e.g. 49 inclusive

optional arguments:
  -h, --help       show this help message and exit
  -v, --verbose    prints verbosely every action
```

