import requests

img_url = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"

image = requests.get(img_url)

with open('google.png', 'wb') as file:
    file.write(image.content)
