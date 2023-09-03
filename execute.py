import json
import random
from selenium import webdriver
from selenium.webdriver.edge.options import Options

import time

import win32api
import win32con


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
    poems = [
    '白日依山尽，黄河入海流。',
    '静夜思',
    '床前明月光，疑是地上霜。',
    '天净沙，秋思',
    '夕阳无限好，只是近黄昏。',
    '明月几时有，把酒问青天。',
    '花间一壶酒，独酌无相亲。',
    '红豆生南国，春来发几枝。',
    '山有木兮木有枝，心悦君兮君不知。',
    '但愿人长久，千里共婵娟。',
    # 添加更多古诗语句...
    '千山鸟飞绝，万径人踪灭。',
    '日照香炉生紫烟，遥看瀑布挂前川。',
    '人生若只如初见，何事秋风悲画扇。',
    '白日依山尽，黄河入海流。',
    '我自横刀向天笑，去留肝胆两昆仑。',
    '青山遮不住，毕竟东流去。',
    '问君能有几多愁，恰似一江春水向东流。',
    '无边落木萧萧下，不尽长江滚滚来。',
    '人生自古谁无死，留取丹心照汗青。',
    '明月几时有，把酒问青天。',
    '野火烧不尽，春风吹又生。',
    '举杯邀明月，对影成三人。',
    '欲穷千里目，更上一层楼。',
    '长风破浪会有时，直挂云帆济沧海。',
    '商女不知亡国恨，隔江犹唱后庭花。',
    '无可奈何花落去，似曾相识燕归来。',
    '黄河之水天上来，奔流到海不复回。',
    '生当作人杰，死亦为鬼雄。',
    '寄蜉蝣于天地，渺沧海之一粟。',
    '会当凌绝顶，一览众山小。',
    '海上生明月，天涯共此时。',
    '不畏浮云遮望眼，只缘身在最高层。',
    '欲把西湖比西子，淡妆浓抹总相宜。',
    '采菊东篱下，悠然见南山。',
    '人生自古谁无死，留取丹心照汗青。',
    '两情若是久长时，又岂在朝朝暮暮。',
    '人生自古谁无死，留取丹心照汗青。',
    '抽刀断水水更流，举杯销愁愁更愁。',
    '两情若是久长时，又岂在朝朝暮暮。',
    '生活不是等待暴风雨过去，而是要学会在雨中跳舞。',
    '前事不忘，后事之师。',
    '死亡教会我爱生命。',
    '人生的长河只有一次，我们要学会奔腾。',
    '秋天不是为了秋天而来，而是为了继续天长地久。',
    '只有不断奋斗，才能活出自己。',
    '生活没有翻不过去的坎，只要你有勇气。',
    '你是最幸福的人，一直要做最幸福的人。',
    '青春不是年华，而是心境。',
    '不论你在什么时候开始，重要的是开始之后不要停止。',
    '人不是应该活得轰轰烈烈，而是应该活得有滋有味。',
    '解决问题的最好办法并不是为问题找一个答案，而是为问题找一个立场。',
    '生活就像咖啡，苦中有味。',
    '创造属于自己的精彩，别活在别人的指责之中。',
    '自信不是众人的夸赞，而是自己微不可察的力量。',
    '只有自己的脚步声，才是最响亮的。',
    '疾风知劲草，板荡识诚臣。',
    '只要心情是晴朗的，每天都是蓝天。',
    '心若没有栖息的地方，到哪里都是流浪。',
    '宁可抱憾而死，不愿过着畏首畏尾的生活。',
    '生活就像一杯咖啡，苦、甜、酸、辣都是味道。',
    '你的未来是用今天创造的。',
    '路是走出来的，而不是空想出来的。',
    '生活终将向前，义无反顾。',
    '一切不忠于生活的事物，都会互相抵消。',
    '不要绝望，绝望是一种常态。',
    '人不是石头，不会无动于衷。',
    '要努力，更要保持微笑。',
    '梦想是现实的前奏。',
    '没有付出，就没有收获。',
    '方向再远，也比不上一步的脚印。',
    '人生不是一场功夫，而是一场修行。',
    '不管遇到什么事情，都不要急于下判论。',
    '生活没有退路，只有进路。',
    '不要让昨天的失去，毁了今天的期待。',
    '不要等待机会，而要创造机会。',
    '做一个有思想有情感的人，这才是生活。',
    '凡事都要加油，坚持不懈。',
    '生命就是不断的学习和进步。',
    '人生就是一种选择，没有对错。',
    '只有不断战胜自己，才能赢得未来。',
    '生活就像咖啡，苦中有味。',
    '只有走出来的路，才是自己的路。',
    '没有过不去的坎，只有不想过去的障碍。',
    '漫天飞舞的，不是花瓣，而是心情。',
    '人生没有终点，只有转折。',
    '你可以在哪里跌倒，就能在哪里站起来。',
    '活在当下，未来才会有意义。',
    '放慢脚步，路上的风景才会更美。',
    '生活不仅有快乐，也会有压力。',
    ]
    random_poem = random.choice(poems)
    OpenUrl('https://cn.bing.com/search?q=' + str(random_poem)+'是什么含义')


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
    List = random.sample(range(1, 10000), timesSum)

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
    print('Microsoft Edge奖励完成')

    # 电脑搜索
    driver = webdriver.Edge(driverPath, options=options)
    getScore('电脑搜索', List[timesEdge:timesEdge + timesPC])
    print('电脑搜索完成')

    # 移动设备搜索
    mobile_emulation = {'deviceName': 'Galaxy S4'}  # 添加移动设备搜索
    options_edge.add_argument("--auto-open-devtools-for-tabs") #打开F12
    driver = webdriver.Edge(driverPath, options=options_edge) #F12不能无窗口运行
    time.sleep(5)
    OpenUrl('https://cn.bing.com')
    win32api.keybd_event(16, 0, 0, 0)
    win32api.keybd_event(17, 0, 0, 0)
    win32api.keybd_event(77, 0, 0, 0)
    win32api.keybd_event(77, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(16, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    getScore('移动设备搜索', List[timesEdge + timesPC:])
    print('移动设备搜索完成')

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

