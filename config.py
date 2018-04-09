#!/usr/bin/python  
#-*-coding:utf-8-*-
import os

# 获取当前目录
basePath = os.getcwd()
# 签名相关配置信息文件路径
signingFilePath = basePath + '/signing.properties'

if os.path.exists(signingFilePath):
    signingFile = open(signingFilePath, 'r')
    lines = signingFile.readlines()
    for line in lines:
        if line.__contains__('STORE_FILE'):
            storePath = line.split('=')[1]
            print (storePath)
        if line.__contains__('STORE_PASSWORD'):
            storePassword = line.split('=')[1]
            print (storePassword)
        if line.__contains__('KEY_ALIAS'):
            alias = line.split('=')[1]
            print (alias)
        if line.__contains__('KEY_PASSWORD'):
            password = line.split('=')[1]
            print (password)
else:
    print ('Can not found signing.properties file')

#keystore信息
#Windows 下路径分割线请注意使用\\转义
keystorePath = storePath
keyAlias = alias
keystorePassword = storePassword
keyPassword = password

listFile = os.listdir(basePath)
for file in listFile:
     # 拼接文件路径
    filePath = basePath + '/' + file
    if os.path.isfile(filePath): # 判断是为文件
        extension = os.path.splitext(filePath)[1][1:]
        if extension.strip() and extension in 'apk':
            apkName = os.path.basename(filePath)
            # 是文件打印
            print(apkName)

#加固后的源文件名（未重签名）
protectedSourceApkName = apkName
#加固后的源文件所在文件夹路径(...path),注意结尾不要带分隔符，默认在此文件夹根目录
protectedSourceApkDirPath = ""
#渠道包输出路径，默认在此文件夹Channels目录下
channelsOutputFilePath = ""
#渠道名配置文件路径，默认在此文件夹根目录
channelFilePath = ""
#Android SDK buidtools path , please use above 25.0+
sdkBuildToolPath = r"C:\Users\mubingdan\AppData\Local\Android\Sdk\build-tools\27.0.3"