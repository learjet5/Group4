# Group4 交大家教平台

### 需求分析

- 交大学生做家教的需求很大，缺乏一个教师和学生双向选择的平台
- 现有家教渠道对于交大学生情况不一定很实用
- 身份认证难以保证安全和正规

### 特点

- 针对交大学生做家教，面对上海地区部分学生用户辅导需求：对学科和年级进行有效划分
- 可以有效缓解资质认证相关问题，投诉环境较好
- 可以一对一交流面试
- ’**可能的话，可以针对性开展付费咨询经验等模块，有效利用交大学生的经验**‘

### 项目简介

- 本项目基于Django 3框架开发，使用SQLite数据库。前端使用bootstrap4框架，提供方便快捷的HTML开发手段。

- 无论你是中小学生，想要寻找一位适合你的家教，还是交大学子，希望能够利用业余时间做一份家教的兼职，我们的家教平台都可以给您提供精准快速的家教匹配服务。

### 使用指南

- 注册&登录：您可以根据您的身份选择注册为教员/学生，登录时则会按照账号的身份提供不同的服务。
- 完善个人信息：在个人中心，教员和老师都可以设置头像，更改个人信息。
- 教员：
  - 可以发布自己的课程，以供学生们申请。
  - 教员可以在“我的课程”来了解课程状态并管理课程。
  - 如果教员和学生联系之后，对于学生的申请同意，由教员通过申请，则课程完成匹配，无法再被申请。
- 学生：
  - 对于自己心仪的课程，可以点击申请并和老师取得联系。
  - 在老师通过申请之后，成功匹配到此课程的学生便可以随时提交对于此课程的评价。
- 本地测试URL：
  - 后台管理：http://127.0.0.1:8000/admin/
  - 注册：http://127.0.0.1:8000/user/register/
    登陆：http://127.0.0.1:8000/user/login/
  - 网站首页：http://127.0.0.1:8000/
  - 教师新增课程：http://127.0.0.1:8000/course/increase_course/
  - 课程详情界面：http://127.0.0.1:8000/course/detail_course/1/
  - 课程管理界面：http://127.0.0.1:8000/course/manage_course/

- 部署地址：https://group4.ml