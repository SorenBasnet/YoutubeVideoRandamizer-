import selenium 

linkFile = open("links.txt", "r")

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(PATH)

x = linkFile.readline() 

driver.get(x)

wait = WebDriverWait(driver, 20*60)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='skip-button:6']/span/button")))

element.click()

# button = driver.find_element_by_class_name('ytp-ad-skip-button-container')
# button.click() 

# try:
#     skip_button = driver.find_element_by_xpath('//*[@id="skip-button:6"]/span/button')
#     skip_button.click()
# except:
#     print('no ad')

# current = driver.find_element_by_xpath('//*[@id="movie_player"]/div[28]/div[2]/div[1]/div[1]/span[1]')
# duration = driver.find_element_by_xpath('//*[@id="movie_player"]/div[28]/div[2]/div[1]/div[1]/span[3]')

# # checks if the current time equals the duration
# if current.text == duration.text:
#     print('true')
# else:
#     print('flase')

# driver.get("https://www.youtube.com/watch?v=QVlfINuDdKE&list=RDMM&index=5")


