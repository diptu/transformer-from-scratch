from typing import cast

import numpy as np
from numpy.typing import NDArray


class PositionalEncoding:
    """
    Sinusoidal Positional Encoding
    (Attention Is All You Need, 2017)

    Parameters
    ----------
    d_model : int
        Embedding dimension.

    max_length : int
        Maximum supported sequence length.
    """

    def __init__(self, d_model: int, max_length: int = 5000):
        self.d_model = d_model
        self.max_length = max_length

        self.encoding = self._build_encoding()

    def _build_encoding(self) -> np.ndarray:
        """
        Create positional encoding matrix.

        Shape
        -----
        (max_length, d_model)
        """

        encoding = np.zeros(
            (self.max_length, self.d_model),
            dtype=np.float32,
        )

        position = np.arange(self.max_length).reshape(-1, 1)

        div_term = np.exp(
            np.arange(0, self.d_model, 2) * (-np.log(10000.0) / self.d_model)
        )

        encoding[:, 0::2] = np.sin(position * div_term)
        encoding[:, 1::2] = np.cos(position * div_term)

        return encoding

    def forward(self, embeddings: np.ndarray) -> np.ndarray:
        """
        Add positional encoding.

        Parameters
        ----------
        embeddings

        Shape
        -----
        (batch_size, sequence_length, d_model)

        Returns
        -------
        Same shape as input.
        """

        sequence_length = embeddings.shape[1]

        embeddings + self.encoding[:sequence_length]
        return cast(NDArray[np.float64], embeddings)
