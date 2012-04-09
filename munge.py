import flickrapi # easy_install flickrapi
import yaml # easy_install pyyaml
import sys

def format_tags(tags, quotes=False):
    output = ''
    for tag in tags:
        txtstr = ''
        tagstr =  tag.attrib['label']
        for z in tag: 
            if z.tag in ('clean'):
                    txtstr = z.text
            elif z.tag in ('raw') and txtstr == '':
                    txtstr = z.text
        if quotes:
            output += '"%s: %s" ' % (tagstr, txtstr)
        else:
            output += '%s: %s\n' % (tagstr, txtstr)
    return output

api = yaml.load(open('api.yaml'))
flickr = flickrapi.FlickrAPI(api['key'], api['secret'])
(token, frob) = flickr.get_token_part_one(perms='write')
if not token: raw_input("Press ENTER after you authorize this program")
flickr.get_token_part_two((token, frob))
set_list = flickr.photosets_getList()
for item in set_list[0]:
    set_title = item[0].text
    this_set = flickr.walk_set(item.attrib['id'])
    print item.attrib['id']
    tag_set = ('Aperture', 'FocalLength', 'Focal Length', 'ISO', 'ISOSpeed', 'ISO Speed', 'Make', 'Model', 'Exposure', 'ExposureTime', 'Exposure Time') 
    for photo in this_set:
        photo_id = photo.get('id')
        try:
            exif = flickr.photos_getExif(photo_id=photo_id)
        except:
            print 'exception on get exif'
            continue
        msg = ''
        tags = set_title
        for x in exif:
            msg += 'Photograph by <a href="http://davidwatson.org/">David Watson</a>\r\nLicensed under <a href="http://creativecommons.org/licenses/by-nc-sa/3.0/">Creative Commons, Attribution, Non-Commercial, Share-Alike</a>\r\nYou may use this image on the internet with proper attribution and a link to my site.\r\n' + format_tags(y for y in x if y.attrib['tag'] in tag_set or y.attrib['label'] in tag_set)
            tags += ' ' + format_tags((y for y in x if y.attrib['tag'] in tag_set or y.attrib['label'] in tag_set), True)
        flickr.photos_setMeta(photo_id=photo_id, title=set_title, description=msg)
        flickr.photos_addTags(photo_id=photo_id, tags=tags)