class Tree:
    # Ініціалізація
    def __init__(self, data):
        self.data = data
        self.left = None
        self.rigt = None

    # Додавання
    def add(self, val):
        if val < self.data:
            if self.left is None: self.left = Tree(val)
            else: self.left.add(val)
        elif val > self.data:
            if self.rigt is None: self.rigt = Tree(val)
            else: self.rigt.add(val)

    # Видалення елементу
    def dell(self, val):
        arr = self.__list_tree()
        arr.remove(val)
        self.data = arr[0]
        self.left, self.rigt = None, None
        for i in arr: self.add(i)
    
    # Виведення
    def output_from_above(self):
        print(self.data, end= " ")
        if self.left: self.left.output_from_above()
        if self.rigt: self.rigt.output_from_above()

    # Переведення у список
    def __list_tree(self, x=[], chek = True):
        if chek is True: x = []
        x += [self.data]
        if self.left: self.left.__list_tree(x,False)
        if self.rigt: self.rigt.__list_tree(x,False)
        return x

    # Переведення у відсортований список
    def __list_sort_tree(self, x=[], chek = True):
        if chek is True: x = []
        if self.left: self.left.__list_sort_tree(x,False)
        x += [self.data]
        if self.rigt: self.rigt.__list_sort_tree(x,False)
        return x

    # Вирівнювання дерева
    def tree_alignment(self, arr = [], check = True):
        if check is True:
            arr = self.__list_sort_tree()
            self.data = arr[int(len(arr)/2)]
            self.left, self.rigt = None, None
        if len(arr)==1: self.add(arr[0])
        else:
            mid = int(len(arr)/2)
            self.add(arr[mid])
            righ = arr[mid:]
            left = arr[:mid]
            self.tree_alignment(righ,False)
            self.tree_alignment(left,False)
    
    # Виведення не через функцію
    def __repr__(self):
        return '['+', '.join([str(i)for i in self.__list_tree()])+']'


def main():
    print("Приклад не гарного бинарного дерева:")
    array = [0,1,2,3,4,5,6,7,8,9,]
    tree = Tree(array[0])
    for val in array: tree.add(val)
    tree.output_from_above()
    
    print("\nНове дерево яке вірівнянно по центру:")
    tree.tree_alignment()
    tree.output_from_above()
    
    print("\nВидалення елементу та виведення через repr:")
    tree.dell(5)
    tree.tree_alignment()
    print(tree)

if __name__ == '__main__':
    main()
