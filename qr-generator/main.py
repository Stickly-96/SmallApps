import qrcode
# sample data
data = "https://pythonist.ru/"
# output file name
filename = "site.png"
# генерируем qr-код
img = qrcode.make(data)
# save img to file
img.save(filename)
