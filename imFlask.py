from flask import Flask, redirect, url_for, render_template, request
from data.read import data_info

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/results')
def results():
    return render_template('results.html')
    # eventually will be: return render_template('results.html', results=variable_for_results)


@app.route('/', methods=['POST'])
def image_up():
    if request.method == "POST":
        file = request.files['file']
        file_data = data_info.extract_data(file)
        return file.filename


if __name__ == '__main__':
    app.run(debug=True)
