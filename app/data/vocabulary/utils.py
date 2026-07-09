from .vocabulary import Vocabulary


def build_vocabulary(tokenized_corpus: list[list[str]]) -> Vocabulary:
    """
    Convenience helper for quickly building a vocabulary.
    """
    vocab = Vocabulary()
    vocab.build(tokenized_corpus)
    return vocab
