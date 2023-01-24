from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.get("https://www.tokopedia.com")

# keyword = driver.find_element(By.NAME, "q")

# keyword.send_keys("Hello World")

# keyword.send_keys(Keys.RETURN)

driver.execute_script("window.scrollTo(3, document.body.scrollHeight);")