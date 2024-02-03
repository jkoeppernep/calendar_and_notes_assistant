"""
data_extractor.py
2024-01-12, JK
Thie DataExtractor class creates summaries using GPT-4 based on the
user's personal data probided in the PersonalDataHub data_hub object.
"""
from methods.openai_functions import create_openai_client, chat_completion


class DataExtractor:
    def __init__(self, data_hub, resources, credentials, logger=None):
        self.__data_hub = data_hub

        self.__resources = resources

        self.__credentials = credentials

        self.__client = create_openai_client(
            credentials=self._DataExtractor__credentials
        )

        self.__logger = logger

    def mock_summary(self):
        self.__summary = self._DataExtractor__data_hub["mock_summary"]

    def create_summary(self):
        # Create messages
        prompt_raw = self._DataExtractor__resources["gpt_prompts"]["generate_summary"]

        _, data_str = self._DataExtractor__data_hub.get_data()

        prompt = prompt_raw.format(user_data_string=data_str)

        messages = [
            {
                "role": "system",
                "content": self._DataExtractor__resources["gpt_prompts"][
                    "generate_summary_system"
                ],
            },
            {"role": "user", "content": prompt},
        ]

        # Create summary
        summary, response = chat_completion(
            client=self._DataExtractor__client,
            messages=messages,
            logger=self._DataExtractor__logger,
        )

        self.__summary = summary

    def mock_create_summary(self):
        self.__summary = self._DataExtractor__data_hub.get_mocked_summary()

    def get_summary(self):
        return self.__summary
