#/usr/bin/python3
import PIL.Image as Image
import PIL.ImageColor
from end import *
import PIL
import os

def extrarctFileType(file):
    """
    Deletes the file's extension type from its name.
    Parameters:
        file: The file's name with its extension (string)
    Returns:
        newFileName: The file's name without its extension (string)
    """
    fileExtensions = (".jpg",".jpeg",".png")
    fileName = [(lettre) for lettre in file]
    newFileName = ''
    for extension in fileExtensions:
        if extension == fileExtensions[0] or extension == fileExtensions[2]:
            for letter in range(len(fileName) - 4):
                newFileName += fileName[letter]
            return(newFileName)
        else:
            for letter in range(len(fileName) - 5):
                newFileName += fileName[letter]
            return(newFileName)
            
def analyze_image(mode,image,backgroundColor="white"):
    """
    Analyzes an image and replaces the the greens with black or white depending on what background color is chosen by the user.
    Parameters:
        mode: Helps the program determine where the analyzed image should be saved
        image: The image to analyze
        backgroundColor: The color the script will put instead of the green screen ("black" or "white", default option is "white")
    Returns:
        Saves the image in the "output" folder of the project
    """
    img = Image.open(image)
    newFileName = extrarctFileType(image)
    lenght, height = img.size
    white, black = (255,255,255), (0,0,0)
    for i in range(height):
        for j in range(lenght):
            if img.getpixel((j,i)) <= (45, 205, 45):
                if backgroundColor == "white":
                    img.putpixel((j,i),white)
                else:
                     img.putpixel((j,i), black)
            else:
                if backgroundColor == "white":
                    img.putpixel((j,i), black)
                else:
                    img.putpixel((j,i), white)
    if mode == "folder":
        img.save("../output/" + newFileName + ".png")
    else:
        img.save("./output" + newFileName + ".png")


def image_analyzer(mode,file,backgroundColor="white"):
    """
    Analyzes a bunch of screenshots taken from a video game or a single one, depending on the values entered by the user.
    Parameters:
        mode: Whether the program should analyze a single image or a bunch of images in a folder ("image" or "folder")
        file: The image's name (with its extension) to analyze
        backgroundColor: The color the script will put instead of the green screen ("black" or "white", default option is "white")
    """
    assert type(file) == str or file == None, "You must enter a valid folder name (with its extension)!"
    assert backgroundColor == "white" or backgroundColor == "black", "The background color must be black or white!"
    assert mode == "file" or mode == "folder", "The mode should be either \"file\" or \"folder\""
    done = 0
    if mode == "folder":
        os.chdir('./images/')
        for file in os.listdir(os.getcwd()):
            analyze_image(mode,file,backgroundColor)
            done+=1
            print("Images analyzed: ", done)
    else:
        analyze_image(mode,image,backgroundColor)

if not "output" in os.listdir():
    os.mkdir("./output",0o755)
    print("Directory \"output\" not found, created \"output\" directory.")
mode = input("Do you want the program to analyze a bunch of images inside of a folder or do you want it to analyze a single image?\n(\"file\" or \"folder\")")
if mode == "file":
    image = input("Please type the name of the image to analyze WITH IT'S EXTENSION!\n")
color = input("What color do you want the background to be?\n(\"black\" or \"white\")\n")
if color == "":
    color = "white"
if mode == "file":
    image_analyzer(mode,image,color)
else:
    image_analyzer(mode,None,color)
end_script()
