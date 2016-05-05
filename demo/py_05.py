# -*- coding: utf-8 -*-
# 文件处理
import codecs
import os
import sys
from setuptools.compat import unicode

# 文件打开 open(name, mode, buf)
#   读写方式打开：r+ / w+  追加和读写方式打开：a+
#   二进制方式打开：加后缀'b'

try:
    f = open('D:/demo/123.txt', 'a+')
    # print(f)
    # print(type(f))
except IOError as error:
    f.close()

# 文件读取方式：
#   read([size])：读取size个字节，默认读取全部字节
#   readline([size])：读取一行
#   readlines([size])：读取由默认缓冲大小的字节数所组成的行，返回每一行所组成的列表
#         size : io.DEFAULT_BUFFER_SIZE
#   iter：使用迭代器读取文件
try:
    f2 = open('D:/demo/123.txt', 'r+')
    # print(help(f2.read))
    # print(f2.read())

    # print(help(f2.readline))
    # print(f2.readline(9))
    # print(f2.readline(9))
    # print(f2.readline(9))

    # print(f2.readlines())
    # print(help(f2.readlines))

    iter_f = iter(f2)
    s = ''
    for line in iter_f:
        s += line
    print(s)
except IOError as error:
    f2.close()

# 文件写入方式：
#   write(str)：将字符串写入文件
#   writelines(sequence_of_strings)：写多行到文件
try:
    f3 = open('D:/demo/123.txt', 'a+')
    # print(help(f3.write))
    # length = f3.write('\nhahaha...')
    # print(length)

    # f3.writelines('''
    #     xixi...
    #     hehe...
    #     haha...
    # ''')
    # f3.writelines(['1', '2', '3'])
    # f3.flush()  # 刷新缓冲
except IOError as error:
    f3.close()

# 文件的游标指针：seek(offset, whence) offset：偏移量，whence：偏移相对位置
#       os.SEEK_SET、os.SEEK_CUR、os.SEEK_END
try:
    f4 = open('D:/demo/123.txt', 'r+')
    f4.seek(0, os.SEEK_END)
    # print(f4.tell())  # 当前指针位置
    # f4.write('world')
except IOError as error:
    f4.close()

try:
    # 文件属性
    f5 = open('D:/demo/123.txt', 'a+')
    # print(f5.fileno())  # 文件描述符
    # print(f5.mode)  # 文件打开权限
    # print(f5.encoding)  # 文件编码格式

    # 标准文件：sys.stdin、sys.stdout、sys.stderr
    # print(sys.stdin.mode)
    # print(sys.stdout.mode)
    # sys.stdout.write('Error：')  # 只接受字符型参数
    # sys.stderr.write('Error：')

    # 文件的命令行参数：sys.argv(字符串组成的列表)
    print(len(sys.argv))
    for arg in sys.argv:
        print(arg)

    # 文件编码
    s = unicode.encode('杨萧', 'utf-8')
    print(s)

    # f5.write('杨萧')
except IOError as error:
    f5.close()

# codecs模块提供方法，创建指定编码格式的文本
#   open(fname, mode, encoding, errors, buffering)
try:
    f6 = codecs.open('D:/demo/demo.txt', 'w', 'utf-8')
    # print(help(codecs.open))
    print(f6.encoding)
    # f6.write('杨萧')

except IOError as error:
    f6.close()

# 使用 os 模块操作文件
#   打开文件：os.open(filename, flag[, mode]) flag：打开文件方式
#        os.O_CREAT、os.O_RDONLY、os.O_WRONLY ．．．
#   os.read(fd, buffersize) fd：文件描述符
#   os.write(fd, byte_object)
#   文件指针操作：os.lseek(fd, pos, how)
#   os.close(fd)
try:
    fd = os.open('D:/demo/aaa.txt', os.O_CREAT)
    # os.write(fd, unicode.encode('杨萧', 'utf-8'))
    # print(os.lseek(fd, 0, os.SEEK_END))
    # print(os.read(fd, 1024))

    # print(os.access('D:/demo/123.txt', os.F_OK))
    # os.remove('D:/demo/demo.txt')
    # print(os.listdir('D:/demo'))
    # mkdir(path[, mode])、mkdirs(path[, mode])
    # removedirs(path)、rmdir(path)(目录必须为空目录)

    # os.path 模块方法
    # print(os.path.exists('D:/demo/123.txt'))
    # print(os.path.dirname('D:/demo/123.txt'))  # 返回路径的目录
    # print(os.path.basename('D:/demo/123.txt'))  # 返回路径的文件名
    # print(os.path.getsize(fd))  # 返回文件大小

except IOError as error:
    os.close(fd)
