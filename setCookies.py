from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time
import json

# 填写webdriver的保存目录
driver = webdriver.Edge('C:/Users/Windy/EdgeDriver/msedgedriver')

# 记得写完整的url 包括http和https
driver.get('https://cn.bing.com/')

# 程序打开网页后10秒内 “手动登陆账户”
time.sleep(10)

with open('cookies.txt', 'w') as f:
    # 将cookies保存为json格式
    f.write(json.dumps(driver.get_cookies()))

driver.close()
