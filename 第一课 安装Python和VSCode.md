## 第一课 给你的MacOS安装Python和VSCode

### 安装brew

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

### 安装Python

```
brew install python
```

### 安装VSCode

```
brew cask install visual-studio-code
```

安装后运行，完成以下工作：

.在home目录下建立一个`work`的目录
.运行 `code work`
.新建一个 `hello.py` 的文件并保存
.安装python相关的两个扩展

### 安装GitHub Desktop

```
brew cask install github
```

运行Github Desktop并通过网站认证登录。

### Python Hello World

然后我们来试试Python HelloWorld：

[![第一次运行Python](https://img.youtube.com/vi/Hb9YxknWvhY/0.jpg)](https://www.youtube.com/watch?v=Hb9YxknWvhY)

然后我们在VSCode里新建一个hello.py的文件(注意VSCode会提示你安装两个Python插件的)

里面写入

```
name = "noah"
name2 = "sicheng"
print("hello %s and %s"  % (name,name2) )
```

保存后，点右上角的run来试试。
