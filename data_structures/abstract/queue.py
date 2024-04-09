from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")


class AbstractQueue(ABC, Generic[T]):

    @abstractmethod
    def put(self, item: T):
        pass

    @abstractmethod
    def pop(self) -> T:
        pass

    @abstractmethod
    def remove(self, item: T):
        pass
