from data_structures.abstract.stack import Stack, T, EmptyStackException, test_stack
from data_structures.linked_list import LinkedList, Node
from typing import Generic


class LinkedListStack(Stack, LinkedList, Generic[T]):

    def push(self, item: T) -> None:
        """ O(n) complexity"""
        self.insert(Node(item))

    def pop(self) -> T:
        """O(n) complexity"""
        if len(self) == 0:
            raise EmptyStackException()
        if len(self) == 1:
            node_to_return = self.head
            self.head = None
            self.size -= 1
            return node_to_return.value

        for idx, node in enumerate(self.node_iterator):
            if idx == len(self) - 2:  # Pre-last node needed to unlink last
                node_to_return = node.next_node
                node.next_node = None
                self.size -= 1
                return node_to_return.value


if __name__ == '__main__':
    test_stack(LinkedListStack[int]())
