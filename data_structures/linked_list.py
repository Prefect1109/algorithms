from typing import Optional


class Node:
    def __init__(self, value: int, next_node: Optional["Node"] = None):
        self.value = value
        self.next_node = next_node


class LinkedList:

    def __init__(self, head: Optional[Node] = None):
        self.head = head

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next_node

    def __str__(self):
        string = "["

        is_empty = True
        for i in self:
            string += str(i)
            string += ", "
            is_empty = False
        if not is_empty:
            string = string[:-2]
        string += "]"
        return string

    def __len__(self):
        len = 0
        for i in self:
            len += 1
        return len

    def __getitem__(self, key):
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

    def insert(self, node: Node, at_index: Optional[int] = None):
        current = self.head
        if current is None:
            self.head = node
        elif at_index is None:
            while current:
                if current.next_node is None:
                    current.next_node = node
                    break
                current = current.next_node
        elif at_index > len(self) - 1:
            raise ValueError("Index out of range")
        elif at_index == 0:
            node.next_node = current
            self.head = node
        else:
            index = 0
            while current:
                if index + 1 == at_index:
                    node.next_node = current.next_node
                    current.next_node = node
                    break
                current = current.next_node
                index += 1

    def search(self, value: int, start_index: int = 0) -> int:
        search_source = self[start_index:]
        for index, node_value in enumerate(search_source):
            if value == node_value:
                return index + start_index
        raise ValueError("Item not found")


if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.insert(Node(1))
    linked_list.insert(Node(2))
    linked_list.insert(Node(3))

    print(linked_list)

    linked_list.insert(Node(4), at_index=1)

    print(linked_list)

    linked_list.insert(Node(5), at_index=0)

    print(linked_list)

    print(linked_list.search(3))

    linked_list.insert(Node(1), at_index=1)
    linked_list.insert(Node(1), at_index=3)
    linked_list.insert(Node(1), at_index=5)

    print(linked_list)

    print(linked_list.search(1))
    print(linked_list.search(1, start_index=1))
    print(linked_list.search(1, start_index=2))
    print(linked_list.search(1, start_index=4))

    # linked_list.insert(Node(6), at_index=10)

    # print(linked_list)
