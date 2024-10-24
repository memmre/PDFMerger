# PDF Merger

This Python script allows you to merge multiple PDF files into a single PDF document. You can specify the input PDF files and optionally provide a custom output filename.

## Features

- Merges multiple PDF documents into one.
- Automatically generates a timestamped output filename if no custom name is provided.
- Supports specifying the output file path with the `-o` or `--output` argument.

## Requirements

To run this script, you need the following libraries:

- `argparse` (standard library)
- `datetime` (standard library)
- `PyPDF2` (for handling PDF files)

Install the required external package by running:

```bash
pip install PyPDF2
```

## Usage

You can use the script from the command line by specifying the PDF files you want to merge.

### Basic Usage

```bash
python pdfmerger.py input1.pdf input2.pdf
```

This will merge the given PDF files and output a file named in the format merged-YYMMDD-HHMMSS.pdf (e.g., merged-241025-121530.pdf).

### Custom Output Name

If you want to specify a custom name for the output file, use the -o or --output flag:

```bash 
python pdfmerger.py input1.pdf input2.pdf -o output.pdf 
```

The output file will be named output.pdf.

## Notes

• The script will print progress as it processes each PDF file and will confirm once the merge is successful.<br>
• If the output file path is not provided, the script will automatically generate a filename based on the current date and time.
