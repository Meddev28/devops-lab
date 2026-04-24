from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
    return "version 5 - deployement automatic test3 test5"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)