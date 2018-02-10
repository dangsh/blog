blog
===========================

## 环境依赖
python 3.6.2
MySQL 5.7

## 部署步骤
1. 安装python3.6.2
2. 通过pip安装 flask , Jinja2 , pymysql 模块
3. 修改linkdb.py文件config中的数据库配置
4. 创建对应的数据库，及表
5. 在blog目录下 使用命令 python headlines.py 运行
6. 在浏览器输入localhost：5678 访问网页


## 目录结构描述 <br/>
├── static                      // js,css等静态资源 <br/>
├── templates                   // 放置html模板 <br/>
├── headlines.py                // 项目主文件 <br/>
├── linkdb.py                   // 用于连接数据库及进行数据库操作 <br/>
└── README.md                   // 帮助文档 <br/>

## V0.0.1 版本内容
1. 进入主界面 
2. 删除空格及相关功能 

## V1.0.0 版本内容更新 2018.1.22    
1. 登录功能       
2. 文章展示         
3. 文章删除	        
4. 字符替换功能    

## V2.0.0 版本 2018.2.2
重新设计了界面，对界面进行了重构 <br/>
删除了一些不必要的功能 <br/>
1.删除了音乐搜索功能 <br/>
2.删除了今日头条功能 <br/>
3.本次更新了所有的static文件 <br/>
4.增加了颜色转换的功能<br/>
5.增加了留言板的功能<br/>
6.美化了404界面<br/>
7.增加了注册，忘记密码的界面<br/>
8.完成了index界面的分页功能 2018-2-8<br/>
9.增加了HTTP代理功能，通过IPProxyPool获取免费的代理IP，<br/>
  提供给用户使用。并且提供了API接口 2018-2-10 <br/>
