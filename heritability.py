with open(origin.txt, 'r') as in_stream:
    print("Asking Darwin.")
    with open('output.txt', 'w') as out_stream:
        for line_index, line in enumerate(in_stream):