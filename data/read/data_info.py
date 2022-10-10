import csv
from PIL import Image
from PIL.ExifTags import TAGS

'''
Data_info handles basic manipulation of the uploaded files. It uses the Pillow library
to interact with the file.
'''


def get_data(file):
    """
    get_data handles getting the unparsed exif data from the image, if it exists
    :param file: the uploaded file
    :return: raw exif data
    """
    image = Image.open(file)
    exif_data = image._getexif()
    return exif_data


def extract_data(exif):
    """
    extract_data extracts readable tag id's for each line in the exif data
    :param exif: the exif data to be parsed and translated
    :return: readable exif data
    """
    exif_data = {}

    for tag_id in exif:
        tag_name = TAGS.get(tag_id, tag_id)
        value = exif.get(tag_id)
        if isinstance(value, bytes):
            value = value.decode('latin1')
        exif_data.update({tag_name: value})

    return exif_data


def write_files(exif_data):
    """
    write_files creates the csv file if it doesn't exist, and writes
    the appropriate lines to the file after creation
    :param exif_data: data to be written to file
    :return: no formal return (writes file to program directory)
    """
    write_csv = csv.writer(open("report.csv", "w", encoding="latin1", errors='ignore', newline=""),
                           delimiter='|', quoting=csv.QUOTE_NONE, quotechar='', escapechar='\\')

    for tag_id in exif_data:

        tag_name = TAGS.get(tag_id, tag_id)
        value = exif_data.get(tag_id)
        if isinstance(value, bytes):
            value = value.decode()
        write_csv.writerow([tag_name, value])
