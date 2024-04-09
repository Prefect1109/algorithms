from typing import Optional, TypeVar, Generic, Union, Iterator

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, value: T, next_node: Optional["Node[T]"] = None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)


class LinkedList(Generic[T]):

    def __init__(self, head: Optional[Node[T]] = None):
        self.head = head
        self.size = 1 if head else 0

    def __iter__(self):
        for node in self.node_iterator:
            yield node.value

    @property
    def node_iterator(self) -> Iterator[Node[T]]:
        current = self.head
        while current:
            yield current
            current = current.next_node

    def __str__(self):
        return ' -> '.join(map(str, self))

    def __len__(self):
        return self.size

    def __getitem__(self, key: Union[slice, int]) -> Union[T, 'LinkedList[T]']:
        if isinstance(key, slice):
            _linked_list = LinkedList()
            start = key.start if key.start else 0
            stop = key.stop if key.stop else len(self)
            for index, value in enumerate(self):
                if start <= index < stop:
                    _linked_list.insert(Node(value))
            return _linked_list
        elif isinstance(key, int):
            if key < 0:  # Handle negative indices
                key += len(self)
            if key < 0 or key >= len(self):
                raise ValueError("The index (%d) is out of range." % key)

            for index, value in enumerate(self):
                if key == index:
                    return value
        else:
            raise ValueError("Invalid argument type.")

    def insert(self, node: Node[T], at_index: Optional[int] = None) -> None:
        """O(n) complexity"""

        if at_index is not None and at_index > len(self):
            raise ValueError("Index out of range")

        if at_index is None:
            at_index = len(self)

        self.size += 1

        if self.head is None:
            self.head = node
            return

        if at_index == 0:
            node.next_node = self.head
            self.head = node
            return

        for idx, current_node in enumerate(self.node_iterator):
            if idx + 1 == at_index:
                node.next_node = current_node.next_node
                current_node.next_node = node
                return

    def search(self, value: int, start_index: int = 0) -> int:
        # Optimization to not perform slicing when unnecessary
        search_source_list = self if start_index == 0 else self[start_index:]
        for index, node_value in enumerate(search_source_list):
            if value == node_value:
                return index + start_index
        raise ValueError("Item not found")


if __name__ == '__main__':
    int_linked_list = LinkedList[int]()
    str_linked_list = LinkedList[str]()

    str_node = Node("1")
    int_node = Node(1)
    str_linked_list.insert(str_node)
    int_linked_list.insert(int_node)
    # str_linked_list.insert(int_node)  # editor highlights as error

    int_linked_list.insert(Node(2))
    int_linked_list.insert(Node(3))

    assert list(int_linked_list) == [1, 2, 3]

    int_linked_list.insert(Node(5), at_index=0)
    int_linked_list.insert(Node(4), at_index=2)
    assert list(int_linked_list) == [5, 1, 4, 2, 3]
    assert int_linked_list.search(5) == 0
    assert int_linked_list.search(4) == 2

    int_linked_list.insert(Node(5))
    assert int_linked_list.search(5, start_index=2) == len(int_linked_list) - 1, int_linked_list.search(5, start_index=2)
