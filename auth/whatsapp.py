import base64
from selenium import webdriver
import pyderman as driver
import time
import os
from selenium.webdriver.firefox.options import Options


def get_picture(element, name='canvas'):
    try:
        image = element.screenshot_as_base64

        # decode
        image_dcd = base64.b64decode(image)

        # save to a file
        path = os.path.dirname(os.path.abspath(__file__))

        filename = "{}/{}.png".format(path, name)
        print(filename)

        with open(filename, 'wb') as f:
            f.write(image_dcd)

        return filename

    except:
        print("Não foi possível gravar um foto")

def get_image_auth(browser):
    # browser.navigate().refresh()
    try:
        image = browser.find_element_by_tag_name("canvas")

        # decode
        imagem_canvas = get_picture(image)

    except:
        print("Impossível gerar imagem de autenticação")

def get_browser(url, headless=False):
    # Install webdriver
    path = driver.install(browser=driver.firefox, overwrite=False, verbose=True)

    options = Options()
    options.headless = headless

    browser = webdriver.Firefox(options=options, executable_path=path)

    browser.get(url)

    return browser


def cadastrar_novos_leads(conversas_id):
    pass



url = 'https://web.whatsapp.com/'
browser = get_browser(url, headless=False)


url = 'file:///opt/whatsapp/auth/index.html'
browser_auth = get_browser(url)


logado=False

while not logado:
    time.sleep(5)
    get_image_auth(browser)
    browser_auth.refresh()
    try:
        logado = browser.find_element_by_xpath("//*[@role='region']")
        print('LOGADO')
    except:
        print('AINDA NAO EFETUOU O LOGIN')

browser_auth.quit()

conversas_id = browser.find_element_by_xpath("//*[@role='region']")

get_picture(conversas_id, 'conversas')
browser.refresh()

mensagens = {}
while True:
    time.sleep(5)
    # browser.find_element_by_xpath("//*[@aria-label='region']")

    # print('BUSCANDO NAO LIDAS')


    try:

        msg_from = browser.find_element_by_xpath("//*[contains(@aria-label,'não lida')]/../../../../..").text.split('\n')[0]
        msg_hour = browser.find_element_by_xpath("//*[contains(@aria-label,'não lida')]/../../../../..").text.split('\n')[1]

        browser.find_element_by_xpath("//*[contains(@aria-label,'não lida')]/../../../../../..").click()
        # print('clicou nao lidas')

        element_ids = browser.find_elements_by_xpath("//*[@data-pre-plain-text]")

        if not mensagens.get(msg_from):
            mensagens[msg_from] = {}

        for element_id in element_ids:

            if not mensagens.get(msg_from).get(element_id.text):
                mensagens.get(msg_from)[element_id.text] = 'HORA'
                print('{}:{}'.format(msg_from, element_id.text))
                # print()

        browser.refresh()

    except:
        pass


# //*[@aria-label]

# //*[matches(@aria-label, 'mensagens')]

# //*[contains(@aria-label,'não lida')]/../../../../..voc