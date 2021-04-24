python 
import origin_parse as op
import re
data = 'origin.txt'
r = re.compile(r'\bherit+\w*\b | \binherit+\w*\b', flags=re.I | re.X)
op.search(r, data, 'file.txt')
word
text = op.read_text(data)
line = op.line_count(data)
line = op.by_line(text)


text =op. read_text(data)
for line in text:
    line = line.strip("\n")
    word = line.split()
    line_number += 1
    if regex_pattern in word:
        print(word)
        results.append((line_number,word.rstrip()))
for word in text 
    word = text.split()

def index(filepath, keywords):
    with open(filepath) as f:
        for counter, line in enumerate(f, start = 1):
            if line.find(keywords) >= 0:
               print(keywords, counter)

r = re.compile(r'\bherit+\w*\b | \binherit+\w*\b, flags=re.I | re.X)

r = re.compile(r'\bherit+\w*\b | \binherit+\w*\b', flags=re.I | re.X)