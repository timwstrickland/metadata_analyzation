"""Overview of functions and capability using the Pillow library"""
import csv
from PIL import Image
from PIL.ExifTags import TAGS

def get_data(filename):
    """load image and return exifdata"""
    image = Image.open(filename)
    exifdata = image._getexif()
    return exifdata

def extract_data(exifdata):
    """returns new dictionary with tagid's"""
    exif_data={}

    for tagid in exifdata:
        tagname = TAGS.get(tagid, tagid)
        value = exifdata.get(tagid)
        if isinstance(value, bytes):
            value = value.decode()
        exif_data.update({tagname: value})

    return exif_data

def write_files(exifdata):
    """creates csv file if it doesn't exist
    writes metadata to file
    """
    write_csv = csv.writer(open("report.csv", "w", encoding="utf8", newline=""))

    for tagid in exifdata:

        tagname = TAGS.get(tagid, tagid)
        value = exifdata.get(tagid)
        if isinstance(value, bytes):
            value = value.decode()
        write_csv.writerow([tagname, value])

def get_gps(exif_data):
    """not functional yet, need to resolve key errors"""
    north = exif_data['GPSInfo'][2]
    east = exif_data['GPSInfo'][4]
    lat = ((((north[0] * 60) + north[1]) * 60) + north[2]) / 60 / 60
    long = ((((east[0] * 60) + east[1]) * 60) + east[2]) / 60 / 60
    lat, long = float(lat), float(long)

    return lat,long
