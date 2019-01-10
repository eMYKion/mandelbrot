from PIL import Image
import colorsys

width = 10000
height = 10000

#this will save some calculation later
#based on a 255x255 image
cutoffRight = int(50*width/255)
cutoffLeft = int(0*width/255)
cutoffTop = int(50*height/255)
cutoffBot = int(50*height/255)

img = Image.new("HSV",(width, height),"black")
pixels = img.load()

def mandlebrotIterationsUntilLarge(c):
    count = 0
    z = c
    while(True):
        z = z**2 + c
        if((z*z.conjugate()).real > 2):
            return count
        elif(count == 180):
            return count
        count +=1


for col in range(width):
    for row in range(height):
        if((col < cutoffLeft) | (col > width - cutoffRight)):
            pixels[col,row] = (0,0,255)
        elif((row < cutoffBot) | (row > height - cutoffTop)):
            pixels[col,row] = (0,0,255)
        else:
            pixels[col,row] = (mandlebrotIterationsUntilLarge(4*(col-width/2)/width -4*(row-height/2)/height * 1j),200,200)



img = img.convert('RGB')
img.save("img.png")
img.show()
