from abc import ABC, abstractmethod


class BaseVocabulary(ABC):
    """Abstract vocabulary interface."""

    @abstractmethod
    def build(self, corpus: list[list[str]]) -> None:
        raise NotImplementedError

    @abstractmethod
    def encode(self, tokens: list[str]) -> list[int]:
        raise NotImplementedError

    @abstractmethod
    def decode(self, ids: list[int]) -> list[str]:
        raise NotImplementedError

    @property
    @abstractmethod
    def size(self) -> int:
        raise NotImplementedError
