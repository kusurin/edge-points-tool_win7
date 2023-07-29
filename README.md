###### 参考

https://blog.csdn.net/weixin_39379132/article/details/129004864

在此基础上进行了部分代码重构，避免了随机数重复的可能，并一次性执行PC和手机端的积分获取

###### 文件介绍
- setCookies.py文件用于获取用户的cookies信息
- execute.py文件用于执行刷取积分操作
- run.py文件用于一键执行整个过程，简化操作
- 下载必要文件.html文件用于下载Python和Edge Driver
- 初始化环境.bat文件用于下载项目后的环境初始化（请先下载Python）
- 点我运行.bat文件用于简单的执行，只需要双击即可

###### 初始化环境（请将项目放在全英文路径，否则可能会有奇怪的错误）
1. 双击“下载必要文件.html”，根据提示信息下载文件
2. 将下载的Edge Driver放入本项目文件夹中，安装下载好的Python安装包，请注意，一定要勾选 Add Python 3.x to PATH，否则脚本将无法正常运行
3. 双击“初始化环境.bat”文件（只需要执行一次）

###### 需要自己修改的地方

1. execute.py文件中

   - timesPC和timesMobile需根据自己的上限进行调整，值为上限除以3（建议稍微多一点）

###### 运行方法（！！！请先初始化环境！！！）

- 双击“点我运行.bat”文件运行

###### 可能出现的问题

1. 在使用脚本时，不能使用代理，会导致运行错误