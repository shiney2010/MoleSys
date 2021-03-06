MoleSys
=======

基于Mole的一个企业级web应用的架子


概述
=====
MoleSys 是一个基础架子示例，结构清晰，没有做过渡封装，包含了python web开发可能涉及的主要模块，特别适合快速
地建立一个后台数据及报表查看管理系统。

特性
======
1. 结构简单清晰，轻量级，便于源码阅读改造
2. 基于[Mole](https://github.com/JoneXiong/Mole)，加入了session模块，并提供了装饰器便于简单的会话验证
3. 包含一个快捷的Grid表报数据查询和导出模型系统，后台数据源的构建方便灵活
4. 系统包含sql语句的统一管理模块，用xml文件组织系统所有sql语句
5. 整合DBUtils数据库连接池模块，为系统提供高效稳定的数据层接口
6. 系统前端UI基于DWZ，为三层菜单结构，后端可以很方便直观地进行配置
7. 提供了form模块方便用面向对象的方式构建前端表单(主要引自Django 相关部分源码)

使用
======
python server.py

界面演示
======

主界面
![main](https://github.com/JoneXiong/MoleSys/raw/master/apps/media/show/main.jpg)

报表界面
![report](https://github.com/JoneXiong/MoleSys/raw/master/apps/media/show/report.jpg)

选人界面
![select](https://github.com/JoneXiong/MoleSys/raw/master/apps/media/show/select.jpg)

操作界面
![op](https://github.com/JoneXiong/MoleSys/raw/master/apps/media/show/op.jpg)

Crud示例
![op](https://github.com/JoneXiong/MoleSys/raw/master/apps/media/show/crud.jpg)

计划
======
1. 加入轻量级的ORM模块支持
2. 基于ORM模型建立Crud，这样便于自动生成后台管理功能
3. 基于ORM模型建立自动的RESTful接口
