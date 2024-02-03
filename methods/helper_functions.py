"""
helper_functions.py
2024-01-13, JK
"""
import os
import yaml
from dotenv import load_dotenv, find_dotenv


def propare_environment(logger=None):
    # env_morning_assistant
    load_dotenv(find_dotenv(".env_morning_assistant"))
    # print(os.environ)

    BASE_DIR = os.getenv("BASE_DIR")

    RESOURCES_FILE_NAME = os.getenv("RESOURCES_FILE_NAME")

    os.chdir(BASE_DIR)

    # Credentials
    load_dotenv(find_dotenv("..env"))

    openai_api_key = os.getenv("OPENAI_API_KEY")

    filename_log = os.getenv("FILENAME_LOG")
    path_log = os.path.join(BASE_DIR, filename_log)

    credentials = {
        "openai_api_key": openai_api_key,
        "base_dir": BASE_DIR,
        "filename_log": path_log,
    }

    # Resources
    resources_file_name = RESOURCES_FILE_NAME

    resources = load_yaml_file(
        resources_file_name, credentials=credentials, logger=logger
    )

    return resources, credentials


def load_yaml_file(rel_path, credentials, logger=None):
    bawse_dir = credentials["base_dir"]

    abs_path = os.path.join(bawse_dir, rel_path)

    with open(rel_path, "r") as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)

            if logger:
                logger.error(exc)
