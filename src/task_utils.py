import chainlit as cl
from src.constants import Constants
from src.data_utils import OpenAIHelper

class TaskUtils:
    def __init__(self):
        self.openai_helper = OpenAIHelper()

    async def on_chat_start(self):
        await cl.Message(content=Constants.WELCOME_MESSAGE).send()
        file = await self.openai_helper.handle_file_upload()
        await self.openai_helper.process_file_and_store_data(file)

    async def handle_message(self, message):
        user_message = message.content
        response_content = await self.openai_helper.handle_user_message(user_message)
        await cl.Message(content=response_content).send()