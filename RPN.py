class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError('Стек пуст.')

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError('Стек пуст.')

    def size(self):
        return len(self.items)

def calculate_expression(expression):
    stack = Stack()
    if len(expression) < 3:
        return 'Слишком мало элементов. Должно быть минимум 3.'

    for token in expression:
        if token not in '+-*/':
            stack.push(float(token))
        else:
            if stack.size() < 2:  # Проверка, достаточно ли элементов для операции
                return 'Недостаточно элементов для выполнения операции.'

            second_to_last_token = stack.pop()
            last_token = stack.pop()
            if token == '+':
                stack.push(last_token + second_to_last_token)
            if token == '-':
                stack.push(last_token - second_to_last_token)
            if token == '*':
                stack.push(last_token * second_to_last_token)
            if token == '/':
                if second_to_last_token == 0:
                    return 'Ошибка: Деление на ноль.'
                stack.push(last_token / second_to_last_token)

    if stack.size() == 1:
        return stack.pop()
    return 'Ошибка: Некорректное выражение.'

if __name__ == '__main__':
    input_math_expression = input('Введите выражение. Поставьте пробел между элементами: ').split()
    print(calculate_expression(input_math_expression))
