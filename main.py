import segno
import os

dirt = "C:/Users/Paco De Oliveira/PycharmProjects/qr-codegenerator/qrcodes_directory"

if not os.path.exists(dirt):
    os.makedirs(dirt)
"""
#Create QR Code for the number 30142
churineu = segno.make("30142") # Correction here
churineu_path = os.path.join(dirt, "badge.png")
if not os.path.exists(churineu_path):
    churineu.save(churineu_path, border=5)
else:
    print("The file 'badge.png' already exists.")

#Create QR Code for "Hello World"
price_tag = segno.make("Hello World")
price_tag_path = os.path.join(dirt, "hello-world.png")
if not os.path.exists(price_tag_path):
    price_tag.save(price_tag_path)
else:
    print("The file 'hello-world.png' already exists.")
    
I was trying to learn how i shouldve done here   
    
    
"""




alternative = input("Type your QRcode:") #Receive from user what's supposed to be created
alt = alternative
alt1 = os.path.join(dirt,f"{alt}.png")
if not os.path.exists(alt1):
    qr_code = segno.make(alt) #Makes the QRcode with .make
    qr_code.save(alt1)   #Saves the QRcode
else:
    print("The archive already exists")
