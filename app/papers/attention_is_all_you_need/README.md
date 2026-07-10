
# Implementation Plan:
> 7-day plan centered on sentence translation

| Day       | Focus                                    | Files                                                                                                            | Deliverable                                                                                                                                                                                   |
| --------- | ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Day 1** | **Data Pipeline & Input Representation** | `tokenizer.py`<br>`vocabulary.py`<br>`dataset.py`<br>`collate.py`<br>`embeddings.py`<br>`positional_encoding.py` | Load a small parallel corpus, tokenize source and target sentences, build vocabularies, convert to token IDs, create padded batches, and produce embedding tensors with positional encodings. |
| **Day 2** | **Scaled Dot-Product Attention**         | `attention.py`                                                                                                   | Implement Scaled Dot-Product Attention (`Q`, `K`, `V`, scaling, masking, softmax). Validate it on toy tensors before integrating it into the model.                                           |
| **Day 3** | **Multi-Head Attention**                 | `multi_head_attention.py`                                                                                        | Implement multi-head attention by splitting into heads, applying attention in parallel, concatenating, and projecting back to `d_model`. Test with batched inputs.                            |
| **Day 4** | **Transformer Encoder**                  | `feed_forward.py`<br>`layer_norm.py`<br>`residual.py`<br>`encoder_layer.py`<br>`encoder.py`                      | Build the encoder stack: embeddings → positional encoding → N encoder layers. Verify the encoder produces contextualized representations of the source sentence.                              |
| **Day 5** | **Transformer Decoder**                  | `masks.py`<br>`decoder_layer.py`<br>`decoder.py`                                                                 | Implement masked self-attention, encoder–decoder attention, and the decoder stack. Feed the target sentence shifted right (`<BOS> ...`) and verify output shapes.                             |
| **Day 6** | **Complete Transformer & Training**      | `model.py`<br>`loss.py`<br>`trainer.py`                                                                          | Assemble the full encoder–decoder Transformer, add the final linear projection to vocabulary logits, compute cross-entropy loss, and train on a small translation dataset.                    |
| **Day 7** | **Inference & Translation**              | `greedy_decode.py`<br>`beam_search.py` (optional)<br>`translate.py`                                              | Implement greedy decoding. Translate new English sentences into the target language and inspect attention weights and predictions.                                                            |


End-of-day milestones
Day 1

English Sentence
        │
        ▼
Tokenizer
        │
        ▼
Vocabulary
        │
        ▼
Token IDs
        │
        ▼
Padding + Batch
        │
        ▼
Embedding
        │
        ▼
Positional Encoding