from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from colorama import Fore
from colored import fg
from dhooks import Webhook
zold=fg('green')

options = Options()
options.add_argument('--log-level=3')
options.add_argument("--disable-notifications")

PATH = "C:\Program Files (x86)\chromedriver.exe"

def varakozas():
    while True:
        val = driver.find_element(By.CSS_SELECTOR, '#remain')
        if val.text != '28':
            sleep(1)
        else:
            break

print("")
wh = input(" --> Add meg a Discord Webhook linket: ")
hook = Webhook(wh)

driver = webdriver.Chrome(options=options, executable_path=PATH)
driver.maximize_window()
driver.get("https://fecooo.github.io/nitro")
sleep(3)

while True:
    url = driver.find_element(By.XPATH, '//*[@id="link"]')
    link = url.text
    print(link)

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    sleep(1)
    driver.get(link)
    sleep(10)

    html_source = driver.page_source

    for i in range(1):
        if "Ajándékkód érvénytelen" in html_source:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            sleep(2)
        else:
            print(f" --> ÉRVÉNYES GIFT: {link}")
            hook.send(f" --> **ÉRVÉNYES GIFT:** {link}")
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            sleep(2)
    sleep(2)
    varakozas()
    print("-----------")