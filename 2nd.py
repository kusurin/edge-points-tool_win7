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


def getScore(str, l):
    times = 0
    for i in l:
        times += 1
        run_pc(i)
        print(str + '第', times, '次完成')
        time.sleep(2)
    driver.quit()


if __name__ == "__main__":
    timesPC = 30  # PC端次数
    timesMobile = 20  # 移动端次数
    timesSum = timesPC + timesMobile  # PC端和移动端总次数
    List = random.sample(range(1, 1000), timesSum)

    options = Options()
    # 设置driver路径
    driverPath = 'C:/Users/Windy/EdgeDriver/msedgedriver'
    # options.add_argument("--headless")  #设置后台运行，无窗口化

    # PC端
    driver = webdriver.Edge(driverPath, options=options)
    getScore('PC端', List[:timesPC])
    print('PC端完成')

    # 移动端
    mobile_emulation = {'deviceName': 'iPhone 6'}  # 添加移动端
    # mobile_emulation = {'deviceName': 'Pixel 5'}  # 添加移动端
    options.add_experimental_option("mobileEmulation", mobile_emulation)  # 使用移动端模拟器打开
    driver = webdriver.Edge(driverPath, options=options)
    getScore('移动端', List[timesPC:])
    print('移动端完成')
