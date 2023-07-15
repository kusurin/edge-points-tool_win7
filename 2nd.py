import json
import random
from selenium import webdriver
from selenium.webdriver.edge.options import Options

import time


def OpenUrl(url):
    # 访问网址
    driver.get(url)
    with open('cookies.txt', 'r') as f:  # 由于webdriver启动时类似无痕模式，使用带cookie的方式登录微软账号
        cookies_list = json.load(f)
        for cookie in cookies_list:
            if isinstance(cookie.get('expiry'), float):
                cookie['expiry'] = int(cookie['expiry'])
            driver.add_cookie(cookie)


def run_pc(random_number):
    OpenUrl('https://cn.bing.com/search?q=' + str(random_number))


def getScore(str, times):
    for i in range(times):  # 每次搜索获取3积分，根据个人等级调整循环次数timse
        random_number = random.randint(1, 10000)
        run_pc(random_number)
        print(str + '第', i + 1, '次完成')
        time.sleep(2)
    driver.quit()


if __name__ == "__main__":
    options = Options()
    # 设置driver路径
    driverPath = 'C:/Users/Windy/EdgeDriver/msedgedriver'
    # options.add_argument("--headless")  #设置后台运行，无窗口化

    # PC端
    driver = webdriver.Edge(driverPath, options=options)
    getScore('PC端', 35)
    print('PC端完成')

    # 移动端
    mobile_emulation = {'deviceName': 'iPhone 6'}  # 添加移动端
    # mobile_emulation = {'deviceName': 'Pixel 5'}  # 添加移动端
    options.add_experimental_option("mobileEmulation", mobile_emulation)  # 使用移动端模拟器打开
    driver = webdriver.Edge(driverPath, options=options)
    getScore('移动端', 25)
    print('移动端完成')
