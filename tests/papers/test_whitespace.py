import pytest

from app.data.tokenizers import WhitespaceTokenizer
from app.data.tokenizers.base import BaseTokenizer


@pytest.fixture
def tokenizer() -> BaseTokenizer:
    return WhitespaceTokenizer()


def test_train_does_not_raise(tokenizer: BaseTokenizer) -> None:
    tokenizer.train(["I love AI", "Transformers are amazing"])


def test_tokenize_simple_sentence(tokenizer: BaseTokenizer) -> None:
    text = "I love AI"
    expected = ["I", "love", "AI"]
    assert tokenizer.tokenize(text) == expected


def test_tokenize_multiple_spaces(tokenizer: BaseTokenizer) -> None:
    text = "I    love      AI"
    expected = ["I", "love", "AI"]
    assert tokenizer.tokenize(text) == expected


def test_tokenize_leading_and_trailing_spaces(tokenizer: BaseTokenizer) -> None:
    text = "   I love AI   "
    expected = ["I", "love", "AI"]
    assert tokenizer.tokenize(text) == expected


def test_tokenize_empty_string(tokenizer: BaseTokenizer) -> None:
    assert tokenizer.tokenize("") == []


def test_detokenize(tokenizer: BaseTokenizer) -> None:
    tokens = ["I", "love", "AI"]
    expected = "I love AI"
    assert tokenizer.detokenize(tokens) == expected


def test_round_trip(tokenizer: BaseTokenizer) -> None:
    text = "Transformers are awesome"
    reconstructed = tokenizer.detokenize(tokenizer.tokenize(text))
    assert reconstructed == text
