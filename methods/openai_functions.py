"""
openai_functions.py
2024-01-12, JK
These are functions which wrap OpenAI's API to add logging of tokens used e.g.
"""
from openai import OpenAI
import logging
import os


def set_up_logger(originator):
    filename_log = os.getenv("FILENAME_LOG")

    logging.basicConfig(
        filename=filename_log,
        level=logging.DEBUG,
        format=f"%(asctime)s - %(name)s - %(levelname)s - {originator} - %(message)s",
    )

    # Get the logger object
    logger = logging.getLogger(__name__)

    return logger


def create_openai_client(credentials):
    client = OpenAI(api_key=credentials["openai_api_key"])

    return client


def chat_completion(
    client,
    messages,
    model="gpt-3.5-turbo",
    temperature=0.1,
    logger=None,
):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=temperature,
    )

    answer = response.choices[0].message.content

    token_usage = response.usage

    if logger:
        logger.info(f"Token usage: {response.model + ', ' + str(token_usage)}")

    return answer, response


def de_this():
    messages = [{"role": "user", "content": "Say this is a test"}]

    return messages
