class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f'{self.data} --> {self.next}'


if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    a.next = b
    print(a)
