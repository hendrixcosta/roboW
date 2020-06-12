import base64
from selenium import webdriver
import pyderman as driver
import time




# Install webdriver
path = driver.install(browser=driver.firefox, overwrite=False, verbose=True)
#
browser = webdriver.Firefox(executable_path=path)
#
# browser.get("https://web.whatsapp.com/")
#
#
#
# image_path = '/opt/whatsapp/auth/download.jpeg'
# browser.get(image_path)
#


# driver = webdriver.Chrome()
# browser.get("http://curran.github.io/HTML5Examples/canvas/smileyFace.html")
browser.get("https://web.whatsapp.com/")

time.sleep(5)

image = browser.find_element_by_tag_name("canvas").screenshot_as_base64

# decode
canvas_png = base64.b64decode(image)

# save to a file
with open(r"/tmp/canvas.png", 'wb') as f:
    f.write(canvas_png)


