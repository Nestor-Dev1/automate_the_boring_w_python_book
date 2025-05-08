import pyperclip

text = pyperclip.paste() #Obtiene el texto del portapapeles
alt_text = '' #Esta cadena almacenara la cadena nueva
make_uppercase = False
for character in text:
    #Va a traves de cada caracter y lo añade a alt_text
    if make_uppercase:
        alt_text += character.upper()
    else:
        alt_text += character.lower()

    make_uppercase = not make_uppercase

pyperclip.copy(alt_text)
print(alt_text)