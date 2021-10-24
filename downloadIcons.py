import csv
from os import mkdir, remove
import shlex
import wget
import glob
from shutil import move, make_archive
import subprocess
from time import sleep

try:
    mkdir("icons")
except: 
    print("Cant make dir (already exists?)")

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
        command = "curl " + url + " -O icon.png"
        args = shlex.split(command)
        process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        move(glob.glob("*.png")[0], "icons/" + id + ".png")
    except:
        print("Failed")
    

with open("cbpsdb.csv", encoding="utf-8") as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count > 1:
            if(row[3] != "None"):
                downloadImage(row[3], str(row[0]))
                sleep(1)

            line_count += 1
        else:
            line_count += 1
    
print("Processed " + str(line_count) + " lines.")

make_archive("icons", 'zip', "icons")