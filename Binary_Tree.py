class Tree:
    # ініціалізація
    def __init__(self, data):
        self.data = data
        self.left = None
        self.rigt = None

    # додавання
    def add(self, val):
        if val < self.data:
            if self.left is None: 
                self.left = Tree(val)
            else: 
                self.left.add(val)
        elif val > self.data:
            if self.rigt is None: 
                self.rigt = Tree(val)
            else: 
                self.rigt.add(val)

    # виведення
    def output_from_above(self):
        print(self.data, end= " ")
        if self.left:
            self.left.output_from_above()
        if self.rigt:
            self.rigt.output_from_above()

    # переведення у список
    def list_sort_treet(self, x=[]):
        if self.left: self.left.list_sort_treet()
        if not self.data in x: x += [self.data]
        if self.rigt: self.rigt.list_sort_treet()
        return x

    # вирівнювання дерева
    def tree_alignment(self, arr=[], check = True):
        if check is True:
            arr = self.list_sort_treet()
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

def main():
    print("Приклад не гарного бинарного дерева:")
    array = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    tree = Tree(array[0])
    for val in array: tree.add(val)
    tree.output_from_above()
    print("\nНове дерево яке вірівнянно по центру:")
    tree.tree_alignment()
    tree.output_from_above()

if __name__ == '__main__':
    main()