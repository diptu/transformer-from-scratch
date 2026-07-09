from collections.abc import Iterable

from .base import BaseTokenizer


class SentencePieceTokenizer(BaseTokenizer):
    """
    SentencePiece tokenizer.

    TODO:
        Implement from the SentencePiece paper
        and use in T5/LLaMA reproductions.
    """

    def train(self, corpus: Iterable[str]) -> None:
        raise NotImplementedError

    def tokenize(self, text: str) -> list[str]:
        raise NotImplementedError

    def detokenize(self, tokens: list[str]) -> str:
        raise NotImplementedError
