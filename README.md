###### 需要自己修改的地方

1st文件中

- driver = webdriver.Edge('C:/Users/Windy/EdgeDriver')，路径改为Edge Driver路径

2nd文件中

- driver = webdriver.Edge('C:/Users/Windy/EdgeDriver/msedgedriver', options=options)，路径改为Edge Driver路径



###### 运行方法

- 首先运行1st文件（cookies存储）
- 然后运行2nd文件（PC端积分获取）
- 然后将以下语句解开注释后运行（移动端积分获取）

mobile_emulation = {'deviceName': 'Pixel 5'}  

options.add_experimental_option("mobileEmulation", mobile_emulation)    