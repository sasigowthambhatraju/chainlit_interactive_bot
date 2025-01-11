import chainlit as cl
import openai
import pandas as pd
import logging
import yaml
import os
from src.constants import Constants

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OpenAIHelper:
    def __init__(self, config_path=None):
        if config_path is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            config_path = os.path.join(base_dir, '..', 'config.yaml')
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        self.api_key = config['openai']['api_key']
        self.model = config['openai']['model']
        self.temperature = config['openai']['temperature']
        self.max_tokens = config['openai']['max_tokens']
        openai.api_key = self.api_key

    async def generate_response(self, messages):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        return response.choices[0]['message']['content'].strip()

    async def process_csv(self, file_path):
        df = pd.read_csv(file_path, encoding="utf-8")
        data_json = df.to_dict(orient='records')
        logger.info(data_json)
        return data_json

    async def handle_file_upload(self):
        files = None
        while files is None:
            files = await cl.AskFileMessage(
                content=Constants.SYS_MSG,
                accept=["text/csv"],
                max_size_mb=100,
                timeout=180,
            ).send()
        return files[0]

    async def process_file_and_store_data(self, file):
        msg = cl.Message(content=f"Processing `{file.name}`...")
        await msg.send()
        data_json = await self.process_csv(file.path)
        cl.user_session.set('data', data_json)
        msg.content = f"Processing `{file.name}` done. You can now ask questions!"
        await msg.update()

    async def handle_user_message(self, user_message):
        data_json = cl.user_session.get('data')

        if data_json:
            messages = [
                {"role": "system", "content": Constants.SYSTEM_MESSAGE_CSV},
                {"role": "user", "content": Constants.USER_MESSAGE_CSV.format(data_json=data_json, user_message=user_message)}
            ]
            response_content = await self.generate_response(messages)

            if "I'm sorry" in response_content:
                messages = [
                    {"role": "system", "content": Constants.SYSTEM_MESSAGE_GENERAL},
                    {"role": "user", "content": user_message}
                ]
                response_content = await self.generate_response(messages)
        else:
            messages = [
                {"role": "system", "content": Constants.SYSTEM_MESSAGE_GENERAL},
                {"role": "user", "content": user_message}
            ]
            response_content = await self.generate_response(messages)

        return response_content