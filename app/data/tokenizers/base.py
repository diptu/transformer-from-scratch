from abc import ABC, abstractmethod
from collections.abc import Iterable


class BaseTokenizer(ABC):
    """
    Abstract tokenizer interface.
    """

    @abstractmethod
    def train(self, corpus: Iterable[str]) -> None:
        """
        Learn tokenizer-specific rules.

        Example:
        - WhitespaceTokenizer -> nothing to learn
        - BPE -> learn merges
        - WordPiece -> learn subwords
        """
        raise NotImplementedError

    @abstractmethod
    def tokenize(self, text: str) -> list[str]:
        """
        Convert text into tokens.
        """
        raise NotImplementedError

    @abstractmethod
    def detokenize(self, tokens: list[str]) -> str:
        """
        Convert tokens back into text.
        """
        raise NotImplementedError
