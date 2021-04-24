import sys
import re

def search(regex, doc, output = 'output.txt'):
    '''
    A function to search a file some matching regular expression

    INPUT 
    -------
    regex - an object that contains a compiled regular expression command 
    e.g, r = re.compile(r'\bherit+\w*\b | \binherit+\w*\b', flags=re.I | re.X)
    ------
    doc - a text file to be read in, needs to be provided as a string
    e.g, 'path/to/your/file.txt'
    ------
    output - a string containing the name of the output file
    e.g., 'output.txt'
    '''
    with open(doc, 'r') as in_stream:
        print('Parsing file',doc)
        with open(output, 'w') as out_stream:
            for line_num, line in enumerate(in_stream, 1):
                if regex.findall(line):
                    match = regex.search(line)
                    # print(match.group(0))
                    # print(match.group())
                    out_stream.write("{0}\t{1}\n".format(line_num, match.group()))
    print("Complete, information in",output)


if __name__ == '__main__':
    regex = re.compile(r'\bherit+\w*\b | \binherit+\w*\b', flags=re.I | re.X)
    doc = 'origin.txt'
    output = 'results.txt'
    search(regex,doc,output)