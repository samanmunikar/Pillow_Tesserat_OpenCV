import PIL
from PIL import Image
from PIL import ImageEnhance

# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')

# build a list of 9 images which have different brightnesses
enhancer=ImageEnhance.Brightness(image)
images=[]
for i in range(1, 10):
    images.append(enhancer.enhance(i/10))

# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)

import PIL
from PIL import Image
from IPython.display import display
file="readonly/msi_recruitment.gif"
original_image=Image.open(file)
original_image=original_image.convert("RGB")
display(original_image)

images=[]
image=original_image.convert("RGB")
print(image.getpixel((0,0)))

colorIntensity_dict = {'red':[0.1, 0.5, 0.9],'green':[0.1, 0.5, 0.9],'blue':[0.1, 0.5, 0.9]}

for color in colorIntensity_dict:
    image=original_image.convert("RGB")
    for intensity in colorIntensity_dict[color]:
        image=original_image.convert("RGB")
        for x in range(image.width):
            for y in range(image.height):
                r,g,b = image.getpixel((x,y))
                #print(color)
                #print(inten)
                if color == "red":
                    r = r * intensity
                    new_color = (int(r), g, b)
                    #print(new_color)
                elif color == "green":
                    g = g * intensity
                    new_color = (r, int(g), b)
                    #print(new_color)
                elif color == "blue":
                    b = b * intensity
                    new_color = (r, g, int(b))
                    #print(new_color)
                
                image.putpixel((x,y), new_color)
        #print("NEXT COLOR")
        images.append(image)

display(image)

first_image=images[0]
x,y = 0,0
contact_sheet=PIL.Image.new(first_image.mode, (3*first_image.width,3*first_image.height))
current_location=0
for img in images:
    contact_sheet.paste(img, (x,y))
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width
contact_sheet=contact_sheet.resize((int(contact_sheet.width/2), int(contact_sheet.height/2)))
display(contact_sheet)