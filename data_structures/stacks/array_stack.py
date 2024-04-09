from data_structures.abstract.stack import Stack, T, EmptyStackException, test_stack
from typing import Generic


class ArrayStack(Stack, Generic[T]):

    def __init__(self):
        self._list = []  # yes, python list is not exactly array

    def push(self, item: T) -> None:
        """O(1) or O(n) complexity"""
        self._list.append(item)

    def pop(self) -> T:
        """O(1) complexity if current size is calculated with O(1) complexity"""
        try:
            return self._list.pop()
        except IndexError as e:
            raise EmptyStackException from e


if __name__ == '__main__':
    test_stack(ArrayStack[int]())
