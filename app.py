from selenium import webdriver

# Return a list ~ Ask User to pick a Stock
stocks = ['Amazon', 'Shopify', 'Palentir', 'Wish', 'AMC']

for stock in stocks:
    print(stock)

print('Here are a brief list of stocks')
stockName = input('Please Choose a Stock Name: ')

# Functions for Stock Price based on chosen stock name


def amazon():
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/search?q=amazon+stock&oq=amazon+stock&aqs=chrome.0.69i59j69i64j0i271l2.11726j0j1&sourceid=chrome&ie=UTF-8').click()


def shopify():
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/search?q=shopify+stock&oq=shopify+stock&aqs=chrome.0.69i59j0i67i433j0i20i131i263i433j0i67j0i67i433l2j0i67l2j0i131i433.3457j0j7&sourceid=chrome&ie=UTF-8').click()


def palentir():
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/search?q=palantir+stock&oq=pa&aqs=chrome.2.69i57j69i59j35i39i285j35i39j0i67j69i61l3.3281j1j7&sourceid=chrome&ie=UTF-8').click()


def wish():
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/search?q=wish+stock&oq=wish+stoc&aqs=chrome.0.69i59j69i57j0j0i10j46j0i10j0j0i10l3.2087j1j7&sourceid=chrome&ie=UTF-8').click()


def amc():
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/search?q=amc+stock&oq=AMC+stock&aqs=chrome.0.69i59j69i57j69i59j0i271j69i60l2j69i61j69i60.1307j0j7&sourceid=chrome&ie=UTF-8').click()

# Running the program based on stock name chosen


if stockName == 'Amazon':
    amazon()
elif stockName == 'Shopify':
    shopify()
elif stockName == 'Palentir':
    palentir()
elif stockName == 'Wish':
    wish()
elif stockName == 'AMC':
    amc()
