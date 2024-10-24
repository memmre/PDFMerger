from argparse import ArgumentParser
from datetime import datetime
from PyPDF2 import PdfMerger


def generate_filename(output_argument):
    if output_argument:
        if not output_argument.endswith('.pdf'):
            return f'{output_argument}.pdf'
        return output_argument
    return datetime.now().strftime('merged-%y%m%d-%H%M%S.pdf')


def merge_documents(documents, output_path):
    merger = PdfMerger()

    for i, document in enumerate(documents):
        print(f'Reading file {i+1} of {len(documents)} ({document})...')
        with open(document, 'rb') as input_file:
            merger.append(input_file)

    print(f'Merging files...')
    with open(output_path, 'wb') as output_file:
        merger.write(output_file)
    print(f'Merged files successfully as \'{output_path}\'.')


if __name__ == '__main__':
    parser = ArgumentParser(description='Merge multiple PDF files into a single PDF document.')
    parser.add_argument('input', nargs='+', help='Paths to the input PDF files to be merged.')
    parser.add_argument('-o', '--output', help='Path for the output PDF file.')

    args = parser.parse_args()
    output = generate_filename(args.output)
    merge_documents(args.input, output)
