from playwright.sync_api import sync_playwright

# Your Zyte API key
zyte_api_key = "fa987dsff87saf8saf8af97a98f7"
proxy_urls = f"http://api.zyte.com:8011/"
api_http = "http://fa987dsff87saf8saf8af97a98f7:@api.zyte.com:8011/"



def main():
    with sync_playwright() as p:
        # Launch the browser with Zyte proxy settings
        browser = p.chromium.launch(headless=False,
                                    proxy={
                                        "server": proxy_urls,
                                        "username": zyte_api_key,
                                    }, timeout=20000, args=["--ignore-certificate-errors"])
        context = browser.new_context()

        # Open a page to verify if the proxy is working
        page = context.new_page()
        try:
            page.goto("https://httpbin.org/ip")
            print(page.content())  # Should display the proxy IP
        except Exception as e:
            print("Error occurred:", e)

        # Close the browser
        browser.close()



if __name__ == "__main__":
    main()