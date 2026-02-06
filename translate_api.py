from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("translate.html")

@app.route("/api/v1/<word>")
def api(word):
    definition = str(word)
    return {"definition":definition.upper(),
            "word":definition}

if __name__ == '__main__':
    app.run(debug=True, port=5002)

