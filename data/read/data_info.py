# Overview of functions and capability using the Pillow library
import csv
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import PIL.ExifTags

# load image and return exifdata
def get_data(filename):
    image = Image.open(filename)
    exif_data = image.getexif()
    return exif_data

# returns new dictionary with tagid's
def extract_data(exifdata):

    exif_data={}

    for tagid in exifdata:
        tagname = TAGS.get(tagid, tagid)
        value = exifdata.get(tagid)
        if isinstance(value, bytes):
            value = value.decode()
        exif_data.update({tagname: value})
        
    return exif_data

def write_files(exifdata):
    
    w = csv.writer(open("report.csv", "w", newline=""))

    for tagid in exifdata:

        tagname = TAGS.get(tagid, tagid)
        value = exifdata.get(tagid)
        if isinstance(value, bytes):
            value = value.decode()
        w.writerow([tagname, value])

# not functional yet, need to resolve key errors
def get_gps(exif_data):
    
    
    north = exif_data['GPSInfo'][2]
    east = exif_data['GPSInfo'][4]
    lat = ((((north[0] * 60) + north[1]) * 60) + north[2]) / 60 / 60
    long = ((((east[0] * 60) + east[1]) * 60) + east[2]) / 60 / 60
    lat, long = float(lat), float(long)

    return lat,long



