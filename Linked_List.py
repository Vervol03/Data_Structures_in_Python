from  random import randint

class Node:
    # вузел
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    # ініціалізація
    def __init__(self):
        self.head = None
    
    # додавання у початок
    def first(self, data):
        self.head = Node(data, self.head)      

    # додавання у кинець
    def add(self, data):
        if not self.head:
            self.head = Node(data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data)

    # виведеня останього вузла
    def last(self):
        n = self.head
        while n.next != None:
            n = n.next
        return n.data

    # перевірка на наявність вузлів
    def is_empty(self):
        return self.head == None
    
    # видаляємо повтори
    def del_repeat(self):
        n = self.head
        s = []
        while n != None:
            if not n.data in s: 
                s.append(n.data)
            n = n.next
        self.del_list()
        for i in s:
            self.add(i)
    
    # відсортовуємо
    def sort(self):
        n = self.head
        s = []
        while n != None: 
            s.append(n.data)
            n = n.next
        self.del_list()
        for i in sorted(s):
            self.add(i)
    
    # видаляємо повтори та відсортовуємо
    def del_repeat_sort(self):
        self.del_repeat()
        self.sort()

    # видаленя усіх вузлів
    def del_list(self):
        self.head = None
    
    # виведення усіх вузлів
    def print_list(self):
        n = self.head
        while n != None:
            print(n.data, end=" -> ")
            n = n.next
        print(None)

    # інструкція для виведення об'єкта 
    def __repr__(self):
        n = self.head
        s = ""
        while n != None:
            s += str(n.data)+" -> "
            n = n.next
        s += "None"
        return s

# Демонстрація можливостей створеного класу
x = LinkedList()
print("Виведеня звичайного связного списку: ")
for i in range(20): x.add(randint(1,9))
x.print_list()
print("Відсортовуємо та видалемо повтори: ")
x.del_repeat_sort()
print(x)