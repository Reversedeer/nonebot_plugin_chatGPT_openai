from nonebot.adapters.onebot.v11 import (Message,MessageSegment)
from nonebot import on_command
from nonebot.params import CommandArg
from .utils import *
from nonebot.rule import to_me
import asyncio

openai_text = on_command(
    "求助", aliases={"请问", "帮忙"}, block=True, priority=5， rule=to_me())



@openai_text.handle()
async def _(msg: Message = CommandArg()):
    if api_key == "没有api":
        await openai_text.send("请先配置openai_api_key")          # 没有配置openai_api_key
    prompt = msg.extract_plain_text()                     
    await openai_text.send(MessageSegment.text("Ding,思考中ing..."))
    prompt = msg.extract_plain_text()
    if prompt == "" or prompt.isspace():
        await openai_text.finish("笨蛋，空气是不可以问的涅qwq")
    loop = asyncio.get_event_loop()
    res = await loop.run_in_executor(None, get_openai_reply,prompt)
    # 将长消息的发送方式改为分段发送限制80字
    while len(res) > 80:
        await openai_text.send(MessageSegment.text(res[:80]))
        res = res[80:]
    await openai_text.send(MessageSegment.text(res))