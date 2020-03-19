# DjangoBlog

🌍
*[English](/docs/README-en.md) ∙ [简体中文](README.md)*

基于`python3.8`和`Django2.1.15`的博客。基于[原版](https://github.com/liangliangyy/DjangoBlog)修改。


[![Build Status](https://travis-ci.org/liangliangyy/DjangoBlog.svg?branch=master)](https://travis-ci.org/liangliangyy/DjangoBlog) [![codecov](https://codecov.io/gh/liangliangyy/DjangoBlog/branch/master/graph/badge.svg)](https://codecov.io/gh/liangliangyy/DjangoBlog) [![Requirements Status](https://requires.io/github/liangliangyy/DjangoBlog/requirements.svg?branch=master)](https://requires.io/github/liangliangyy/DjangoBlog/requirements/?branch=master)  [![license](https://img.shields.io/github/license/liangliangyy/djangoblog.svg)]()  

## 安装
使用Docker部署请移步 [快速部署DjangoBlog](https://github.com/kentio/ondjblog)

## 修改详情
- 添加Dockerfile
- 考虑兼容性，降级至`Django2.1.15`
- 优化settgins配置
- 写文章自动保存作者，允许作者`author`字段为空
- 初始化migrations文件
- 允许分类`category`字段为空
- 重构项目目录结构，App全部移至`apps`目录
- 优化中间件`OnlineMiddleware`逻辑，规范中间件使用

有任何问题欢迎提Issue。

## 原版功能：
- 文章，页面，分类目录，标签的添加，删除，编辑等。文章及页面支持`Markdown`，支持代码高亮。
- 支持文章全文搜索。
- 完整的评论功能，包括发表回复评论，以及评论的邮件提醒，支持`Markdown`。
- 侧边栏功能，最新文章，最多阅读，标签云等。
- 支持Oauth登陆，现已有Google,GitHub,facebook,微博,QQ登录。
- 支持`Memcache`缓存，支持缓存自动刷新。
- 简单的SEO功能，新建文章等会自动通知Google和百度。
- 集成了简单的图床功能。
- 集成`django-compressor`，自动压缩`css`，`js`。
- 网站异常邮件提醒，若有未捕捉到的异常会自动发送提醒邮件。
- 集成了微信公众号功能，现在可以使用微信公众号来管理你的vps了。
