import csv
import shutil
import os

#TODO: Organize the training dataset into different catagories, then output it to different folders

#change the directory paths for your own code
parent_dir = "C:/Users/chris/Desktop/"
#different catagories, foldernames used. All files go into the "images" directory
folders = ["images/", "Melanoma/", "Melanocytic Nevus/", "Neither/"]
destinations = []
for i in range(len(folders)):
    if i == 0:
        path = os.path.join(parent_dir, folders[i])
    else:
        path = os.path.join(parent_dir + folders[0], folders[i])
        destinations.append(path)
    os.mkdir(path)
    print("Directory '% s' created" % folders[i])

location = "C:/Users/chris/Downloads/ISIC_2019_Training_GroundTruth.csv"
none = 0

with open(location, 'r') as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        image = row["image"]
        MELval = row["MEL"]
        NVval = row["NV"]
        originalIMG = "C:/Users/chris/Downloads/ISIC_2019_Training_Input/ISIC_2019_Training_Input/" + image + ".jpg"
        if(int(MELval) == 1):
            destIMG = destinations[0] + image + ".jpg"
        elif(int(NVval) == 1):
            destIMG = destinations[1] + image + ".jpg"
        else:
            destIMG = destinations[2] + image + ".jpg"
            print(image + " was neither")
            none += 1
        shutil.copy(originalIMG, destIMG)

print("Total number of nonclassified: " + str(none))

print("ALL IMAGES COPIED SUCCESSFULLY")