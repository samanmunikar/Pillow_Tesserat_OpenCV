from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np

from zipfile import ZipFile
from io import BytesIO
from PIL import ImageDraw

face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

images_zip = ZipFile('readonly/images.zip')

face_search = str(input('Enter a face to search: '))

print('\n')

for file in images_zip.infolist():
    data = images_zip.read(file)
    dataEnc = BytesIO(data)
    image_pil = Image.open(dataEnc)
    
    text = pytesseract.image_to_string(image_pil)
    
    if (face_search in text): 
        print('The string ',face_search,' was found in ',file.filename)
        
        cv_img = cv.imdecode(np.frombuffer(data, np.uint8), 1)
        gray = cv.cvtColor(cv_img, cv.COLOR_BGR2GRAY) 
        faces = face_cascade.detectMultiScale(gray,3) 
        
        face_images = []
        for x,y,w,h in faces:
            face_images.append(image_pil.crop((x,y,x+w,y+h)))
        
        if(len(face_images)>0): 
            print('Also, ',len(face_images),'faces were found')
            
            first_image=face_images[0]
            contact_sheet=Image.new(first_image.mode, (216*5,216*2))
            x,y=0,0
            
            for img in face_images:
                contact_sheet.paste(img,(x, y))
                if(x+216 == contact_sheet.width):
                    x,y=0,y+216
                else:
                    x=x+216

            contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
            display(contact_sheet)
            print('\n\n')
            
        else:
            print('No faces found')
    else:
        print('The string ',face_search,' was not found in ',file.filename,'\n\n')