# Sort through the data for a specific tag - String and dictionary params
def sort_data(exif_tag, exif_data):
    # Get the key set from the dictionary
    tags = exif_data.keys()
    found = False

    # Search for the tag
    for tag in tags:
        if exif_tag == tag:
            found = True
            break

    # If the tag (key) was not found, throw exception
    if not found:
        raise Exception("Exif tag missing from current file.")

    # Return the value if the tag was found
    return exif_data[exif_tag]


# Scrub the dictionary of key/value pairs that do not have meaningful data - dictionary param
def scrub_data(exif_data):
    # Copy the data over (will throw if you modify while iterating)
    new_dict = exif_data.copy()

    # If the key has no meaningful data, pop it from the new dictionary
    for key in exif_data:
        if (exif_data[key] is None) or (exif_data[key] == ""):
            new_dict.pop(key)

    return new_dict


exifDict = {"yes": "data", "ImageWidth": None, "test1": "", "test2": None, "ImageHeight": None, "Make": "Samsung"}

print(sort_data("ImageWidth", exifDict))
print(scrub_data(exifDict))
print(sort_data("ImageHeight", exifDict))

# This should throw with a message of a missing tag
print(sort_data("ImageHeight", scrub_data(exifDict)))
