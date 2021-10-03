from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



email =  ''
password = ''

### xpath needed ###
username='//*[@id="login_field"]'
Password='//*[@id="password"]'
login='/html/body/div[3]/main/div/div[4]/form/div/input[12]'

Create_repo='/html/body/div[4]/main/div/form/div[4]/button'
repo_name='//*[@id="repository_name"]'

### the function that makes the repo  ###
def makerepo(reponame):
    try:
        #open the firefox driver
        driver = webdriver.Firefox(executable_path=r'D:\Downloads\project\Bots automation\webdriver\geckodriver.exe')
        #go to the link
        driver.get('https://github.com/new')
        time.sleep(2)
        # login 
        driver.find_element_by_xpath(username).send_keys(email)
        driver.find_element_by_xpath(Password).send_keys(password)
        time.sleep(0.25)
        driver.find_element_by_xpath(login).click()
        time.sleep(2)
        #creating new repo
        driver.find_element_by_xpath(repo_name).send_keys(reponame)
        time.sleep(3)
        driver.find_element_by_xpath(Create_repo).click()
        
        print('repository was created successfully.')
    except:
        print('Erreur repository not created!')

# get name of repository and call the function
name=input('repository name :')
makerepo(name)


