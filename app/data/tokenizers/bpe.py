# GPT/GPT-2 style
from collections.abc import Iterable

from .base import BaseTokenizer


class BPETokenizer(BaseTokenizer):
    """
    Byte Pair Encoding tokenizer.

    TODO:
        Implement from the GPT/GPT-2 papers.
    """

    def train(self, corpus: Iterable[str]) -> None:
        raise NotImplementedError

    def tokenize(self, text: str) -> list[str]:
        raise NotImplementedError

    def detokenize(self, tokens: list[str]) -> str:
        raise NotImplementedError
