class Queue:
    # Ініціалізація
    def __init__(self):
        self.list = []

    # Додавання
    def push(self, el):
        self.list.insert(0, el)

    # Вилученя
    def pop(self):
        return self.list.pop(0)

    # Перевірка на наявність елементів 
    def isElement(self):
        return True if self.list==[] else False
    
    # Виведення елементу по индексу
    def __getitem__(self, x):
        return self.list[len(self.list)-1] if x>len(self.list) else None

    # Кількість елементів у черзі
    def __len__(self):
        return len(self.list)
    
    # Виведення у форматі строки
    def __repr__(self):
        return "["+", ".join([str(i)for i in self.list])+"]"

# Виконання операцій
def operations(oper, x, y):
    if   oper=="+": return x+y
    elif oper=="-": return x-y
    elif oper=="*": return x*y
    elif oper=="/": return x/y

# Створюємо елементарний калькулятор (як на мові Lisp)
# Введеня виконується у форматі num num + num /
# Обов'язково між першими двома числами повинен бути відступ
# Далі відступи не обов'язкові але обов'язково потрібно 
# дотримуватися правил число операция и приклад закінчується на операцію
def main():
    x = Queue(); m = ''
    s = input("Ваедіть приклад: ")
    for i in ["+","-","*","/"]:
        s = s.replace(i," "+i+" ")
    s = s.replace("  ", " ").strip()
    for i in s:
        if   i == "+": x.push(operations("+", x.pop(), x.pop()))
        elif i == "-": x.push(operations("-", x.pop(), x.pop()))
        elif i == "*": x.push(operations("*", x.pop(), x.pop()))
        elif i == "/": x.push(operations("/", x.pop(), x.pop()))
        else:
            if i==" ":
                if m!='': x.push(float(m)); 
                m = ''
            else: m += i

    print("Результат: ", x.pop())
    
if __name__ == '__main__':
    main()
