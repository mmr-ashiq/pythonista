with open('file_write.txt', 'w') as file:
    data = input('Enter data: ')
    file.write(data)


with open('file_write.txt', 'r') as file:
    data = file.read()
    print(data)