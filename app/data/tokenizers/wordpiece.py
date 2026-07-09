# BERT style
from collections.abc import Iterable

from .base import BaseTokenizer


class WordPieceTokenizer(BaseTokenizer):
    """
    WordPiece tokenizer.

    TODO:
        Implement from the BERT paper.
    """

    def train(self, corpus: Iterable[str]) -> None:
        raise NotImplementedError

    def tokenize(self, text: str) -> list[str]:
        raise NotImplementedError

    def detokenize(self, tokens: list[str]) -> str:
        raise NotImplementedError
