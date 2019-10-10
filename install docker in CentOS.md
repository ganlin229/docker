1. 使用 sudo 或 root 权限的用户登入终端
2. 确保 yum 是最新的
``` bash
$ yum update
```
3. 添加 yum 仓库
``` bash
tee /etc/yum.repos.d/docker.repo <<-'EOF'
[dockerrepo]
name=Docker Repository
baseurl=https://yum.dockerproject.org/repo/main/centos/$releasever/
enabled=1
gpgcheck=1
gpgkey=https://yum.dockerproject.org/gpg
EOF
```
4. 安装 docker
``` bash
$ yum install -y docker-engine
```
5. 安装成功后，使用 docker version 命令查看是否安装成功
``` bash
[root@nodeb4 ~]# docker version
Client:
 Version:      17.05.0-ce
 API version:  1.29
 Go version:   go1.7.5
 Git commit:   89658be
 Built:        Thu May  4 22:06:25 2017
 OS/Arch:      linux/amd64
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```
6. 启动 docker
``` bash
$ systemctl start docker.service
```
7. 验证安装是否成功(有 client 和 service 两部分表示 docker 安装启动都成功了)
``` bash
[root@nodeb4 ~]# docker version
Client:
 Version:      17.05.0-ce
 API version:  1.29
 Go version:   go1.7.5
 Git commit:   89658be
 Built:        Thu May  4 22:06:25 2017
 OS/Arch:      linux/amd64

Server:
 Version:      17.05.0-ce
 API version:  1.29 (minimum version 1.12)
 Go version:   go1.7.5
 Git commit:   89658be
 Built:        Thu May  4 22:06:25 2017
 OS/Arch:      linux/amd64
 Experimental: false
 ```
8. 设置 server 开机自启动
``` bash
 [root@nodeb4 ~]# systemctl enable docker
Created symlink from /etc/systemd/system/multi-user.target.wants/docker.service to /usr/lib/systemd/system/docker.service.
```
9. 开启远程连接
* 配置docker进程开启远程连接端口
``` bash
vim /usr/lib/systemd/system/docker.service
# ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
ExecStart=/usr/bin/dockerd -H tcp://0.0.0.0:2375 --containerd=/run/containerd/containerd.sock
```
* 使用以下命令重新加载配置文件和重启 docker
``` bash
systemctl daemon-reload
systemctl restart docker
```
* 然后使用以下命令查看 docker 进程的状态
``` bash
[root@nodeb4 ~]# ps -ef|grep docker
root      5563     1  3 04:07 ?        00:00:00 /usr/bin/dockerd -H tcp://0.0.0.0:2375 --containerd=/run/containerd/containerd.sock
```
可以看到已经开启了端口。