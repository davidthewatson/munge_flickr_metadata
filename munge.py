import flickrapi # see http://stuvel.eu/flickrapi/documentation/
import yaml
import sys

def format_tags(tags):
    output = ''
    for tag in tags:
        txtstr = ''
        #print tag.attrib
        tagstr =  tag.attrib['label']
        for z in tag: 
            if z.tag in ('clean'):
                    txtstr = z.text
            elif z.tag in ('raw') and txtstr == '':
                    txtstr = z.text
        output += '%s: %s\n' % (tagstr, txtstr)
    return output

api = yaml.load(open('api.yaml'))
flickr = flickrapi.FlickrAPI(api['key'], api['secret'])
(token, frob) = flickr.get_token_part_one(perms='write')
if not token: raw_input("Press ENTER after you authorize this program")
flickr.get_token_part_two((token, frob))
set_title = flickr.photosets_getInfo(photoset_id=sys.argv[1])[0].getchildren()[0].text
this_set = flickr.walk_set(sys.argv[1])
print dir(this_set)
tag_set = ('Aperture', 'FocalLength', 'Focal Length', 'ISO', 'ISOSpeed', 'ISO Speed', 'Make', 'Model', 'Exposure', 'ExposureTime', 'Exposure Time') 
for photo in this_set:
        photo_id = photo.get('id')
        try:
                exif = flickr.photos_getExif(photo_id=photo_id)
        except:
                print 'exception on get exif'
                continue
        msg = ''
        for x in exif:
                tag_set = ('Aperture', 'FocalLength', 'Focal Length', 'ISO', 'ISOSpeed', 'ISO Speed', 'Make', 'Model', 'Exposure', 'ExposureTime', 'Exposure Time')
                msg += format_tags(y for y in x if y.attrib['tag'] in tag_set or y.attrib['label'] in tag_set)
                
        flickr.photos_setMeta(photo_id=photo_id, title=set_title, description=msg)
        print msg
                                                                                                                                                                                                 
                                                                                                                                        
