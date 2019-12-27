import webbrowser, pyperclip, sys


if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

print ('The Address you are being redirected to is : ' + address) 

webbrowser.open('https://www.google.com/maps/place/' + address)

