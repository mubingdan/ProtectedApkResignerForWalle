#!/usr/bin/python  
#-*-coding:utf-8-*-

#keystore信息
#Windows 下路径分割线请注意使用\\转义
keystorePath = ""
keyAlias = ""
keystorePassword = ""
keyPassword = ""

#加固后的源文件名（未重签名）
protectedSourceApkName = "app-qa-release-3.3.20.6606.apk"
#加固后的源文件所在文件夹路径(...path),注意结尾不要带分隔符，默认在此文件夹根目录
protectedSourceApkDirPath = ""
#渠道包输出路径，默认在此文件夹Channels目录下
channelsOutputFilePath = ""
#渠道名配置文件路径，默认在此文件夹根目录
channelFilePath = ""
#Android SDK buidtools path , please use above 25.0+
sdkBuildToolPath = r"C:\Users\mubingdan\AppData\Local\Android\Sdk\build-tools\27.0.3"