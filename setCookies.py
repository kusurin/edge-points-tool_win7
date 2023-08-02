from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time
import json

options_reader = open('.\options.txt','r',encoding='UTF-8')
options = Options()
line = options_reader.readline()
while line:
        options.add_argument(line)  # 设置后台运行，无窗口化
        line = options_reader.readline()
options_reader.close()
# 在msedgedriver_path.txt填写webdriver的保存目录（win7填写绝对路径）
driver_reader = open('.\msedgedriver_path.txt','r',encoding='UTF-8')
driverPath = driver_reader.readline()
driver = webdriver.Edge(driverPath,options=options)
driver_reader.close()

# 记得写完整的url 包括http和https
driver.get('https://cn.bing.com/')

# 程序打开网页后10秒内 “手动登陆账户”
time.sleep(10)

with open('cookies.txt', 'w') as f:
    # 将cookies保存为json格式
    f.write(json.dumps(driver.get_cookies()))

driver.close()
print('用户Cookies读取完成')
