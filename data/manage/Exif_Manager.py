"""
Exif_manager handles manipulating the exif data in any desired way.
Only one should exist for each function.
"""


def sort_data(exif_tag, exif_data):
    """
    Takes an exif tag string argument and compares it to
    the key values from the exif data. If the tag exists,
    return that value. If it does not exist, throw an exception.

    :param exif_tag: string value of the desired tag
    :param exif_data: dictionary of exif data
    :return: value of the exif tag, or throws exception
    """
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


def scrub_data(exif_data):
    """
    Removes entries from the exif_data dictionary if they do not have
    associated values (this could be None or empty).

    :param exif_data: dictionary of exif values
    :return: a new dictionary without empty values
    """
    # Copy the data over (will throw if you modify while iterating)
    new_dict = exif_data.copy()

    # If the key has no meaningful data, pop it from the new dictionary
    for key in exif_data:
        if (exif_data[key] is None) or (exif_data[key] == ""):
            new_dict.pop(key)

    return new_dict
