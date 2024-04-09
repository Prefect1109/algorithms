from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")


class EmptyQueueException(Exception):
    pass


class Queue(ABC, Generic[T]):

    @abstractmethod
    def enqueue(self, item: T) -> None:
        pass

    @abstractmethod
    def dequeue(self) -> T:
        """Should raise EmptyQueueException if queue is empty"""
        pass
