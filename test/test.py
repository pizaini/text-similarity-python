#!pip install -U sentence-transformers

import time
from scipy.spatial import distance
from sentence_transformers import SentenceTransformer

ts = time.time()
print(f'Loading model {ts}')
# model = SentenceTransformer('saved_model_data')
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# Sample sentence
sentences = ["Nabi sedang khutbah hari jum'at dan jamaah mendatangi pedagang",
			 "Para sahabat yang sedang mendengarkan khutbah menghampiri pedagang dan membeli barang dagangannya",
			 "Para sahabat meninggalkan solat jum'at karena membeli barang dagangan",
			 "Para sahabat bertransaksi dengan pedagang di pasar",
			 "Transaksi perdagangan terjadi di hari jum'at sebelum ibadah",
			 "Kaum muslim yang sedang solat jum'at berbondong-bondong menuju pedagang dan bertransaksi. Namun di saat yang sama para sahabat meninggalkan solat tersebut",
			 "Muhammad berkhutbah hari jum'at. jamaah mendatangi pedagang esok hari"
			 ]


kunci_jawaban = "Surah Al-Jumu'ah ayat 11 diturunkan karena terjadi suatu peristiwa ketika Nabi Muhammad SAW sedang berkhutbah pada hari Jumat. Saat itu, ada kafilah dagang yang datang ke Madinah dengan membawa barang-barang dagangan. Para sahabat yang sedang mendengarkan khutbah beranjak meninggalkan Nabi dan bergegas untuk melihat dan bertransaksi dengan kafilah tersebut. Hanya sebagian kecil sahabat yang tetap mendengarkan khutbah. Kejadian ini menjadi sebab turunnya ayat yang mengingatkan pentingnya mendengarkan khutbah Jumat dan meninggalkan aktivitas jual beli selama waktu shalat Jumat"
# print('Kunci jawaban: ', kunci_jawaban)

ts = time.time()
test_vec = model.encode([kunci_jawaban])[0]
print(f'Processing... {ts}')

for i, sent in enumerate(sentences):
	ts = time.time()
	similarity_score = 1 - distance.cosine(test_vec, model.encode([sent])[0])
	similarity_percent = similarity_score * 100
	print(f'\nJabawan {i+1}: {sent}\nSimilarity Score = {similarity_score} ({similarity_percent} %)')
