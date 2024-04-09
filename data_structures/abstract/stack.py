from abc import abstractmethod, ABC
from typing import TypeVar, Generic

T = TypeVar('T')


class EmptyStackException(Exception):
    pass


class Stack(ABC, Generic[T]):

    @abstractmethod
    def push(self, item: T) -> None:
        pass

    @abstractmethod
    def pop(self) -> T:
        """should raise EmptyStackException if stack is empty"""
        pass


def test_stack(stack: Stack[int]):
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    x = stack.pop()
    assert x == 1, x
    try:
        stack.pop()
    except EmptyStackException:
        pass
    else:
        assert False, "Exception expected"

    print(f"test stack completed successfully! {stack.__class__.__name__} is a valid stack")
