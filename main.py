import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
# from selenium.webdriver.common.keys import Keys
# from datetime import datetime

with open('README.txt') as file:
    all_ = file.readlines()
    chrome_driver_path = all_[0].strip()

# chrome_driver_path = 'chromedriver_LINUX_v_107'
s = Service(chrome_driver_path)
# URL = 'https://www.rottentomatoes.com/tv/the_white_lotus'
# URL =
# URL = 'https://www.rottentomatoes.com/tv/the_peripheral'
with open(file='URL.txt') as file:
    links = file.readlines()


def solves_cookies():
    i_accept_cookies = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
    i_accept_cookies.click()


def main_function(URL):
    global name_of_the_show, driver
    driver = webdriver.Chrome(service=s)
    driver.get(URL)
    time.sleep(1)
    solves_cookies()
    # # main info:
    name_of_the_show = driver.find_element(By.CLASS_NAME, 'title').text
    # print(f'name of the show : {name_of_the_show}')
    tomatometer = driver.find_elements(By.CLASS_NAME, 'mop-ratings-wrap__percentage')
    average_tomato = tomatometer[0].text
    audience_score = tomatometer[1].text
    # print(f'scores: {average_tomato} and {audience_score}')
    reviews_page = driver.find_element(By.CLASS_NAME, 'mop-ratings-wrap__icon-link')
    reviews_link = reviews_page.get_property('href')
    # reviews_link = 'https://www.rottentomatoes.com/tv/the_white_lotus/s02/reviews'
    driver.get(reviews_link)
    time.sleep(1)

    header = ['USERNAME', 'RATING FOR THE SHOW', 'REVIEW TEXT', "URL TO THE REVIEWER'S PROFILE",
              'THE NUMBER OF TOTAL REVIEWS FOR THE REVIEWER', 'TOMATOMETER', 'AUDIENCE SCORE']
              # "something random because AUDIENCE SCORE doesn't show up"]
    first_line = ['', '', '', '', '', average_tomato, audience_score]
    with open(file=f'{name_of_the_show}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerow(first_line)


def total_reviews(link):
    driver.execute_script("window.open('');")

    # Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[1])
    driver.get(link)
    for _ in range(2):
        try:
            time.sleep(1)
            time.sleep(1)
            try:
                tv_button = driver.find_element(By.XPATH, '//*[@id="filter-chips-wrapper"]/filter-chip/label')
                tv_button.click()
                tv_button2 = driver.find_element(By.XPATH, '//*[@id="filter-chips-wrapper"]/filter-chip[2]/label')
                tv_button2.click()
            except:
                pass
            time.sleep(1)
            reviews_number = len(driver.find_elements(By.CSS_SELECTOR, 'tr')) - 1
            next_page = driver.find_element(By.ID, 'pagination-next').get_attribute('class')[5:]
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            if next_page == 'hide':
                return reviews_number
            else:
                return f'{reviews_number}+'
        # except Exception as e:
        except:
            driver.refresh()
            time.sleep(5)
            # print(e)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    return 'no data available'


def get_data_from_one_page():

    rows = driver.find_elements(By.CLASS_NAME, 'review_table_row')
    for row in rows:
        row_to_csv = []
        # time.sleep(10)
        critic_name_element = row.find_element(By.CLASS_NAME, 'critic__name')
        username = critic_name_element.text
        link_to_user = critic_name_element.get_property("href")
        row_to_csv.append(username)
        # print(f'username: {username} \nlink: {link_to_user}')
        review_container = row.find_element(By.CLASS_NAME, 'review_container')
        rate = review_container.find_element(By.CLASS_NAME, 'review_icon').get_attribute('class')[23:]
        # print(f'rate: {rate}')
        review_text = row.find_element(By.CLASS_NAME, 'critic__review-quote').text
        # print(review_text)
        original_score = row.find_elements(By.CLASS_NAME, 'subtle')[1].text[14:]
        # print(original_score)
        rating_for_the_show = f'{rate}, {original_score}'
        row_to_csv.append(rating_for_the_show)
        row_to_csv.append(review_text)
        row_to_csv.append(link_to_user)
        tot_reviews = total_reviews(link_to_user)
        row_to_csv.append(tot_reviews)
        with open(file=f'{name_of_the_show}.csv', mode='a', newline='')as file:
            writer = csv.writer(file)
            writer.writerow(row_to_csv)
        # print(f'nr of the reviews by the reviewer {total_reviews(link_to_user)}')
        time.sleep(1)
        # print('\n\n\n'
    driver.quit()


for URL in links:
    URL = URL.strip()
    main_function(URL)
    get_data_from_one_page()
# total_reviews('https://www.rottentomatoes.com/critics/kaleena-rivera')

# time.sleep(1000000)

