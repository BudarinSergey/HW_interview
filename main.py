class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        removed = self.stack[-1]
        self.stack.pop()
        return removed

    def peek(self):
        if not self.isEmpty():
            peek_item = self.stack[-1]
            return peek_item

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack.clear()


list_main = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '](()}{]{}', '{{[(])]}}', '[[{())}][']

BAL_DICT = {
    '(': ')',
    '[': ']',
    '{': '}'
}

def check_ballance(c_l):
    s = Stack()
    for i in c_l:
        if i in BAL_DICT:
            s.push(i)
            # print (s.stack)
        elif i == BAL_DICT.get(s.peek()):
            s.pop()
        else:
            return False
    return s.isEmpty()

if __name__ == '__main__':
    for c_l in list_main:
        print(f'{c_l:<30}{check_ballance(c_l)}')





