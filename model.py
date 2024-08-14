from sentence_transformers import SentenceTransformer

print('Loading model')
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

model.save('saved_model_data')
print('Saved model')