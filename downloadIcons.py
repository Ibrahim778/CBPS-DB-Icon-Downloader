import csv
from os import mkdir, remove
from os.path import isdir
from shutil import rmtree
import shlex
import wget
from shutil import make_archive
import subprocess

try:
    if(isdir("icons")):
        rmtree("icons")
    mkdir("icons")
except: 
    print("Cant re-make dir (already exists?)")

try:
    remove("cbpsdb.csv")
except:
    print("Couldn't delete old file.....probably wasn't there")

try:
    wget.download("https://raw.githubusercontent.com/KuromeSan/cbps-db/master/cbpsdb.csv", "cbpsdb.csv")
except:
    print("Error download db")
    exit(0)

def downloadImage(url, id):
    print("")
    print("Downloading from " + url)
    try:
        command = "curl " + url + f" -o icons/{id}.png"
        args = shlex.split(command)
        process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
    except:
        print("Failed")
    

with open("cbpsdb.csv", encoding="utf-8") as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count > 1:
            if(row[3] != "None"):
                downloadImage(row[3], str(row[0]))

            line_count += 1
        else:
            line_count += 1
    
print("Processed " + str(line_count) + " lines.")

make_archive("icons", 'zip', "icons")