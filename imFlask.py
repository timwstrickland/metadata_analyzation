from flask import Flask, redirect, url_for, render_template, request, send_file
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
    file = request.files['file']
    try:
        check_file(file.filename)
        file_data = data_info.get_data(file)
        meta = data_info.extract_data(file_data)
        new_file = data_info.write_files(meta)
        return render_template('results.html', meta=meta)
    except NameError:
        return render_template('index.html')
    except TypeError:
        return render_template('index.html')

@app.route('/files')
def files():
    return send_file('report.csv')

def check_file(filename):
    approved_types = ['jpg', 'jpeg']
    bad_characters = "!@#$%^&*/<>"

    for value in range(0, len(filename)):
        if filename[value] in bad_characters:
            raise NameError()

    if '.' in filename and filename.rsplit('.', 1)[1].lower() not in approved_types:
        raise TypeError()


if __name__ == '__main__':
    app.run(debug=True)
    app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024
