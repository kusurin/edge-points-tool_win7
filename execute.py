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
    timesPC = 40  # PC端次数
    timesMobile = 30  # 移动端次数
    timesSum = timesPC + timesMobile  # PC端和移动端总次数
    List = random.sample(range(1, 10000), timesSum)

    options = Options()
    # 设置driver路径
    driverPath = 'C:/Users/Windy/EdgeDriver/msedgedriver'
    options.add_argument("--headless")  # 设置后台运行，无窗口化

    # PC端
    driver = webdriver.Edge(driverPath, options=options)
    getScore('PC端', List[:timesPC])
    print('PC端完成')

    # 移动端
    mobile_emulation = {'deviceName': 'Galaxy S5'}  # 添加移动端
    options.add_experimental_option("mobileEmulation", mobile_emulation)  # 使用移动端模拟器打开
    driver = webdriver.Edge(driverPath, options=options)
    getScore('移动端', List[timesPC:])
    print('移动端完成')

    # deviceName列表
    # "deviceName": "Apple iPhone 3GS",
    # "deviceName": "Apple iPhone 4",
    # "deviceName": "Apple iPhone 5",
    # "deviceName": "Apple iPhone 6",
    # "deviceName": "Apple iPhone 6 Plus",
    # "deviceName": "BlackBerry Z10",
    # "deviceName": "BlackBerry Z30",
    # "deviceName": "Google Nexus 4",
    # "deviceName": "Google Nexus 5",
    # "deviceName": "Google Nexus S",
    # "deviceName": "HTC Evo, Touch HD, Desire HD, Desire",
    # "deviceName": "HTC One X, EVO LTE",
    # "deviceName": "HTC Sensation, Evo 3D",
    # "deviceName": "LG Optimus 2X, Optimus 3D, Optimus Black",
    # "deviceName": "LG Optimus G",
    # "deviceName": "LG Optimus LTE, Optimus 4X HD",
    # "deviceName": "LG Optimus One",
    # "deviceName": "Motorola Defy, Droid, Droid X, Milestone",
    # "deviceName": "Motorola Droid 3, Droid 4, Droid Razr, Atrix 4G, Atrix 2",
    # "deviceName": "Motorola Droid Razr HD",
    # "deviceName": "Nokia C5, C6, C7, N97, N8, X7",
    # "deviceName": "Nokia Lumia 7X0, Lumia 8XX, Lumia 900, N800, N810, N900",
    # "deviceName": "Samsung Galaxy Note 3",
    # "deviceName": "Samsung Galaxy Note II",
    # "deviceName": "Samsung Galaxy Note",
    # "deviceName": "Samsung Galaxy S III, Galaxy Nexus",
    # "deviceName": "Samsung Galaxy S, S II, W",
    # "deviceName": "Samsung Galaxy S4",
    # "deviceName": "Sony Xperia S, Ion",
    # "deviceName": "Sony Xperia Sola, U",
    # "deviceName": "Sony Xperia Z, Z1",
    # "deviceName": "Amazon Kindle Fire HDX 7″",
    # "deviceName": "Amazon Kindle Fire HDX 8.9″",
    # "deviceName": "Amazon Kindle Fire (First Generation)",
    # "deviceName": "Apple iPad 1 / 2 / iPad Mini",
    # "deviceName": "Apple iPad 3 / 4",
    # "deviceName": "BlackBerry PlayBook",
    # "deviceName": "Google Nexus 10",
    # "deviceName": "Google Nexus 7 2",
    # "deviceName": "Google Nexus 7",
    # "deviceName": "Motorola Xoom, Xyboard",
    # "deviceName": "Samsung Galaxy Tab 7.7, 8.9, 10.1",
    # "deviceName": "Samsung Galaxy Tab",
    # "deviceName": "Notebook with touch",
    # "deviceName": "iPhone 6"

