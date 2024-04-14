from data_structures.abstract.priority_queue import PriorityQueue, T, EmptyPriorityQueueException, test_priority_queue
from typing import Generic
from collections import defaultdict


class ArrayPriorityQueue(PriorityQueue, Generic[T]):

    def __init__(self):
        self.sorted_priorities: list[int] = []
        self.priority_to_value_map: dict[int, list[T]] = defaultdict(list)

    def _sorted_insert_priority(self, priority: int):
        # O(n)
        if not self.sorted_priorities:
            self.sorted_priorities.append(priority)
            return

        for idx, item in enumerate(self.sorted_priorities):
            if item > priority:
                break
        else:
            self.sorted_priorities.append(priority)
            return
        self.sorted_priorities.insert(idx, priority)

    def pop_highest_priority(self) -> T:
        # O(1)
        try:
            return self.priority_to_value_map[self.sorted_priorities.pop()].pop()
        except IndexError:
            raise EmptyPriorityQueueException()


    def peek_highest_priority(self) -> T:
        # O(1)
        try:
            return self.priority_to_value_map[self.sorted_priorities[-1]][-1]
        except IndexError:
            raise EmptyPriorityQueueException()

    def insert_with_priority(self, item: T, priority: int) -> None:
        # O(n)
        self._sorted_insert_priority(priority)
        self.priority_to_value_map[priority].insert(0, item)


if __name__ == '__main__':
    test_priority_queue(ArrayPriorityQueue[int]())
