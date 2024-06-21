from rembg import remove
from PIL import Image

inputPath = input("Dosyanın Yolunu Giriniz: ")
outputPath = input("Varsayılan yere mi kaydedilsin Y/N?")

if outputPath == "y" or outputPath == "Y":
    fileName = input("Çıktı dosyasının adını giriniz: ")
    outputPath = f"/Users/kemalozyon/Downloads/BackgroundImageDeleted/{fileName}.png"

elif outputPath == "n" or outputPath == "N":
    myPath = input("Kaydedilecek yerin adresini giriniz")
    fileName = input("Çıktı dosyasının adını giriniz: ")
    outputPath = input(myPath+f"{fileName}.png")

input1 = Image.open(inputPath)
output1 = remove(input1)

output1.save(outputPath)