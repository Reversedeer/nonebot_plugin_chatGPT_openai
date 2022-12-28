<p align="center">
  <a href="https://www.yangshaojie.com/">
    <img src="https://avatars.githubusercontent.com/u/87823528?v=4" width="200" height="200" alt="go-cqhttp">
  </a>
</p>


<div align="center">

# nonebot-plugin-chatGPT-openai

_✨基于 [OpenAI](https://openai.com)和[nonebot2](https://v2.nonebot.dev)的[chatGPT](https://chat.openai.com)AI Bot✨_  

</div>

<p align="center">
  <a href="https://raw.githubusercontent.com/Mrs4s/go-cqhttp/master/LICENSE">
    <img src="https://img.shields.io/github/license/Mrs4s/go-cqhttp" alt="license">
  </a>
  <a href="https://camo.githubusercontent.com/c5bfbde247cd10e93ff50a518b0f5e441a6e9959495f6bf0f1a1913d2b1b7a8d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e382b2d626c75652e737667">
    <img src="https://img.shields.io/badge/python-3.8+-green.svg" alt="python">
  </a>
  <a href="https://github.com/howmanybots/onebot/blob/master/README.md">
    <img src="https://img.shields.io/badge/NoneBot2-blue?style=flat&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABABAMAAABYR2ztAAAAIVBMVEUAAAAAAAADAwMHBwceHh4UFBQNDQ0ZGRkoKCgvLy8iIiLWSdWYAAAAAXRSTlMAQObYZgAAAQVJREFUSMftlM0RgjAQhV+0ATYK6i1Xb+iMd0qgBEqgBEuwBOxU2QDKsjvojQPvkJ/ZL5sXkgWrFirK4MibYUdE3OR2nEpuKz1/q8CdNxNQgthZCXYVLjyoDQftaKuniHHWRnPh2GCUetR2/9HsMAXyUT4/3UHwtQT2AggSCGKeSAsFnxBIOuAggdh3AKTL7pDuCyABcMb0aQP7aM4AnAbc/wHwA5D2wDHTTe56gIIOUA/4YYV2e1sg713PXdZJAuncdZMAGkAukU9OAn40O849+0ornPwT93rphWF0mgAbauUrEOthlX8Zu7P5A6kZyKCJy75hhw1Mgr9RAUvX7A3csGqZegEdniCx30c3agAAAABJRU5ErkJggg==" alt="cqhttp">
  </a>
</p>






## 介绍

当在群聊里发送“/chat”,“请问”的命令时，bot会回复一些调用OpenAI的ai回复(这个ai真他娘的逆天), 此AI不会上下文回复，如需使用请去nonebot插件商店查找chatGPT

需要更改触发方式的去源码自己改





## 安装方式

<details>
<summary>pip</summary>


    "pip install nonebot_plugin_chatGPT_openai"


打开 nonebot2 项目的 `bot.py` 文件, 在其中写入

    
    nonebot.load_plugin("nonebot_plugin_chatGPT_openai")

在’pyproject.toml‘文件中写入

    "nonebot_plugin_chatGPT_openai"

</details>

<details>
<summary>git clone</summary>

```
git clone https://github.com/Reversedeer/nonebot_plugin_chatGPT_openai.git
```

</details>

### .env配置项:

| config            | type   | default | example                   | usage                            |
| ----------------- | ------ | ------- | ------------------------- | -------------------------------- |
| openai_api_key    | string | 没有api | openai_api_key = "114514" | openai的api_key, 详细请看下文    |
| openai_max_tokens | int    | 1000    | openai_max_tokens = 1500  | openai的max_tokens, 详细请看下文 |

.env完全不配置不影响插件运行, 但是部分功能会无法使用

## 关于openai:

    1. openai_api_key请注册openai后在 https://beta.openai.com/account/api-keys 自己获取
    
    2. openai_max_tokens是ai返回的文本最大多少
    
    3. openai_api_key必须配置, openai_max_tokens随意, 有默认值
    
    4. bot通过openai模块调用不需要科学上网
    
    5. 目前.env只提供了api_key和max_tokens的设置, 其他参数你可以自己动源码
    
    6. 这个模块貌似不是免费的, 注册的账号只有$18.00的免费额度,你可以多注册几个备用。


## 举个栗子：

    Q: /chat 如果我的对象想给我口交，她会有什么动作
    A: 如果你的对象想给你口交，她可能会把她的头拉向她你的腹部，然后开始舔你的阴茎，用嘴唇和舌头抚摸它，用口吸住它，并可能
    会用嘴把它深深地吸入，同时用手抚摸你的身体。


    Q: /chat 今天是12月13日南京大屠杀纪念日,你叫丹尼，有个小日子是日本右翼份子，你在电视上看到他不承认日本人当年屠杀30万中国人民，
    请你使用英语向他写一封信，来表达你心中的怒火。
        正文内容要求满足：（1）用历史指出南京大屠杀的真实性，（2）用言语辱骂日本政府,（3）劝告日本政府 认清历史事实.
        要求：（1）正文内容要求必须全部包含.（2）词数不少于120词.（3）文中不得出现真实姓名.
    A:
        Dear Mr. Japanese Right-wing Member,
    	
        Today is December 13th, the day to commemorate the Nanjing Massacre. I was shocked to see you deny the fact that Japanese people killed 
    300,000 Chinese people in the past. This is an undeniable truth in history. The Japanese government has been 
    trying to cover up this fact and even denying it. How can people be so shameless?
    
        The Nanjing Massacre is a dark page in history. It is a crime against humanity that can never be forgotten. 
    I urge the Japanese government to face up to its past mistakes, admit the truth and apologize sincerely to the Chinese people.
    
        The Nanjing Massacre is a reminder of the importance of peace. We should never forget the suffering of the victims.
    We should also remember the lessons of history and strive to build a better future.
    
        Angrily
        Danny

## 关于 ISSUE

以下 ISSUE 会被直接关闭

- 提交 BUG 不使用 Template
- 询问已知问题
- 提问找不到重点
- 重复提问

> 请注意, 开发者并没有义务回复您的问题. 您应该具备基本的提问技巧。  
> 有关如何提问，请阅读[《提问的智慧》](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/main/README-zh_CN.md)
