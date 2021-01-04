from selenium import webdriver

chrome_driver_path = "/usr/local/bin/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com")
driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=sr_1_3?dchild=1&keywords=instant+pot+duo+evo+plus+9&qid=1609618556&sr=8-3")
price = driver.find_element_by_id("priceblock_ourprice")
# //*[@id="priceblock_ourprice"]
print(price.text)
driver.close()
