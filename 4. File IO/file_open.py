with open('file_open.txt', 'r') as file:
    data = file.read()
    lines = data.split('\n')
    # print(lines)
    # print(type(lines))
    words = []
    for line in lines:
        words.extend(line.split(' '))
    print(words)
    print(len(words))
    
    unique_words = list(set(words))
    print(unique_words)
    print(len(unique_words))
    
