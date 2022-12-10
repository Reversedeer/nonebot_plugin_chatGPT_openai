<p align="center">
  <a href="https://www.yangshaojie.com/">
    <img src="https://avatars.githubusercontent.com/u/87823528?v=4" width="200" height="200" alt="go-cqhttp">
  </a>
</p>


<div align="center">

# nonebot-openai

_✨基于 [OpenAI](https://openai.com)和[nonebot2](https://v2.nonebot.dev)的[chatGPT](https://chat.openai.com)AI Bot✨_  

</div>

<p align="center">
  <a href="https://raw.githubusercontent.com/Mrs4s/go-cqhttp/master/LICENSE">
    <img src="https://img.shields.io/github/license/Mrs4s/go-cqhttp" alt="license">
  </a>
  <a href="https://github.com/Mrs4s/go-cqhttp/releases">
    <img src="https://img.shields.io/badge/python-3.8+-green.svg" alt="python">
  </a>
  <a href="https://github.com/howmanybots/onebot/blob/master/README.md">
    <img src="https://img.shields.io/badge/OneBot-v11-blue?style=flat&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABABAMAAABYR2ztAAAAIVBMVEUAAAAAAAADAwMHBwceHh4UFBQNDQ0ZGRkoKCgvLy8iIiLWSdWYAAAAAXRSTlMAQObYZgAAAQVJREFUSMftlM0RgjAQhV+0ATYK6i1Xb+iMd0qgBEqgBEuwBOxU2QDKsjvojQPvkJ/ZL5sXkgWrFirK4MibYUdE3OR2nEpuKz1/q8CdNxNQgthZCXYVLjyoDQftaKuniHHWRnPh2GCUetR2/9HsMAXyUT4/3UHwtQT2AggSCGKeSAsFnxBIOuAggdh3AKTL7pDuCyABcMb0aQP7aM4AnAbc/wHwA5D2wDHTTe56gIIOUA/4YYV2e1sg713PXdZJAuncdZMAGkAukU9OAn40O849+0ornPwT93rphWF0mgAbauUrEOthlX8Zu7P5A6kZyKCJy75hhw1Mgr9RAUvX7A3csGqZegEdniCx30c3agAAAABJRU5ErkJggg==" alt="cqhttp">
  </a>
</p>





## 介绍

当在群聊里发送“@bot 求助”,“请问”的命令时，bot会回复一些调用OpenAI的ai回复(这个ai真他娘的逆天), 此AI不会上下文回复，如需使用请去nonebot插件商店查找chatGPT





## 安装方式

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装


    nb plugin install nonebot-plugin-openai

</details>

<details>
<summary>pip</summary>
    打开 nonebot2 项目的 `bot.py` 文件, 在其中写入


    pip install nonebot-plugin-openai

    nonebot.load_plugin("nonebot_plugin_openai")

在’pyproject.toml‘文件中写入

    "nonebot_plugin_openai"

</details>

### env配置项:

| config            | type   | default | example                   | usage                            |
| ----------------- | ------ | ------- | ------------------------- | -------------------------------- |
| openai_api_key    | string | None    | openai_api_key = "114514" | openai的api_key, 详细请看下文    |
| openai_max_tokens | int    | 1000    | openai_max_tokens = 1500  | openai的max_tokens, 详细请看下文 |
| openai_cd_time    | int    | 60      | openai_cd_time = 114      | openai调用的cd                   |

.env完全不配置不影响插件运行, 但是部分功能会无法使用

## 关于openai:

    1. openai_api_key请注册openai后在 https://beta.openai.com/account/api-keys 自己获取
    
    2. openai_max_tokens貌似是ai返回的文本最大多少(根据我自己用的经验)
    
    3. openai_api_key必须配置, openai_max_tokens随意, 有默认值
    
    4. bot通过openai模块调用应该不需要科学上网
    
    5. 目前env只提供了api_key和max_tokens的设置, 其他参数你可以自己动源码
    
    6. 据我个人使用的情况, 总是有群友提问一些引诱犯罪的问题, 如果你遇到这种情况, 你可以考虑自己处理prompt字符串做一些判断
    
    7. 这个模块貌似不是免费的, 注册的账号只有$18.00的免费额度, 有大佬调用了大约1500回, 目前的额度 $7.05 / $18.00
    
    8. 一些具体的实例:
    
        Q: @bot求助 使用golang定义一个全局变量client, 并让其在init函数内与redis相连接
        A: @USER  
            package main
            import (
                "github.com/go-redis/redis"
            )
            var client *redis.Client
            func init() {
                client = redis.NewClient(&redis.Options{
                    Addr:     "localhost:6379",
                    Password: "", // no password set
                    DB:       0,  // use default DB
                })
            }
            (这逼甚至手撕二叉树, 手撸STL容器, 已经吊打我这个废物了....)
    
        Q: @bot求助 假如你是李华，今日中国三大运营商——中国联通，中国移动，中国电信，屏蔽了中国境内对 GitHub 的访问，请你使用英语向你的外国笔友
           Jane写一封信，简要讨论这件事。正文内容要点：（1）对GitHub被封感到震惊、（2）谈论此事对中国开源界的影响、（3）对中国开源界的未来进行探讨。
           要求：（1）正文要点必须全部包含、（2）词数不少于100词、（3）文中不得出现真实的姓名
        A: @USER 
            Dear Jane,
            I am writing to tell you about a shocking news that three major Chinese operators, China Unicom, 
            China Mobile and China Telecom, have blocked access to GitHub in China.
    
            This news has caused great concern among Chinese open source communities. On the one hand, the 
            number of people who use GitHub to store and share their codes has decreased dramatically. On the
            other hand, the development of open source technology in China is facing a great challenge.
    
            I'm really worried about the future of open source in China. The government should take measures
            to guarantee the development of open source projects and encourage more people to join in. Moreover,
            the operators should also consider the interests of users and provide better services.
    
            I hope the situation can be improved soon.
    
            Yours,
            Li Hua

## 举个栗子：

    Q: 求助 群聊的同性朋友总幻想和我发生性关系怎么办
    A: 首先，你需要有耐心，坦诚地和朋友进行沟通，明确你的立场。如果朋友不能理解你的想法，你可以尝试改变聊天的话题，
       让谈话变得更加积极有趣。如果朋友仍然追求你，你可以向他/她明确表达你的立场，如果朋友仍然不能接受，你可以考虑暂时结束聊天，
       或者把他/她从群聊中移除。

## 关于 ISSUE

以下 ISSUE 会被直接关闭

- 提交 BUG 不使用 Template
- 询问已知问题
- 提问找不到重点
- 重复提问

> 请注意, 开发者并没有义务回复您的问题. 您应该具备基本的提问技巧。  
> 有关如何提问，请阅读[《提问的智慧》](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/main/README-zh_CN.md)
