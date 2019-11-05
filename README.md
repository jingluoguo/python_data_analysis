# python_data_analysis
一些python对数据处理的小脚本，外加不错的一些小工具

- 修改单独文件上传命令 
git pull 仓库名 master
git rm -r --cached 文件夹
git commit -m ""
git push -u origin master

#### handle_fasta

1. 区分DP和OP，并且生成不同的文件
2. 根据要求截取下标左右两边n个数据，并分配到文件下
3. 判断是否够n个数据，然后进行处理
4. 702ge.fasta为测试数据

#### handle_positive_negative

1. 根据shell提供的文件名来执行操作
2. 筛选positive和negative并划分n份
3. 顺序区分训练集和测试集
4. 缓存每次训练集和测试集，并自动清除
5. 存储训练完结果，并放在result_file.txt

#### 使用DBeaver操作postSQL.md

一个不错的管理服务器端postSQL数据库的tool的介绍
