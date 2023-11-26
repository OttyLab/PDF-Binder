## PDF Binder
PDF Binder picks up pages from multiple PDF files and merges them into single PDF file.

## How to use
0. Install dependencies
```shell
$ pip install -r requirements.txt
```

1. Prepare list file
```csv
abc.pdf,130,131-134,135
edf.pdf,101,140-150
```

2. Run command
```shell
$ python run.py list.csv output.pdf
```