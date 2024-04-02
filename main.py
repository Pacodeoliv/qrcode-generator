import segno
import os
import urllib.parse
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




# Receive from the user what will be used to create the QR Code (can be a link or text)
alternative = input("Enter what you want to include in the QR Code (can be a link or text): ")

# Check if what the user entered is a link or text
if alternative.startswith("http://") or alternative.startswith("https://"):
    # If it's a link, create the QR Code with the provided link
    url = alternative
    filename = urllib.parse.quote_plus(url) + ".png"
    qr_code = segno.make(url)
else:
    # If it's text, use the text as the content of the QR Code
    filename = f"{alternative}.png"
    qr_code = segno.make(alternative)

# Save the QR Code as a PNG image
qr_code_path = os.path.join(dirt, filename)
if not os.path.exists(qr_code_path):
    qr_code.save(qr_code_path, scale=10)
    print(f"QR Code saved at: {qr_code_path}")
else:
    print("The file already exists.")
