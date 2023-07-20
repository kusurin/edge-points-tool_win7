###### 参考

https://blog.csdn.net/weixin_39379132/article/details/129004864

在此基础上进行了部分代码重构，避免了随机数重复的可能，并一次性执行PC和手机端的积分获取



###### 需要自己修改的地方

setCookies.py文件中

- driver = webdriver.Edge('C:/Users/Windy/EdgeDriver')，路径改为自己的Edge Driver路径

execute.py文件中

- driver = webdriver.Edge('C:/Users/Windy/EdgeDriver/msedgedriver', options=options)，路径改为自己的Edge Driver路径
- timesPC和timesMobile需根据自己的上限进行调整，值为上限除以3


###### 运行方法

- 运行run.py文件
