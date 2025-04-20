from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    er = None
    if request.method == "POST":
        try:
            likes = int(request.form["like"])
            comments = int(request.form["Comment"])
            shares = int(request.form["Share"])
            followers = int(request.form["Follower"])
            
            if followers == 0:
                return "Jumlah follower tidak boleh 0!"
            
            er = ((likes + comments + shares) / followers) * 100
        
        except ValueError:
            return "input tidak valid! Masukkan angka yang benar."
    
    return render_template("index.html", er=round(er, 2) if er is not None else None)

if __name__ == "__main__":
    app.run(debug=True)
    