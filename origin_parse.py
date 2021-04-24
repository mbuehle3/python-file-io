import sys

def read_text(file):
    """
    Use function to read in a user defined text file
    """
    with open(file, 'r') as f:
        text = f.readlines()

    return text

def line_count(file):
    """
    Use this function to calculate the total number of lines in a file.
    INPUT:
    -----
    file = str of file to be processed
    """
    read_text(file)
    line_count = 0
    file = read_text(file)
    for line in file:
        line = line.strip("\n")
        line_count += 1
        print(line_count,':', line) # Can be used to print all lines in human readable format
    return line_count

def by_line(txt_obj):
    for line in txt_obj:
        line = line.strip("\n")
        line = print(line)
    return line

# def word_find(file, regex_pattern):
    
# print(s)

if __name__ == '__main__':
    if len(sys.argv)!= 2:
        sys.exit(sys.argv[0] + ": Expecting you to give me a text file to parse")
    text = open(sys.argv[1],'r')
