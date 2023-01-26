from PIL import Image
import piexif

codec = 'ISO-8859-1'

def exif_to_tag(exif_dict):
    exif_tag_dict = {}
    thumbnail = exif_dict.pop('thumbnail')
    exif_tag_dict['thumbnail'] = thumbnail.decode(codec)

    for ifd in exif_dict:
        exif_tag_dict[ifd] = {}
        for tag in exif_dict[ifd]:
            try:
                element = exif_dict[ifd][tag].decode(codec)

            except AttributeError:
                element = exif_dict[ifd][tag]

            exif_tag_dict[ifd][piexif.TAGS[ifd][tag]["name"]] = element

    return exif_tag_dict

def img_get_location(path_to_image):
    rslt = []
    image = Image.open(path_to_image)
    exif_dict = piexif.load(image.info.get('exif'))
    exif_dict = exif_to_tag(exif_dict)
    rslt.append(float(str(exif_dict['GPS'].get('GPSLatitude')[0][0])+"."+str(exif_dict['GPS'].get('GPSLatitude')[1][0])))
    rslt.append(float(str(exif_dict['GPS'].get('GPSLongitude')[0][0])+"."+str(exif_dict['GPS'].get('GPSLongitude')[1][0])))
    return rslt