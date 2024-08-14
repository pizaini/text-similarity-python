
from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from starlette.responses import JSONResponse


class MultiAnswer(BaseModel):
    correct_answer: str
    responses: list = []


class SingleAnswer(BaseModel):
    correct_answer: str
    response: str


app = FastAPI()


@app.get("/")
def root():
    jsonData = {
        "message": 'OK'
    }
    return JSONResponse(content=jsonData)


@app.get("/check/single")
def root(answer: SingleAnswer):
    return checkSingleResponse(answer)


@app.get("/check/multi")
def root(answers: MultiAnswer):
    return checkMultiResponse(answers)


def checkSingleResponse(answer: SingleAnswer):
    correct_answer = answer.correct_answer
    response = answer.response
    similarity_scores = semantic_textual_similarity([correct_answer], [response])
    similarity_score = similarity_scores.tolist()[0][0]

    jsonData = {
        "corrent_answer": correct_answer,
        "response": response,
        "score": similarity_score,
    }
    return JSONResponse(content=jsonData)


def checkMultiResponse(answer: MultiAnswer):
    correct_answer = answer.correct_answer
    responsesOnly = pluck(answer.responses, 'response')

    similarity_scores = semantic_textual_similarity([correct_answer], responsesOnly)
    similarity_scoreAsArray = similarity_scores.tolist()[0]

    responsesWithScore = []
    for idx, response in enumerate(answer.responses):
        responsesWithScore.append({
            "id": response.get('id'),
            "response": response.get('response'),
            "score": similarity_scoreAsArray[idx]
        })

    jsonData = {
        "correct_answer": correct_answer,
        "responses": responsesWithScore,
    }
    return JSONResponse(content=jsonData)


def semantic_textual_similarity(kunci_jawaban: list, sentences: list):
    model = SentenceTransformer('saved_model_data')
    encodeKunciJawaban = model.encode(kunci_jawaban)
    encodeJawaban = model.encode(sentences)
    return model.similarity(encodeKunciJawaban, encodeJawaban)


def pluck(lst, key):
    return [x.get(key) for x in lst]
