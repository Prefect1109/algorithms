from dataclasses import dataclass
from typing import Self, Optional


@dataclass
class Node[T]():

    value: T
    right: Optional[Self] = None
    left: Optional[Self] = None

    def __str__(self):
        return f'Node({self.value})'


@dataclass
class BinaryTree[T]():

    root_node: Optional[Node[T]] = None

    def insert(self, value: T) -> None:
        if self.root_node is None:
            self.root_node = Node(value)
            return
        current_node = self.root_node
        while True:
            
            if current_node.left is not None and value < current_node.left.value:
                current_node = current_node.left
                continue
            if current_node.right is not None and value > current_node.right.value:
                current_node = current_node.right
                continue
            
            if value < current_node.value:
                current_node.left = Node(value)
                break
            if value >= current_node.value:
                current_node.right = Node(value)
                break
            
    
    def delete(self, value: T) -> None:
        current_node = self.root_node
        previous_node = None
        while True:
            if current_node.left is not None and value <= current_node.left.value:
                previous_node = current_node
                current_node = current_node.left
                continue
            if current_node.right is not None and value >= current_node.right.value:
                previous_node = current_node
                current_node = current_node.right
                continue
            
            if current_node.value == value:
                if current_node.left is not None:
                    right_leaf = self._find_right_leaf(current_node.left)
                    right_leaf.right = current_node.right
                # if current_node.right is not None:
                #     right_leaf = self._find_right_leaf(current_node.right)
                #     right_leaf.left = current_node.right
                
                
                if previous_node is not None: 
                    previous_node.left = current_node.left
                    return
                self.root_node = current_node.left
                return
            

    def __contains__(self, value: T) -> bool:
        current_node = self.root_node
        while True:
            if current_node.left is not None and value <= current_node.left.value:
                current_node = current_node.left
                continue
            if current_node.right is not None and value >= current_node.right.value:
                current_node = current_node.right
                continue
            
            return current_node.value == value      

    def _find_right_leaf(self, node: Node[T]) -> Node[T]:
        current_node = node
        while True:
            if current_node.right is not None:
                current_node = current_node.right
                continue
            return current_node

    def __str__(self):
        res = ''

        if self.root_node is None:
            return "Binary three is empty"

        return res


if __name__ == '__main__':
    tree = BinaryTree()
    tree.insert(40)
    tree.insert(30)
    tree.insert(25)
    tree.insert(50)
    tree.insert(20)
    tree.insert(60)
    print(tree.root_node)
    print(tree.root_node.left)
    print(tree.root_node.right)
    print(tree.root_node.left.left)
    print(tree.root_node.right.right)
    print('deleting item')
    tree.delete(30)
    print(tree.root_node)
    print(tree.root_node.left)
    print(tree.root_node.right)
    # print(tree.root_node.left.left)
    print(tree.root_node.right.right)

    