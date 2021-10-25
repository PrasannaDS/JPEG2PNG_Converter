import sys
import os
from PIL import Image

parent_dir = sys.argv[1]

directory = sys.argv[2]

path = os.path.join(parent_dir, directory)

if not os.path.exists(directory):
    os.makedirs(directory)

for filename in os.listdir(parent_dir):
    img = Image.open(f'{parent_dir}{filename}')
    clean_name = os.path.splitext(filename)
    img.save(f'{directory}{clean_name[0]}.png','png')
    print('All Done!clear')
    
