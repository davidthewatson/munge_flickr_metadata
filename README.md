#munge.py 

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

##Warning

If you have a large number of sets or photos on flickr, this script may run for hours. It will emit the set id it is processing so you can go to flickr and observe the changes as they happen.

##See the flickr API doc

    http://librdf.org/flickcurl/api/flickcurl-auth-register.html
