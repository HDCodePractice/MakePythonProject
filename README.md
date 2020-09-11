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

[给你的Windows安装Python和VScode](./第一课%20安装Python和VSCode%20(Windows).md)

## 第二课 

[使用GitHub和建立第一个机器人](https://github.com/HDCodePractice/MakePythonProject/blob/master/%E7%AC%AC%E4%BA%8C%E8%AF%BE%20%E4%BD%BF%E7%94%A8GitHub%E5%92%8C%E5%BB%BA%E7%AB%8B%E7%AC%AC%E4%B8%80%E4%B8%AA%E6%9C%BA%E5%99%A8%E4%BA%BA.md)

## 第三课

[简单的时运机器人](https://github.com/HDCodePractice/MakePythonProject/blob/master/%E7%AC%AC%E4%B8%89%E8%AF%BE%20%E7%AE%80%E5%8D%95%E7%9A%84%E6%97%B6%E8%BF%90%E6%9C%BA%E5%99%A8%E4%BA%BA.md)

## 第四课

#### 简单的时运机器人(Issue)

让我们完成一个判罚机器人：

* 定义一个命令，让被处罚的人自己去执行它
* 创建一个数组，里面包括了可能扣除的XP的说明:"完了！扣除1000XP你要降级啦！"、"你太幸运啦！不用扣除XP！"、"普普通通，500XP没有了"、"让神来决定你的命运吧！"
* 利用 [Python random库](https://docs.python.org/3/library/random.html) 中的可以使用的方法来随机选择一个运气
* 如果选择到的是"让神来决定你的命运吧！"，那么再从500...1500中选择出一个数字来，再多说一句话"亲爱的%s，天神将掠夺去你的%sXP，希望你的级别平安"
* 最后再加上一句"作者 xxxx"

#### 使用两个文件

* 将与判罚相关的代码放到一个单独的文件里去
* import的使用

#### 时运机器人的第二个功能(Issue)

* 定义一个命令，让完成了一个issue的同学去执行它
* 创建一个数组，里面包括了完成一个issue的的奖励选择:"爽了！直接加90XP"、"你太幸运啦！不用加XP！"、"普普通通，只有40XP"、"让神来决定你的命运吧！"
* 如果选择到的是"让神来决定你的命运吧！"，那么再从40...120中选择出一个数字来，再多说一句话"亲爱的%s，天神奖励你%sXP，离下一级你还有多远"
* 最后再加上一句"作者 xxxx"
* 将这个功能放入另一个文件里

#### 将机器人的命令快捷显示

* 加入/start和/help
* 在BotFather用/setcommands来设置

#### 装饰一下你的机器人

* 好的名字
* 方便 @ 的 username
* 像样的头像
* 一个简单的说明

## 资源

[Telegram Bot介绍](https://core.telegram.org/bots)

[Telegram API](https://core.telegram.org/bots/api/#available-methods)

[python-telegram-bot API](https://python-telegram-bot.readthedocs.io/en/stable/)

[python-telegram-bot Github](https://github.com/python-telegram-bot/python-telegram-bot)
