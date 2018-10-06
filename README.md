### youdao_translate
爬虫实现有道翻译。

使用爬虫的办法使用有道翻译。有道翻译页面的URL是如下：
```python3
http://dict.youdao.com/w/{0}/#keyfrom=dict2.top
```
只要填入英文单词或者中文就可以实现翻译了。目前找到的API接口无法得到发音，所以还是直接解析页面吧，不过这样一来程序非常没有可读性，我自己都不愿意修改一些小问题了。

另外介绍一下一个小窍门。对于python，变成exe还是比较困难的。使用pyinstaller也许是一个好办法，不过有时候速度还不如直接运训python文件快。那么这个有道翻译怎么使用呢？我的办法是建一个专门的文件夹，把它添加到环境路径里面去。再这里面写一个批处理文件，比如对于这个程序，我将写一个translate.cmd，文件内容如下：
```batch
@echo off
python you_path_to/translate.py %*
```
其中`%*`会将你的输入参数原封不动的复制下来。而这个文件是在环境里面的，在cmd任何路径下面输入：
```batch
translate words
```
你将得到以下输出：
```batch
pronunciation:
英 [wɜːdz]
美 [wɝdz]
meaning:
n. [计] 字（word的复数）；话语；言语
v. 用言语表达（word的三单形式）
```
（当然其实是由于我不会写setup.py，不过这个对于一些小东西还是很管用的，不光是python的东西。）