from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from retry import retry     #retry和retrying是两个包，用法不同，详见：https://blog.csdn.net/TFATS/article/details/106141062
import requests
import json


class Student(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @retry(tries=30,delay=5,backoff=2,max_delay=60)#运行失败则重新运行，
    def submit_form(self):
        s = Service("./chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.implicitly_wait(10) # seconds 
        #打卡网站
        driver.get('http://authserver.hhu.edu.cn/authserver/login?service=http%3A%2F%2Fmy.hhu.edu.cn%2Fportal-web%2Fj_spring_cas_security_check')

        # 登录
        sleep(1)
        driver.find_element(by=By.XPATH, value='//*[@id="username"]').send_keys(self.username)
        driver.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys(self.password)
        sleep(1)
        driver.find_element(by=By.XPATH, value='//*[@id="casLoginForm"]/p[5]/button').click()
        sleep(1)
        driver.get('http://dailyreport.hhu.edu.cn/pdc/form/list')
        sleep(1)
        driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[4]/div/section/section/div/a').click()
        sleep(1)
        driver.find_element(by=By.XPATH, value='//*[@id="d-RADIO_799044"]/div/label[1]/input').click()
        sleep(1)
        driver.find_element(by=By.XPATH, value='//*[@id="saveBtn"]').click()
        sleep(5)
        
        driver.quit()



#将打卡情况发送到主页
def post(aa):
    data ={
        XXXXXX
    }
    req = requests.post("https://XXXXXX",data=json.dumps(data))  # 发post请求,以json字符串参数格式
    a=json.loads(req.text)["retlist"][1]["content"]
    print(a)

    data1 = {
        XXXXXXX
    }
    req = requests.post("https://XXXXXX",data=json.dumps(data1))  # 发post请求,以json字符串参数格式
    print(req.text)





#if __name__ == "__main__":
con =  time.strftime("%Y年%m月%d日%H点%M分", time.localtime())
try:
    Student("XXXXXXXXXXXX", "XXXXXXXXXXXXX").submit_form()
    con = con+"**打卡成功**\n"
    
except:
    con = con+"**打卡失败**\n"
post("- "+con)

