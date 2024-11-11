# Flask App Template

**An complete Flask application template, with useful plugins.**

Use this Flask app to initiate your project with less work. In this application  template you will find the following plugins already configured:

* **Flask-Login** - Flask-Login provides user session management for Flask.
* **Flask-Bootstrap** - Ready-to-use Twitter-bootstrap for use in Flask.
* **Flask-Uploads** - Flask-Uploads allows your application to flexibly and efficiently handle file uploading and serving the uploaded files.
* **Flask-Cache** - Adds cache support to your Flask application.
* **Flask-Admin** - Flask extension module that provides an admin interface
* **Flask-Flatpages** - Provides flat static pages to a Flask application, based on text files as opposed to a relational database.
* **Flask-Gravatar** - Small extension for Flask to make using Gravatar easy.
* **Flask-Mail** - Makes sending mails from Flask applications very easy and has also support for unittesting.
* **Flask-Restless** - Flask-Restless provides simple generation of ReSTful APIs for database models defined using Flask-SQLAlchemy.
* **Flask-SQLAlchemy** - Adds SQLAlchemy support to Flask. Quick and easy.
* **Flask-PyMongo** - Add PyMongo Support MongoDB.
* **Flask-Themes** - Flask-Themes makes it easy for your application to support a wide range of appearances.
* **Flask-WTF** - Simple integration of Flask and WTForms, including CSRF, file upload, and reCAPTCHA.

## Requirements

Python 3.8.5+, pipenv

## Instalation

First, clone this repository.

    $ git clone http://github.com/berlotto/flask-app-template
    $ cd flask-app-template

After, install all necessary to run:

    $ pipenv install

Than, run the application:

	$ pipenv run python run.py

To see your application, access this url in your browser: 

	http://localhost:5000

All configuration is in: `configuration.py`



/yourapp
    /app
        /api             # 处理所有API相关的操作
            __init__.py
            views.py
            errors.py
        /auth            # 认证模块
            __init__.py
            views.py
            models.py
        /main            # 主应用模块
            __init__.py
            views.py
            models.py
            forms.py
        /static          # 静态文件
        /templates       # Jinja2模板文件
        /commands        # 自定义命令行命令
        /data            # 数据处理模块
        /services        # 业务逻辑层
        /utils           # 工具模块
        /tests           # 测试模块
        __init__.py      # 创建和配置应用
    /migrations         # 数据库迁移
    /venv               # 虚拟环境
    config.py           # 配置文件
    run.py              # 启动文件
    requirements.txt    # 依赖文件
