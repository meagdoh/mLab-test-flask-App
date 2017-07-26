from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Hi there, how ya doin Chris?"

if __name__ == "__main__":
    app.run()
