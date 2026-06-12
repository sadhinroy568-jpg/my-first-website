from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to  tomake hack kore nilam ami sadhin onek to bolcili amake hack kore dekha akon to hack kore nilam</h1>"

if __name__ == "__main__":
    app.run(debug=True)
