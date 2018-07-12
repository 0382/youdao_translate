### youdao_translate
爬虫实现有道翻译

使用爬虫的办法使用有道翻译。有道翻译的URL意外的很简单：
```python3
http://dict.youdao.com/w/{0}/#keyfrom=dict2.top
```
只要填入英文单词就可以实现翻译了。

另外介绍一下一个小窍门。对于python，变成exe还是比较困难的。使用pyinstaller时一个好办法，不过有时候速度还不如直接运训python文件快。那么这个有道翻译怎么使用呢？我的办法是建一个专门的文件夹，把它添加到环境路径里面去。再这里面写一个批处理文件，比如对于这个程序，我将写一个translate.cmd，文件内容如下：
```batch
@echo off
python you_path_to\translate.py %*
```
其中`%*`会将你的输入参数原封不动的复制下来。而这个文件是在环境里面的，只要在cmd下面输入：
```batch
translate words
```
你将得到以下输出：
```batch
pronounce:
英 [wɜːdz]
美 [wɝdz]
mean:
n. [计] 字（word的复数）；话语；言语
v. 用言语表达（word的三单形式）
```