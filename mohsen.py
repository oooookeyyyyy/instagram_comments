import selenium.webdriver as wd
from time import sleep
import csv

driver = wd.Firefox() # you can change it to other browsers
username = '' # replace your instagram username here
password = '' # replace your instagram password here

def login(username, password) :
    driver.find_element_by_xpath('//input[@name="username"]').send_keys(username)
    driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)
    driver.find_element_by_xpath('//button[@type="submit"]').click()

def fetch_comments(link):
    driver.get(link)
    i = 1
    while True:
        try:
            comment = driver.find_element_by_xpath(f'//article/div/div[2]/div/div[2]/div[1]/ul/ul[{i}]/div/li/div/div/div[2]/span').text
            with open('comments.csv', 'a', encoding='UTF-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([comment])
                f.close()
            if i % 12 == 0:
                sleep(2)
                driver.find_element_by_xpath('//article/div/div[2]/div/div[2]/div[1]/ul/li/div/button').click()
                sleep(2)
            i+=1
        except Exception as e:
            print(e)
            print('Done!')
            break

def main() :
    driver.get('https://www.instagram.com/')
    try :
        driver.find_element_by_xpath('//button[text()="Accept"]').click()
    except :
        pass
    sleep(2)
    login(username, password)
    sleep(8)
    try :
        login(username, password)
    except :
        pass
    sleep(5)
    while True:
        fetch_comments(input('post link >>'))

if __name__ == '__main__':
    main()