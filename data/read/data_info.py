# Overview of functions and capability using the Pillow library

import csv
from tkinter import image_names
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import PIL.ExifTags

# load image in local folder
test_img = 'gps_ex.jpg'
image = Image.open(test_img)


# Extract exif metadata
exifdata = image._getexif()


def extract_data():
    # Loop through present tags
    for tagid in exifdata:

        tagname = TAGS.get(tagid, tagid)
        value = exifdata.get(tagid)
        if isinstance(value, bytes):
            value = value.decode()

        print(f"{tagname:40}: {value}")

#extract_data()

def write_files():
    
    w = csv.writer(open("image_metas.csv", "w", newline=""))

    for tagid in exifdata:

        tagname = TAGS.get(tagid, tagid)
        value = exifdata.get(tagid)
        if isinstance(value, bytes):
            value = value.decode()
        w.writerow([tagname, value])

#write_files()

def get_gps():
    
    exif = {
        PIL.ExifTags.TAGS[k]: v
        for k, v in image._getexif().items()
        if k in PIL.ExifTags.TAGS
    }

    print(exif['GPSInfo'])
    north = exif['GPSInfo'][2]
    east = exif['GPSInfo'][4]

    print(north)
    print(east)

    lat = ((((north[0] * 60) + north[1]) * 60) + north[2]) / 60 / 60
    long = ((((east[0] * 60) + east[1]) * 60) + east[2]) / 60 / 60
    lat, long = float(lat), float(long)

    print(lat)
    print(long)

#get_gps()



