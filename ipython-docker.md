1. 安装ipython
yum install ipython
2. 键入 ipython 就进入 ipython 的 shell 了
* 实例化client
* 输入client.然后按tab键要求补全的话，就会显示出所有client实例可以调用的方法和属性
* 对于一个属性比如client.containers,后面输入？再按回车，就可以看到这个属性相关的一些说明和用法
``` bash
[root@nodeb4 ~]# ipython
...
...
In [1]: import docker

In [2]: client = docker.from_env()

In [3]: client.
client.api         client.containers  client.from_env    client.login       client.ping        client.services    client.volumes
client.close       client.df          client.images      client.networks    client.plugins     client.swarm
client.configs     client.events      client.info        client.nodes       client.secrets     client.version

In [3]: client.containers?
Type:        property
String form: <property object at 0x3013260>
Docstring:
An object for managing containers on the server. See the
:doc:`containers documentation <containers>` for full details.
```