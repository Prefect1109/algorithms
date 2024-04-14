from dataclasses import dataclass
from typing import TypeVar, Generic, Optional
from custom_types import Comparable
from enum import Enum

T = TypeVar('T', bound=Comparable)


class DirectionEnum(str, Enum):
    LEFT = 'left'
    RIGHT = 'right'


@dataclass
class Node(Generic[T]):

    value: T
    count: int = 1
    right: Optional['Node'[T]] = None
    left: Optional['Node'[T]] = None

    def _raise_no_direction_exception(self, direction: DirectionEnum):
        raise ValueError(f"No direction {direction}")

    def get_node_by_direction(self, direction: DirectionEnum) -> Optional[T]:
        if direction == DirectionEnum.RIGHT:
            return self.right
        if direction == DirectionEnum.LEFT:
            return self.left
        self._raise_no_direction_exception(direction)

    def add_node_by_direction(self, direction: DirectionEnum, node: 'Node'[T]) -> None:
        if direction == direction.LEFT:
            self.left = node
            return
        if direction == direction.RIGHT:
            self.right = node
            return
        self._raise_no_direction_exception(direction)

    def attached_nodes(self) -> list['Node'[T]]:
        return list(
            filter(
                lambda item: item is not None,
                [self.left, self.right]
            )
        )

    def __bool__(self):
        return self.value is not None

    def __str__(self):
        return f'Node({self.value}, {self.count})'


@dataclass
class BinaryTree(Generic[T]):

    root_node: Optional[Node[T]] = None

    def insert(self, value: T) -> None:
        if self.root_node is None:
            self.root_node = Node(value)
            return

        current_node = self.root_node
        while True:

            if current_node.value > value:
                direction = DirectionEnum.LEFT
            elif current_node.value == value:
                current_node.count += 1
                return
            else:
                direction = DirectionEnum.RIGHT

            next_node = current_node.get_node_by_direction(direction)
            if next_node:
                current_node = next_node
                continue
            current_node.add_node_by_direction(direction, Node(value))
            return

    def delete(self, value):
        pass

    def __contains__(self, item: T) -> bool:
        pass

    def __str__(self):
        res = ''

        if self.root_node is None:
            return "Binary three is empty"

        return res

