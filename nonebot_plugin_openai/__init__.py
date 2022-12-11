# 导入必要的库
from nonebot.adapters.onebot.v11 import (Message,MessageSegment)
from nonebot import on_command
from nonebot.params import CommandArg
from .utils import *
from nonebot.rule import to_me
import asyncio

# 定义命令
openai_text = on_command(
    "/chat", aliases={"请问", "帮忙"}, block=True, priority=5)


    
@openai_text.handle()
async def _(msg: Message = CommandArg()):
    if api_key == "没有api":
        await openai_text.finish("请先配置openai_api_key")
    prompt = msg.extract_plain_text()
    if prompt == "" or prompt == None or prompt.isspace():
        await openai_text.finish("笨蛋，空气是不可以问的涅qwq")
    await openai_text.send(MessageSegment.text("Ding,思考中ing..."))
    loop = asyncio.get_event_loop()
    try:
        res = await loop.run_in_executor(None, get_openai_reply, prompt)
    except Exception as e:
        await openai_text.finish(str(e))
    await openai_text.finish(MessageSegment.text(res))