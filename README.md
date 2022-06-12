# ToAZK使用方法
* 程序核心来自Kindle Previewer3的azkcreator（azkcreator.exe）程序  

* 语法（注意空格） ：azkcreator --source 源文件绝对路径（带文件名和后缀名） --target 目标路径

* .azk实际上是一个zip的压缩包，kindle peieviewer3调用azkcreator转换mobi和azw3格式成散文件并压缩为.azk文件，并且azkcreator程序在转换格式时会删除书名和作者，用python代码中将书名补回（补回作者比较麻烦就暂时没弄）再使用python调用winrar将转换后并修改完书名的文件打包为zip并重命名后缀名为azk  

* azkcreator在windows上生成的azk文件没有目录，我查一下外网，挺多人遇到这个问题，目前没找到解决办法


## 1、安装Java运行环境（jdk）并配置环境变量
* MAC  
     下载链接 https://download.oracle.com/java/18/latest/jdk-18_macos-x64_bin.dmg  
     mac好像是自动配置好环境变量了，我忘记了，各位自己在终端（Terminal）试一下输入java有没有反应，没有的话自己百度一下吧
* Windlws  
     下载链接 https://download.oracle.com/java/18/latest/jdk-18_windows-x64_bin.exe  
     环境变量 https://jingyan.baidu.com/article/7c6fb4281df557c1652c9058.html

## 2、安装Kindle Previewer 3  
* 下载链接  
    https://www.amazon.com/Kindle-Previewer/b?node=21381691011
* Mac  
    从 /Applications/Kindle Previewer 3.app/Contents/MacOS 文件夹下复制 azkcreator 到 /usr/local/bin 文件夹下
* Windows  
    找到Kindle Previewer 3安装目录下的Kindle Previewer 3\lib文件夹，复制该文件夹路径，打开右键打开电脑属性——高级系统设置——环境变量——下方系统变量，编辑path——新建，将刚刚复制的路径粘贴进去，确定保存
## 3、安装winrar压缩软件
* 下载链接  
    https://www.rarlab.com/download.htm
* Mac  
    解压压缩包后复制 rar 和 unrar 到 /usr/local/bin 文件夹下（方法：Finder——前往——前往文件夹——/usr/local/bin）
* Windows  
    安装winrar后找将安装目录添加到环境变量，参考上方
## 4、安装Python 
* Mac  
    https://www.python.org/ftp/python/3.10.5/python-3.10.5-macos11.pkg
* Windows  
    开始安装时，打开安装包，下方勾选 Add Python 3.10 to PATH
    下载链接 https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe

## 5、转换格式
* Mac  
    ToAZKForMac.py复制到mobi或azw3所在目录，假设在桌面一个叫book文件夹
    打开终端（Terminal），输入：cd /Users/你的用户名/Desktop/book
    输入python3 ToAZKForMac.py
    转换好的最终会保存在当前目录的zip文件夹内
* Windows  
    ToAZKForMac.py复制到mobi或azw3所在目录，假设在桌面一个叫book文件夹
    打开cmd，输入cd C:\Users\你的用户名\Desktop\book
    输入python ToAZKForMac.py
    转换好的最终会保存在当前目录的zip文件夹内