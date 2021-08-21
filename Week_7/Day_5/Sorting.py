def sort_list():
    sequence = input("Write a comma separated sequence of words: ")
    sequence = sequence.split(',')
    sequence.sort()
    print(','.join(sequence))
sort_list()
