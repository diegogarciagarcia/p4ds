import os, zipfile, sys

#dir_name = "C:/Users/dgarciagarci/Downloads/Garmin/rungap_exports"
dir_name = "C:/Users/dgarciagarci/Downloads"
extension = ".zip"
sys.argv = ['-p'] #included sys.argv for testing with Atom Runner

def print_zip (zip_name):
    print(zip_name)

def extract_zip(zip_name):
    zip_ref = zipfile.ZipFile(file_name) # create zipfile object
    zip_ref.extractall(dir_name) # extract file to dir
    zip_ref.close() # close file
    if "-r" in sys.argv:
        os.remove(file_name) # delete zipped file


os.chdir(dir_name) # change directory from working dir to dir with files

for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        file_name = os.path.abspath(item) # get full path of files
        if "-e" in sys.argv:
            extract_zip(file_name)
        if "-p" in sys.argv:
            print_zip(file_name)
