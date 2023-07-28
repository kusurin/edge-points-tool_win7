###### 参考

blog.csdn.net/weixin_39379132/article/details/129004864

在此基础上进行了部分代码重构，避免了随机数重复的可能，并一次性执行PC和手机端的积分获取

###### 文件介绍
- setCookies.py文件用于获取用户的cookies信息
- execute.py文件用于执行刷取积分操作
- run.py文件用于一键执行整个过程，简化操作

###### 需要自己修改的地方

1. setCookies.py文件中

   - driver = webdriver.Edge('C:/Users/Windy/EdgeDriver')，路径改为自己的Edge Driver路径

2. execute.py文件中

   - driver = webdriver.Edge('C:/Users/Windy/EdgeDriver/msedgedriver', options=options)，路径改为自己的Edge Driver路径
   - timesPC和timesMobile需根据自己的上限进行调整，值为上限除以3

###### 运行方法

- 运行run.py文件

###### 可能出现的问题

1. 如果不能自动登录edge，请注释掉setCookies.py文件中以下代码，并手动登录：
   - options = Options()
   - options.add_argument("--headless")  # 设置后台运行，无窗口化
2. 在使用脚本时，不能科学上网，会导致运行错误