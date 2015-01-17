## install aria2 in centOS 6.5

aria2 是另一款 Linux 下轻量级的多线程下载工具，支持Http/Https、Ftp、BitTorrent、Metalink协议。它比 axel 优秀的地方在于：
完全支持 BitTorrent 协议，同时可以作为 BitTorrent 客户端来下载种子文件；支持 Metalink 协议；远程控制（通过 web 端）下载进程。
官网地址：http://aria2.sourceforge.net ，首页有简略使用教程（Usage Examples），更多高阶教程围观官网 Manual 。


本文介绍的是如何在 CentOS 中安装 aria2 ，以及出现错误的一些记录。
同样的，默认 repo 里没有 aria2 ，因此需要到 http://pkgs.repoforge.org/aria2/ 去下载 rpm 包安装即可。


### 1. 安装依赖包
在安装过程有可能会出现缺少 libnettle.so.4 的错误提示。
因此需要先到 http://pkgs.repoforge.org/nettle/ 去下载安装 nettle 即可。

CentOS 6.x 64 位下安装

wget -c http://pkgs.repoforge.org/nettle/nettle-2.2-1.el6.rf.x86_64.rpm
wget -c http://pkgs.repoforge.org/nettle/nettle-devel-2.2-1.el6.rf.x86_64.rpm
rpm -ivh nettle-2.2-1.el6.rf.x86_64.rpm
rpm -ivh nettle-devel-2.2-1.el6.rf.x86_64.rpm

### 2. 安装 aria2 到 CentOS 6.x 64位

CentOS 6.x 64 位下安装

wget -c http://pkgs.repoforge.org/aria2/aria2-1.16.4-1.el6.rf.x86_64.rpm
rpm -ivh aria2-1.16.4-1.el6.rf.x86_64.rpm
