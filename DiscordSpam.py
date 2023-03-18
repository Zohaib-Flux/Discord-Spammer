from threading import Thread
from turtle import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#i'm really proud of the code below because it is the only code i didn't have to google for errors. 😀
uname = input("What is your discord email/username? ")
pas = input("What is your Discord Password? ")
mess = input("What would you like to send? ")
path = input("what is the XPATH of the chat you would like to spam (to find this please refer to instructions.txt) ")

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete
ts =  webdriver.Chrome()
ts.get('https://discord.com/login')

time.sleep(5.5)

username = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/input")
username.send_keys(uname)
password = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/div[2]/div/input")
password.send_keys(pas)
login = ts.find_element(By.XPATH, "//html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/button[2]")
login.click()

time.sleep(10.5)

channel = ts.find_element(By.XPATH, path)
channel.click()

time.sleep(4.5)

#from here everything just repeats. i couldn't be bothered to repeat the same line of code so i copied
#and pasted everything multiple times. 

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

type = ts.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div")
type.send_keys(mess)
type.send_keys(Keys.ENTER)

time.sleep(10.5);




#quizz home
#quizz = ts.find_element(By.XPATH, "/html/body/tasso-app/tasso-wheel-highlighter/tasso-entry/div/div/learner-dashboard/div[2]/discipline-dashboard-container/discipline-dashboard/div/quiz-suggestion-list/quiz-suggestion-card[1]/button/div[1]/div[2]")
#quizz.click()

#for i in range(3):
  # [here goes your code]