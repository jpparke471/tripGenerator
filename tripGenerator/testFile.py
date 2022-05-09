from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/jparke2/Desktop/tripGenerator/tripGenerator/chromedriver')
driver.get('https://www.momondo.com')


fromField = 'zEiP-origin'
fromFieldTwo = 'k_my-input'
datesField = 'zEiP-dates'
datesMonthButton = 'M8yV-mod-pres-datePicker'
#data-index = 2
searchButton = 'zEiP-submit'
exploreButton = '/html/body/div[4]/div/div[3]/div/div/div[2]/div/div[2]/div[2]/button'

resultsContainer = '/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div/div'

try:
    wait = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, fromField))
    )
    current = driver.find_element_by_class_name(fromField)
    current.click()
    current = driver.find_element_by_class_name(fromFieldTwo)
    current.send_keys("dtw")
    current.send_keys(Keys.RETURN)

    current = driver.find_element_by_class_name(datesField)
    current.click()
except:
    print("Initial Connection Failure")

try:
    wait = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, datesMonthButton))
    )

    current = driver.find_element_by_class_name(datesMonthButton)
    current.click()

    current = driver.find_element_by_class_name(searchButton)
    current.click()

    
except:
    print("Date Format Changed")

try:
    wait = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, exploreButton))
    )

    current = driver.find_element_by_xpath(exploreButton)
    current.click()
except:
    print("Explore Button Not Found")

try:
    wait = WebDriverWait(driver, timeout=5, poll_frequency=1).until(
        EC.visibility_of_element_located((By.XPATH, resultsContainer))
    )
    results = []
    for i in range(1,13):
        print(i)
        result = resultsContainer + "/div[" + i + "]"
        print(result)
        resultName = result+'/div/button/div/div[2]/div[1]/div[1]'
        print(resultName)
        resultPrice = result+'/div/button/div/div[2]/div[1]/div[2]'
        print(resultPrice)
        resultDate = result+'/div/button/div/div[2]/div[2]/div[2]'
        print(resultDate)
        name=driver.find_element_by_xpath(resultName)
        price=driver.find_element_by_xpath(resultPrice)
        date=driver.find_element_by_xpath(resultDate)

        results.append([name.text,price.text,date.text])
        print(results)
except:
    print("Travel Results Not Found")
    print(driver.find_element_by_xpath(resultsContainer))