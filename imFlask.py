from flask import Flask, render_template, request, send_file, flash
from data.read import data_info

'''
ImageMetrics allows a user to upload a file and read the embedded exif data within. 
This program handles running the server for the user to interact with.

Run this file, and use your localhost address that is annotated in debug window to
interact with it. It currently runs in developer mode (not a production server)
as we do not have the resources to have a formal website.
'''

app = Flask(__name__)
app.secret_key = 'thisisasecretkey'
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024


@app.route('/')
def home():
    """
    Route the user to the home page.

    :return: index page
    """
    return render_template('index.html')


@app.route('/about')
def about():
    """
    Route the user to the about page.

    :return: about page
    """
    return render_template('about.html')


@app.route('/results')
def results():
    """
    Route the user to the results page.

    :return: results page
    """
    return render_template('results.html')


@app.route('/', methods=['POST'])
def image_up():
    """
    Handles uploading the file, which is first checked for validity.
    Also handles exceptions that result from naming errors, file type errors,
    exif data errors, and file writing errors. Each will flash a message on
    screen for the user and return them to the home page.

    This has the issue right now of immediately writing the file once uploaded.
    If multiple users were to use the site, it would result in the file being
    overwritten and possibly returning the wrong file to the user if they export.

    :return: Results page if successful, home page if an exception occurs.
    """
    file = request.files['file']
    try:
        check_file(file.filename)
        file_data = data_info.get_data(file)
        meta = data_info.extract_data(file_data)
        data_info.write_files(meta)
        return render_template('results.html', meta=meta)
    except NameError:
        flash("Invalid file name, please try again.")
        return render_template('index.html')
    except TypeError:
        flash("Presented file has no exif data.")
        return render_template('index.html')
    except NotImplementedError:
        flash("Incorrect file type. ImageMetrics can only use jpg or jpeg pictures.")
        return render_template('index.html')
    except FileNotFoundError:
        flash("Sorry, we couldn't export the CSV.")
        return render_template('index.html')


@app.route('/files')
def files():
    """
    Returns the exported CSV to the user.

    :return: CSV report of exif data.
    """
    return send_file('report.csv')


def check_file(filename):
    """
    Handles checking the file for validity.
    This function will check if the file is approved (jpg, jpeg),
    and ensures the file does not have any dangerous characters (never trust user input).

    :param filename: the name of the uploaded file, with file extension.
    :return: Exception if invalid file is uploaded, nothing if a valid file.
    """
    approved_types = ['jpg', 'jpeg']
    bad_characters = "!@#$%^&*/<>"

    for value in range(0, len(filename)):
        if filename[value] in bad_characters:
            raise NameError()

    if '.' in filename and filename.rsplit('.', 1)[1].lower() not in approved_types:
        raise NotImplementedError()


if __name__ == '__main__':
    app.run(debug=True)
