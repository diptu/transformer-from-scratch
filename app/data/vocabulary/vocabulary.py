from .base import BaseVocabulary
from .specials import SPECIAL_TOKENS, UNK_TOKEN


class Vocabulary(BaseVocabulary):
    """Simple word-level vocabulary."""

    def __init__(self) -> None:
        self.token_to_id: dict[str, int] = {}
        self.id_to_token: dict[int, str] = {}

        # Add special tokens first
        for token in SPECIAL_TOKENS:
            self._add_token(token)

    def _add_token(self, token: str) -> None:
        if token not in self.token_to_id:
            idx = len(self.token_to_id)
            self.token_to_id[token] = idx
            self.id_to_token[idx] = token

    def build(self, corpus: list[list[str]]) -> None:
        """
        corpus example:

        [
            ["I", "love", "AI"],
            ["Transformers", "are", "awesome"]
        ]
        """

        for sentence in corpus:
            for token in sentence:
                self._add_token(token)

    def encode(self, tokens: list[str]) -> list[int]:
        unk_id = self.token_to_id[UNK_TOKEN]

        return [self.token_to_id.get(token, unk_id) for token in tokens]

    def decode(self, ids: list[int]) -> list[str]:
        return [self.id_to_token[idx] for idx in ids]

    @property
    def size(self) -> int:
        return len(self.token_to_id)
