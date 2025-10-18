class MyStackInt:
    def __init__(self):
        self._stack = []
        self._max_stack = []

    def push(self, num: int):
        self._stack.append(num)
        if not self._max_stack or num >= self._max_stack[-1]:
            self._max_stack.append(num)
        else:
            self._max_stack.append(self._max_stack[-1])
    
    def pop(self) -> int:
        if not self._stack:
            raise IndexError("pop from empty stack")
        self._max_stack.pop()
        return self._stack.pop()