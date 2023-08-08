import os
print(os.name)  # posix
print(os.uname())  # mac 详细系统信息, windows没有此方法
print(os.environ)  # 系统环境变量
print(os.environ.get('PATH'))  # 获取环境变量的某个值
print(os.environ.get('x', 'default'))

# 查看当前目录绝对路径
print(os.path.abspath('.'))

# 拼接路径
print(os.path.join('/user/me', 'testdir'))  # /user/me/testdir

# 创建目录 os.mkdir
# 删除路径 os.rmdir

# 分割路径
print(os.path.split('/Users/michael/testdir/file.txt'))  # ('/Users/michael/testdir', 'file.txt')

# 获取文件扩展名
print(os.path.splitext('/path/to/file.txt'))  # ('/path/to/file', '.txt')

# 文件重命名 os.rename
# 删除文件 os.remove

# os 不提供复制文件 可使用shutil模块复制文件

# 列出当前文件夹下所有文件夹
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 列出所有.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

allFileList = []
def findAllNameLikeFile(filename, dir = '.'):
    dirList = [x for x in os.listdir(dir) if os.path.isdir(os.path.join(dir, x))]
    fileList = [x for x in os.listdir(dir) if os.path.isfile(os.path.join(dir, x)) and filename in os.path.split(x)[1]]
    allFileList.extend(fileList)
    # print(dir,'=====dir======', dirList, fileList)
    # print([x for x in os.listdir(dir) if os.path.isfile(x)])

    if len(dirList) == 0:
        return
    for curDir in dirList:
        nextDir = ''
        if(dir == '.'):
            nextDir = os.path.join(os.path.abspath('.'), curDir)
        else:
            nextDir = os.path.join(dir, curDir)

        findAllNameLikeFile(filename, nextDir)
    # print(dirList, fileList)

findAllNameLikeFile('li')
print(allFileList, 'allFileList')