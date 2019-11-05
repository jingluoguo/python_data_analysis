#### 一、 下载并安装DBeaver

1. 从<https://dbeaver.io/download/>页面左侧找到Windows 64 bit的安装包，下载。

2. 安装时选择“Anyone who uses this computer”，会自动使用管理员权限，安装的组件选择默认即可，其他设置根据情况选择。

3. 确保服务器的postgresql数据库已经运行，打开DBeaver，出现如下图界面：

    

   [![KzHVN8.md.jpg](https://s2.ax1x.com/2019/11/05/KzHVN8.md.jpg)](https://imgchr.com/i/KzHVN8)

4. 找到PostgreSQL选项，选中然后下一步，输入对应的主机、用户、密码等信息，其他可以使用默认

#### 二、 修改postSQL远程连接

1. 在/etc/postgresql/10/main/

[![KzHucj.md.jpg](https://s2.ax1x.com/2019/11/05/KzHucj.md.jpg)](https://imgchr.com/i/KzHucj) 

2. 在/etc/postgresql/10/main/pg_hba.conf修改IPv4下面，添加一行

[![KzHQun.md.jpg](https://s2.ax1x.com/2019/11/05/KzHQun.md.jpg)](https://imgchr.com/i/KzHQun) 

