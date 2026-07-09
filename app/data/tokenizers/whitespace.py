from collections.abc import Iterable

from .base import BaseTokenizer


class WhitespaceTokenizer(BaseTokenizer):
    """
    Simplest tokenizer.

    Example:
        "I love AI"

    becomes

        ["I", "love", "AI"]
    """

    def train(self, corpus: Iterable[str]) -> None:
        """
        No training required.
        """
        pass

    def tokenize(self, text: str) -> list[str]:
        return text.strip().split()

    def detokenize(self, tokens: list[str]) -> str:
        return " ".join(tokens)


if __name__ == "__main__":
    tokenizer = WhitespaceTokenizer()
    text = "I love AI"
    tokens = tokenizer.tokenize(text)
    print(tokens)
