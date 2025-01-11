import chainlit as cl
from src.task_utils import TaskUtils

task_utils = TaskUtils()

@cl.on_chat_start
async def on_chat_start():
    await task_utils.on_chat_start()

@cl.on_message
async def handle_message(message):
    await task_utils.handle_message(message)

if __name__ == "__main__":
    cl.run()