from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class EmptyPriorityQueueException(Exception):
    pass


class PriorityQueue(ABC, Generic[T]):

    @abstractmethod
    def insert_with_priority(self, item: T, priority: int) -> None:
        pass

    @abstractmethod
    def pop_highest_priority(self) -> T:
        """should raise EmptyPriorityQueueException if queue is empty"""
        pass

    @abstractmethod
    def peek_highest_priority(self) -> T:
        """should raise EmptyPriorityQueueException if queue is empty"""
        pass


class DescendingOrderPriorityQueue(ABC, PriorityQueue):
    """Items with the highest priorities leave first"""
    pass


class AscendingOrderPriorityQueue(ABC, PriorityQueue):
    """Items with the lowest priorities leave first"""
    pass
