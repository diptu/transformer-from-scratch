# Convert integer token IDs into dense vectors that the Transformer can process.

from typing import cast

import numpy as np
from numpy.typing import NDArray


class Embedding:
    """
    Simple embedding layer implemented using NumPy.

    Parameters
    ----------
    vocab_size : int
        Number of tokens in the vocabulary.

    d_model : int
        Size of each embedding vector.
    """

    def __init__(self, vocab_size: int, d_model: int) -> None:
        self.vocab_size = vocab_size
        self.d_model = d_model

        # Learnable embedding matrix
        self.weight = np.random.randn(vocab_size, d_model)

    def forward(
        self, token_ids: np.ndarray | list[int] | list[list[int]]
    ) -> NDArray[np.float64]:
        """
        Convert token IDs into embedding vectors.

        Parameters
        ----------
        token_ids

        Single sequence:
            [2, 4, 5, 6, 3]

        Batch:
            [
                [2, 4, 5, 6, 3],
                [2, 8, 9, 1, 3],
            ]

        Returns
        -------
        Single sequence:
            (sequence_length, d_model)

        Batch:
            (batch_size, sequence_length, d_model)
        """

        token_ids = np.asarray(token_ids, dtype=np.int64)

        embeddings = self.weight[token_ids]
        return cast(NDArray[np.float64], embeddings)
