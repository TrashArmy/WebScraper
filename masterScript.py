import os
import json

def createPath(parentPath, folderName):
    if not os.path.isdir('./' + parentPath + folderName):
        # os.system
        os.system("mkdir " + parentPath + folderName)


# Set up json
datastore = json.load(open('schema.json'))

for cat, subcats in datastore.iteritems():
    for subcat, search_query_list in subcats.iteritems():
        # Subcategory name
        directory = subcat
        createPath('dataset_images/', subcat)
        offset = 0
        for search_q in search_query_list:
            print 'run python search for ' + search_q + ' for folder ' + subcat
            os.system("python scrapeImages.py -d ./dataset_images/" + subcat + " -s " + search_q + " -n 100 -p " + subcat + " -o " + str(offset * 100))
            offset += 1

# createPath('dataset_images/', "test_images")
# os.system("python scrapeImages.py -d ./test_images -s aluminum_foil -n 10 -p Foil")
