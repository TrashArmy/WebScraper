# Once a folder is created, you can run this script to clean up all the files and make it ok to start labelling with

# converts gif png svg files to .jpeg
ls -1 *.gif *.png *.svg | parallel --eta convert '{}' '{.}.jpg'

# Rename all .jpeg to .jpg
find . -type f -name '*.jpeg' -print0 | xargs -0 rename 's/\.jpeg/\.jpg/'

# Delete all non .jpg files
find . -type f ! -name '*.jpg' -delete