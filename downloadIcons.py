import csv
from os import mkdir
import wget
import glob
from shutil import move, make_archive

try:
    mkdir("icons")
except: 
    print("Cant make dir (already exists?)")

try:
    wget.download("https://raw.githubusercontent.com/KuromeSan/cbps-db/master/cbpsdb.csv", "cbpsdb.csv")
except:
    print("Error download db")
    exit(0)

def downloadImage(url, id):
    print("")
    print("Downloading from " + url)
    try:
        wget.download(url)
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

            line_count += 1
        else:
            line_count += 1
    
print("Processed " + str(line_count) + " lines.")

make_archive("icons.zip", 'zip', "icons")