import qrcode

data = "https://github.com/Dragonemperor-J/QR-Code-Scanner-and-Generator/"
filename = "site.png"

img = qrcode.make(data)

img.save(filename)
