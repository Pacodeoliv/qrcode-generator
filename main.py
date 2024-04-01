import segno
import os

dirt = "C:/Users/Paco De Oliveira/PycharmProjects/qr-codegenerator/qrcodes_directory"

if not os.path.exists(dirt):
    os.makedirs(dirt)

# Criar QR Code para o número 30142
churineu = segno.make("30142")  # Correção aqui
churineu_path = os.path.join(dirt, "cracha.png")
if not os.path.exists(churineu_path):
    churineu.save(churineu_path, border=5)
else:
    print("O arquivo 'cracha.png' já existe.")

# Criar QR Code para "Hello World"
price_tag = segno.make("Hello World")
price_tag_path = os.path.join(dirt, "hello-world.png")
if not os.path.exists(price_tag_path):
    price_tag.save(price_tag_path)
else:
    print("O arquivo 'hello-world.png' já existe.")
