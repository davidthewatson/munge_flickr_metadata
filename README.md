#munge.py 

##uses the Flickr API web service to munge the metadata for photos

* iterate over every set for the given user
* iterate over every photo in the set
* set the title to the title of the parent photo
* set the description to a concatenation of basic EXIF data including: Camera make, model, aperture, shutter speed, and ISO
* set tags to the tokens used in the title and the description

##Install

    easy_install flickrapi
    easy_install pyyaml

Create a text file named api.yaml in the same directory as the script which contains two lines
    
    key : YOUR-KEY-GOES-HERE
    secret : YOUR-SECRET-GOES-HERE

##Run

    python munge.py

##See the flickr API documentation for more information:

    http://librdf.org/flickcurl/api/flickcurl-auth-register.html
