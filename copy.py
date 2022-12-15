import os
import shutil

source_folder = r"C:\Users\Alexa\OneDrive\Área de Trabalho\teste\\"
destination_folder = r"C:\Users\Alexa\OneDrive\Área de Trabalho\destino\\"

# fetch all files
for file_name in os.listdir(source_folder):
    # construct full file path
    source = source_folder + file_name
    destination = destination_folder + file_name
    # copy only files
    if os.path.isfile(source):
        shutil.copy(source, destination)
        print('copied', file_name)