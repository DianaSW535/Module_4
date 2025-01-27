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

TRUE_MESSAGE = 'Последовательность верна.'
FALSE_MESSAGE = 'Последовательность неверна.'
EMPTY_MESSAGE = 'Последовательность пуста.'

opening_parenthesis = ['(', '{', '[']
closing_parenthesis = [')', '}', ']']
valid_parentheses = set(opening_parenthesis + closing_parenthesis)

def checking_sequence(sequence):
    stack = Stack()
    if len(sequence) == 0:
        return EMPTY_MESSAGE
    if len(sequence) % 2 != 0 or not all(i in valid_parentheses for i in sequence):
        return FALSE_MESSAGE

    for symbol in sequence:
        if symbol in opening_parenthesis:
            stack.push(symbol)
        if symbol in closing_parenthesis:
            if stack.peek() != opening_parenthesis[closing_parenthesis.index(symbol)]:
                return FALSE_MESSAGE
            stack.pop()
            if stack.is_empty():
                return TRUE_MESSAGE

if __name__ == '__main__':
    input_sequence = input('Введите скобочную последовательность: ')
    print(checking_sequence(input_sequence))
