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


class DescendingOrderPriorityQueue(PriorityQueue, ABC):
    """Items with the highest priorities leave first"""
    pass


class AscendingOrderPriorityQueue(PriorityQueue, ABC):
    """Items with the lowest priorities leave first"""
    pass


def test_priority_queue(queue: PriorityQueue[int]) -> None:
    queue.insert_with_priority(2, 20)
    queue.insert_with_priority(3, 20)
    queue.insert_with_priority(1, 10)

    assert queue.peek_highest_priority() == 2
    assert queue.pop_highest_priority() == 2

    assert queue.peek_highest_priority() == 3
    assert queue.pop_highest_priority() == 3

    assert queue.peek_highest_priority() == 1
    assert queue.pop_highest_priority() == 1
    try:
        queue.pop_highest_priority()
    except EmptyPriorityQueueException:
        pass
    else:
        assert False, "No exception raised"
    print('tests passed')