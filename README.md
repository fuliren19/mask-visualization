# mask-visualization
When tagging data with the markup tool(E.g: labelme), it is difficult to check if the tag's category is correct, which will affect the training effect of deep learning. This script can visualization label and makes it easy to view the class of the tag.
# Instructions
file_path = '/home/data/XXX'

save_path = '/home/Visualization/XXX'

image_path = '/home/data/XXX'

Files in json format can be placed in the same folder as files in jpg format, but the names must be the same.（E.g: 2019.json and 2019.jpg)

Will generate different class of folders under the save_path, and put the visual mask image in the folder
