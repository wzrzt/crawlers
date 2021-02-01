
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

driver = Chrome('./chromedriver.exe', options=chrome_options)

with open('stealth.min.js') as f:
    js = f.read()

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": js
})

driver.get('https://bot.sannysoft.com')
time.sleep(5)
driver.save_screenshot('walkaround.png')

# save source
souce = driver.page_source
with open('result.html', 'w') as f:
    f.write(souce)