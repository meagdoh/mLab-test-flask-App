from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        region = request.form['region']

    return render_template('region.html', region=region)

    return render_template('index.html')

if __name__ == "__main__":
    app.run()
