from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Data rekomendasi berdasarkan kategori & mood
rekomendasi = {
    "normies": {
        "sedih": {"lagu": "Someone Like You - Adele", "film": "The Fault in Our Stars"},
        "senang": {"lagu": "Happy - Pharrell Williams", "film": "The Intern"},
        "marah": {"lagu": "Numb - Linkin Park", "film": "John Wick"},
        "tenang": {"lagu": "Perfect - Ed Sheeran", "film": "The Secret Life of Walter Mitty"}
    },
    "kpopers": {
        "sedih": {"lagu": "Blue & Grey - BTS", "film": "Twenty"},
        "senang": {"lagu": "Dynamite - BTS", "film": "Extreme Job"},
        "marah": {"lagu": "Kill This Love - BLACKPINK", "film": "The Villainess"},
        "tenang": {"lagu": "Love Poem - IU", "film": "Little Forest"}
    },
    "wibu": {
        "sedih": {"lagu": "Orange - 7!!", "film": "AnoHana"},
        "senang": {"lagu": "Gotoubun no Katachi - Nakano-ke no Itsutsugo", "film": "Komi-san wa, Komyushou desu"},
        "marah": {"lagu": "Uragiri no Yuuyake - Theatre Brook", "film": "Attack on Titan: Chronicle"},
        "tenang": {"lagu": "Kataware Doki - RADWIMPS", "film": "Clannad"}
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rekomendasi', methods=['POST'])
def get_rekomendasi():
    mood = request.form['mood'].lower()
    kategori = request.form['kategori']

    # Jika user memilih random
    if kategori == "random":
        kategori = random.choice(list(rekomendasi.keys()))

    if kategori in rekomendasi and mood in rekomendasi[kategori]:
        hasil = rekomendasi[kategori][mood]
    else:
        hasil = {"lagu": "Belum ada rekomendasi untuk mood ini.", "film": "-"}

    return render_template('index.html', mood=mood, kategori=kategori, lagu=hasil["lagu"], film=hasil["film"])

if __name__ == '__main__':
    app.run(debug=True)
