import time

from seleniumwire import webdriver

proxy = 'http://scraperapi:03a620dbdc81e9e5c772a86859eb777a@proxy-server.scraperapi.com:8001'
# proxy = "https://api.scrape.do/?token=aa48e53ef4934d95a56acecacaec8fe454ebf634a98"
# proxy = "http://9dbe950ef6284a5da9e7749db9f7cbd1:@api.zyte.com:8011/"

seleniumwire_options = {
    'proxy': {
        'http': proxy,
        'https': proxy,  # Use the same proxy for HTTPS
    }
}
# Create a WebDriver instance with Selenium Wire
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(seleniumwire_options=seleniumwire_options)

driver.get("https://httpbin.org/ip")
driver.get("https://m.shein.com/us/pdsearch/pants/")

time.sleep(100)
# Close the browser
driver.quit()
