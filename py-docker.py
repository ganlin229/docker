# !/usr/bin/python
# -*- encoding:utf-8 -*-

# pip2 install docker-py
import docker

client = docker.Client(base_url='tcp://192.168.100.64:2375')

# 将当前 docker 及其所依赖的环境中各个组件的版本信息以一个字典的方式展现出来
# for component, version in client.version().iteritems():
#     print component, version

# 获取镜像信息,不指定 name 时返回所有镜像信息
# images = client.images()
# for image in images:
#     print image
    # print str(image["Id"])[7:19]
    # print image["RepoTags"][0]
# 获取容器信息
containers = client.containers(all=True)
for container in containers:
    print container
    # print container["Names"][0].encode('utf-8')[1:], container["State"]
    # print container["Ports"][0]["PrivatePort"]
# docker info命令的那些输出
# print client.info()
# 相当于docker start和stop指定容器
# client.stop("kafka1")
# 移除容器
# client.remove_container("kafka2")
# 拉取镜像
# image = client.pull('hello-world:latest')
# print image
# 移除镜像
# client.remove_image("hello-world:latest")
# 创建容器
# result = client.create_container(image="hello-world:latest", name="hello-world")
# print result
