# !/usr/bin/python
# -*- encoding:utf-8 -*-

# pip2 install docker-py
import docker

client = docker.Client(base_url='tcp://192.168.100.64:2375')

# 将当前 docker 及其所依赖的环境中各个组件的版本信息以一个字典的方式展现出来
for component, version in client.version().iteritems():
    print component, version

# 获取镜像信息,不指定 name 时返回所有镜像信息
print client.images(['configtool'])
# 获取容器信息
print client.containers(['configtool'])
# docker info命令的那些输出
print client.info()
# 相当于docker start和stop指定容器
# client.start/stop(name)　　