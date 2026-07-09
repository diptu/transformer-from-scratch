from app.data.tokenizers import WhitespaceTokenizer
from app.data.vocabulary import Vocabulary

if __name__ == "__main__":
    tokenizer = WhitespaceTokenizer()

    sentence = "I love AI"

    tokens = tokenizer.tokenize(sentence)

    # ["I", "love", "AI"]

    corpus = [
        tokenizer.tokenize("I love AI"),
        tokenizer.tokenize("Transformers are awesome"),
    ]

    vocab = Vocabulary()
    vocab.build(corpus)

    ids = vocab.encode(tokens)

    print(ids)

    print(vocab.decode(ids))
