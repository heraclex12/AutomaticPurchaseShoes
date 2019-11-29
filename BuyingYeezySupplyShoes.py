from selenium import webdriver
import time
import threading
import sys
from selenium.webdriver.chrome.options import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType

#PROXY BUYING CLASS
class BuyingShoesAutomationProxy():
    def __init__(self):
        self.__running = True
        self.ALL_PROXIES = get_proxies()
    def run(self, url):
        # purchase function
        second_timeout = 2
        if self.__running:
            try:
                browser = proxy_driver(self.ALL_PROXIES)
            except:
                new = self.ALL_PROXIES.pop()
                browser = proxy_driver(self.ALL_PROXIES)
                print("--- Switched proxy to: %s" % new)
                time.sleep(0.5)

            browser.get(url)
            time.sleep(second_timeout)
            cnt = 0
            flag = False
            while True:
                if cnt % 10 == 0:
                    browser.delete_all_cookies()
                    print(cnt)
                    if cnt == 100:
                        cnt = 0
                        browser.get(url)
                        time.sleep(second_timeout)

                while True:
                    try:
                        browser.find_element_by_xpath(
                            "//select[@class='gl-native-dropdown__select-element']/option[text()='12']").click()
                        break
                    except:
                        browser.delete_all_cookies()
                        browser.get(url)
                        time.sleep(second_timeout)

                browser.find_element_by_xpath("//button[@data-auto-id='ys-add-to-bag-btn']").click()
                elem = browser.find_elements_by_xpath("//a[@data-auto-id='yeezy-mini-basket']")
                for e in elem:
                    tmp = e.text
                    if "CART 1" in tmp:
                        browser.get("https://www.yeezysupply.com/delivery")
                        self.__running = False
                        flag = True
                if flag:
                    break
                cnt += 1

#NON-PROXY BUYING CLASS
class BuyingShoesAutomation():
    def __init__(self):
        self.__running = True
    def run(self, url):
        #purchase function
        second_timeout = 2
        if self.__running:
            options = webdriver.ChromeOptions()
            options.add_argument("--enable-javascript")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-extensions")
            options.add_argument("--start-maximized")
            options.add_argument('--no-sandbox')
            options.add_argument("user-agent={ Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36 }")
            browser = webdriver.Chrome(executable_path='chromedriver_linux64/chromedriver', options=options)
            browser.get(url)
            time.sleep(second_timeout)
            cnt = 0
            flag = False
            while True:
                if cnt % 10 == 0:
                    browser.delete_all_cookies()
                    print(cnt)
                    if cnt == 100:
                        cnt = 0
                        browser.get(url)
                        time.sleep(second_timeout)

                while True:
                    try:
                        browser.find_element_by_xpath("//select[@class='gl-native-dropdown__select-element']/option[text()='12']").click()
                        break
                    except:
                        browser.delete_all_cookies()
                        browser.get(url)
                        time.sleep(second_timeout)

                browser.find_element_by_xpath("//button[@data-auto-id='ys-add-to-bag-btn']").click()
                elem = browser.find_elements_by_xpath("//a[@data-auto-id='yeezy-mini-basket']")
                for e in elem:
                    tmp = e.text
                    if "CART 1" in tmp:
                        browser.get("https://www.yeezysupply.com/delivery")
                        self.__running = False
                        flag = True
                if flag:
                    break
                cnt += 1

# PROXY SECTION

def get_proxies():
    co = webdriver.ChromeOptions()
    co.add_argument("log-level=3")
    co.add_argument("--headless")
    driver = webdriver.Chrome(executable_path='chromedriver_linux64/chromedriver', options=co)
    driver.get("https://free-proxy-list.net/")

    PROXIES = []
    proxies = driver.find_elements_by_css_selector("tr[role='row']")
    for p in proxies:
        result = p.text.split(" ")

        if result[-1] == "yes":
            PROXIES.append(result[0]+":"+result[1])

    driver.close()
    return PROXIES


def proxy_driver(PROXIES):
    options = webdriver.ChromeOptions()
    options.add_argument("--enable-javascript")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--start-maximized")
    options.add_argument('--no-sandbox')
    options.add_argument("user-agent={ Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36 }")
    prox = Proxy()

    while True:
        if PROXIES:
            pxy = PROXIES.pop()
            break
        else:
            print("--- Proxies used up (%s)" % len(PROXIES))
            PROXIES = get_proxies()

    prox.proxy_type = ProxyType.MANUAL
    prox.http_proxy = pxy
    prox.socks_proxy = pxy
    prox.ssl_proxy = pxy

    capabilities = webdriver.DesiredCapabilities.CHROME
    prox.add_to_capabilities(capabilities)

    driver = webdriver.Chrome(executable_path='chromedriver_linux64/chromedriver', options=options, desired_capabilities=capabilities)

    return driver


if __name__ == '__main__':
    use_proxy = False
    passing_url = None
    time_range = 2
    number_section = 2
    time_delay = 0.2
    if len(sys.argv) >= 3:
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-u' or sys.argv[i] == '--url':
                passing_url = sys.argv[i + 1]

            elif sys.argv[i] == '-p' or sys.argv[i] == '--use-proxy':
                use_proxy = True

            elif sys.argv[i] == '-n' or sys.argv[i] == '--number':
                number_section = sys.argv[i + 1]

            elif sys.argv[i] == '-t' or sys.argv[i] == '--rtime':
                time_range = sys.argv[i + 1]

            elif sys.argv[i] == '-d' or sys.argv[i] == '--delay':
                time_delay = sys.argv[i + 1]

        if passing_url is None or passing_url == "":
            print("Missing url <!> Please add more \'--url https://abcxyz.com\'")
            exit(0)

        if use_proxy:
            thread_class = BuyingShoesAutomationProxy()
        else:
            thread_class = BuyingShoesAutomation()
        urls = []
        number_section = int(number_section)
        for k in range(number_section):
            urls.append(passing_url)

        sec = int(time_range)
        time_delay = float(time_delay)
        childs = []
        for step in range(0, int(sec / time_delay) + 1):
            childs.extend([threading.Thread(target=thread_class.run, args=(url,)) for url in urls])

        c_tmp = 0
        for child in childs:
            child.start()
            c_tmp += 1
            if c_tmp == number_section:
                time.sleep(time_delay)
                c_tmp = 0

        for child in childs:
            child.join()

        print("<-DONE->")

    else:
        print("You must pass url into program!")