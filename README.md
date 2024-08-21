# Text Similarity App by Python

A simple app to serve text similarity check using Semantic Sentence Transformer build with Python and FastApi.
Simple example to use it is question and answering system. To compare student's answer text to answer key provided by a teacher

## Model
We use SentenceTransformers from https://sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html using this available models https://sbert.net/docs/sentence_transformer/pretrained_models.html

Currently, we use `paraphrase-multilingual-MiniLM-L12-v2` that support multilingual include Indonesia

## How to use
1. Clone this image
2. Run `python model.py` This command to save the downloaded model to the directory to speed up running application
3. Access from url

URLs
* GET `/` -> to check this endpoint is running
* GET `/check/single` -> to check 1 sentense to 1 comparation
* GET `/check/multi` -> to check 1 sentense to multiple comparation

## Example use

Question: Apa yang dimaksud dengan Teknologi blockchain?

Answer key: Blockchain adalah teknologi yang berfungsi sebagai sistem penyimpanan atau bank data digital yang terhubung melalui kriptografi. Ini adalah database terdistribusi yang menyimpan catatan transaksi dengan aman dan transparan di seluruh jaringan komputer. Blockchain pertama kali dikenal melalui Bitcoin dan cryptocurrency lainnya, tetapi memiliki potensi luas untuk penerapan di berbagai sektor


Answer 1: Blockchain merupakan bitkoin

Answer 2: Blockchain adalah sektor keuangan

Answer 3: Teknologi digital terbaru adalah blockchain

## Data
### Single check:
To check single answer to answer key

```json
{
  "correct_answer": "Blockchain adalah teknologi yang berfungsi ...",
  "response": "Blockchain merupakan bitkoin"
}
```

Reply
```json
{
  "correct_answer": "Blockchain adalah teknologi yang berfungsi ...",
  "response": "Blockchain merupakan bitkoin",
  "score": 70.55555
}
```

The score range 0.0 to 1.0



### Multi Check:
To check multi answer at once per answer key