import pyshorteners

link = input('Enter the link you want to shorten: ')

s = pyshorteners.Shortener()
print(s.tinyurl.short(link))



