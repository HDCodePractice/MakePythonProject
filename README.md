# 创建一个你的项目

## 说明

这个项目是用于学习创建一个团体工作的项目。包括：

* 在你的MacOS上安装一个Python
* 在你的MacOS上安装一个VSCode
* 书写第一个Python HelloWorld
* 为你的项目准备一个自定义的Python
* 准备第一个Python Telegram Bot项目
* 书写每一个Hello Telegram Bot

## 第一课 

[给你的MacOS安装Python和VSCode](https://github.com/HDCodePractice/MakePythonProject/blob/master/%E7%AC%AC%E4%B8%80%E8%AF%BE%20%E5%AE%89%E8%A3%85Python%E5%92%8CVSCode.md)

## 第二课 

[使用GitHub和建立第一个机器人](https://github.com/HDCodePractice/MakePythonProject/blob/master/%E7%AC%AC%E4%BA%8C%E8%AF%BE%20%E4%BD%BF%E7%94%A8GitHub%E5%92%8C%E5%BB%BA%E7%AB%8B%E7%AC%AC%E4%B8%80%E4%B8%AA%E6%9C%BA%E5%99%A8%E4%BA%BA.md)


#### 注意

不要将自己的token、password放到Github上去，这样会让全世界都知道了你的秘密！如何解决？

* 让我们来认识一个新朋友`.gitignore`
* 将你的密码存到一个文件里去

```
import os

def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    # 读取文件内容到all_the_text
    all_the_text = open(file_path).read()
    # print type(all_the_text)
    return all_the_text

TOKEN=read_file_as_str('BOT_TOKEN')
```
* 将`BOT_TOKEN`文件加到`.gitignore`里去

#### 将你的第一个bot代码提交到Github上吧

## 资源

[Telegram Bot介绍](https://core.telegram.org/bots)

[Telegram API](https://core.telegram.org/bots/api/#available-methods)

[python-telegram-bot API](https://python-telegram-bot.readthedocs.io/en/stable/)

[python-telegram-bot Github](https://github.com/python-telegram-bot/python-telegram-bot)
