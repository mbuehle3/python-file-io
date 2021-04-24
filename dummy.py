
# use the with statement with open to make sure that the object closes 

# .format() 
print('Opening dummy.txt')
with open('dummy.txt','r') as in_stream:
    print('Opening output.txt')
    with open('output.txt', 'w') as out_stream:
        for line_index, line in enumerate(in_stream):
            line = line.strip()
            word_list = line.split()
            word_list.sort()
            for word in word_list:
                out_stream.write('{0}\t{1}\n'.format(line_index, word))
print('Done!')
print('dummy.txt. is close?', in_stream.closed) 
print('output.txt is closed?', out_stream.closed)