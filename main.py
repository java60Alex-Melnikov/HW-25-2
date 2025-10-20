class MyStackInt:
    def __init__(self):
        self._stack = []
        self._max_stack = []

    def push(self, num: int):
        self._stack.append(num)
        if not self._max_stack or num >= self._max_stack[-1]:
            self._max_stack.append(num)
    
    def pop(self) -> int:
        if not self._stack:
            raise IndexError("pop from empty stack")
        num = self._stack.pop()
        if num == self._max_stack[-1]:
            self._max_stack.pop()
        return num
    
    def max(self) -> int:
        if not self._max_stack:
            raise IndexError("max from empty stack")
        return self._max_stack[-1]
