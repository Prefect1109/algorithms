from data_structures.abstract.priority_queue import PriorityQueue, T, EmptyPriorityQueueException, test_priority_queue
from typing import Generic


class ArrayPriorityQueue(PriorityQueue, Generic[T]):
    def __init__(self):
        self.sorted_priorities: list[int] = []
        self.priorities_values: dict[int, list[T]] = {}

    def insert_with_priority(self, item: T, priority: int):
        # O(n)
        if len(self.sorted_priorities) == 0:
            self.sorted_priorities.append(priority)
            self.priorities_values[priority] = [item]
        else:
            for index, stored_priority in enumerate(self.sorted_priorities):
                if priority == stored_priority:
                    items = self.priorities_values[priority]
                    items.append(item)
                    self.priorities_values[priority] = items
                    break
                if priority < stored_priority:
                    self.sorted_priorities.insert(index, priority)
                    self.priorities_values[priority] = [item]
                    break
            else:
                self.sorted_priorities.append(priority)
                self.priorities_values[priority] = [item]

    def pop_highest_priority(self) -> T:
        # O(1)
        if not self.sorted_priorities:
            raise EmptyPriorityQueueException
        key = self.sorted_priorities[-1]
        items = self.priorities_values.get(key)
        item = items[0]
        if len(items) > 1:
            items.remove(item)
            self.priorities_values[key] = items
        else:
            del self.priorities_values[key]
            self.sorted_priorities.pop()
        return item

    def peek_highest_priority(self) -> T:
        # O(1)
        if not self.sorted_priorities:
            raise EmptyPriorityQueueException
        key = self.sorted_priorities[-1]
        items = self.priorities_values.get(key)
        item = items[0]
        return item


if __name__ == '__main__':
    test_priority_queue(ArrayPriorityQueue[int]())
