python 
import origin_parse as op
data = 'origin.txt'
text = op.read_text(data)
line = op.line_count(data)
line = op.by_line(text)