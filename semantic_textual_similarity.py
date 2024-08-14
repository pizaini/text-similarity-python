from sentence_transformers import SentenceTransformer

model = SentenceTransformer('saved_model_data')

# Sample sentence
sentences = ["Nabi sedang khutbah hari jum'at dan jamaah mendatangi pedagang",
			 "Para sahabat sedang mendengarkan Nabi berkhutbah. Saat pedangan tiba sahabar lalu bertransaksi jual beli pada pedagang",
			 "Para sahabat meninggalkan solat jum'at karena membeli barang dagangan",
			 "Para sahabat bertransaksi dengan pedagang di pasar",
			 "Transaksi perdagangan terjadi di hari jum'at sebelum ibadah",
			 "Kaum muslim yang sedang solat jum'at berbondong-bondong menuju pedagang dan bertransaksi. Namun di saat yang sama para sahabat meninggalkan solat tersebut",
			 "Muhammad berkhutbah hari jum'at jamaah mendatangi pedagang di hari sabtu"
			 ]


kunci_jawaban = [
	"Nabi Muhammad SAW sedang berkhutbah pada hari Jumat. Saat itu, ada kafilah dagang yang datang ke Madinah dengan membawa barang-barang dagangan. Para sahabat yang sedang mendengarkan khutbah beranjak meninggalkan Nabi dan bergegas untuk melihat dan bertransaksi dengan kafilah tersebut. Hanya sebagian kecil sahabat yang tetap mendengarkan khutbah. Kejadian ini menjadi sebab turunnya ayat yang mengingatkan pentingnya mendengarkan khutbah Jumat dan meninggalkan aktivitas jual beli selama waktu shalat Jumat"
]

encodeKunciJawaban = model.encode(kunci_jawaban)
encodeJawaban = model.encode(sentences)

similarities = model.similarity(encodeKunciJawaban, encodeJawaban)

# Output the pairs with their score
for idx_i, sentence1 in enumerate(kunci_jawaban):
    print(sentence1)
    for idx_j, sentence2 in enumerate(sentences):
        print(f" - {sentence2: <30}: {similarities[idx_i][idx_j]:.4f}")
