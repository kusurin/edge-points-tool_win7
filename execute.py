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


def run_pc(random_item):
    OpenUrl('https://cn.bing.com/search?q=' + random_item)


delay_max = random.randint(1200,2000)

def getScore(str, l):
    times = 0
    for i in l:
        times += 1
        run_pc(i)
        print(str + '第', times, '次完成')
        time.sleep(float(random.randint(200,delay_max))/100)
    driver.quit()


if __name__ == "__main__":
    timesEdge = random.randint(6,10)  # Microsoft Edge奖励次数
    timesPC = random.randint(30,40)  # 电脑搜索次数
    timesMobile = random.randint(30,40)  # 移动设备搜索次数
    timesSum = timesEdge + timesPC + timesMobile  # 总次数
    
    #从searchitems.txt读取搜索项目
    items_reader = open('.\searchitems.txt','r',encoding='UTF-8')
    List = []
    while True:
        line=items_reader.readline()
        if not line:
            break
        if line == '\n':
            continue
        List.append(line)
    items_reader.close()
    if timesSum > len(List):
        print("搜索项不足")
        exit()
    random.shuffle(List)

    options_reader = open('.\options.txt','r',encoding='UTF-8')
    options = Options()
    options_edge = Options()
    line = options_reader.readline()
    while line:
        line = line.replace('\n','')
        options.add_argument(line)
        if line != "--headless": # edge奖励不能无窗口运行
            options_edge.add_argument(line)
        line = options_reader.readline()
    options_reader.close()
    # 在msedgedriver_path.txt设置driver路径（win7使用绝对路径）
    driver_reader = open('.\msedgedriver_path.txt','r',encoding='UTF-8')
    driverPath = driver_reader.readline()
    driver_reader.close()

    # Microsoft Edge奖励
    driver = webdriver.Edge(driverPath, options=options_edge)
    getScore('Edge奖励', List[:timesEdge])
    del List[:timesEdge]
    print('Microsoft Edge奖励完成')

    # 电脑搜索
    driver = webdriver.Edge(driverPath, options=options)
    getScore('电脑搜索', List[:timesPC])
    del List[:timesMobile]
    print('电脑搜索完成')

    # 移动设备搜索
    mobile_emulation = {'deviceName': "iPhone 12 Pro"}  # 添加移动设备搜索
    options_edge.add_experimental_option("mobileEmulation", mobile_emulation)  # 使用移动设备搜索模拟器打开
    user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    options_edge.add_argument(f"user-agent={user_agent}") 
    driver = webdriver.Edge(driverPath, options=options_edge)

    getScore('移动设备搜索', List[:timesMobile])
    del List[:timesEdge]
    print('移动设备搜索完成')

    #删除已搜索项目
    items_writer= open('.\searchitems.txt','w',encoding='UTF-8')
    for i in List:
        items_writer.write(i)
    items_writer.close()

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

