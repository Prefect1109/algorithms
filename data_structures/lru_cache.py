from typing import Optional, TypeVar, Generic, Union, Iterator, Hashable

K = TypeVar('K', bound=Hashable)
V = TypeVar('V')


class LRUCache(Generic[K, V]):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = {}
        self.queue: list[K] = []

    def put(self, key: K, value: V):
        if key in self.storage:  # Get index
            self.queue.remove(key)
        else:
            if len(self.queue) == self.capacity:
                del self.storage[self.queue.pop()]

        self.storage[key] = value
        self.queue = [key] + self.queue

    def get(self, key: K) -> V:
        if key not in self.storage:
            raise ValueError("key is not in storage")

        self.queue.remove(key)
        self.queue = [key] + self.queue

        return self.storage[key]


def test_put():
    cache = LRUCache[int, int](capacity=3)
    cache.put(key=1, value=10)
    cache.put(key=2, value=20)
    cache.put(key=3, value=30)
    print(cache.queue)
    assert cache.queue == [3, 2, 1]

    cache.put(key=1, value=10)
    cache.put(key=4, value=40)
    print(cache.queue)
    assert cache.queue == [4, 1, 3]


def test_get():
    cache = LRUCache[int, int](capacity=3)
    cache.put(key=1, value=10)
    cache.put(key=2, value=20)
    cache.put(key=3, value=30)
    print(cache.queue)
    assert cache.queue == [3, 2, 1]

    cache.get(key=1)
    cache.put(key=4, value=40)
    print(cache.queue)
    assert cache.queue == [4, 1, 3]


if __name__ == '__main__':
    test_put()
    test_get()
