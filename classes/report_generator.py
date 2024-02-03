"""
report_generator.py
2024-01-13, JK
Calss ReportGenerator for generation presentaions of the summrized data.
- Audio
- HTML
"""
from methods.openai_functions import create_openai_client


class ReportGenerator:
    def __init__(self, resources, credentials, extractor, logger=None):
        self.__resources = resources

        self.__credentials = credentials

        self.__logger = logger

        self.__extractor = extractor

        self.__client = client = create_openai_client(credentials=credentials)

    def generate_html_report(self):
        pass

    def generate_audio_report(self, speech_file_path="speech.mp3"):
        client = self.__client

        this_summary = self.__extractor.get_summary()

        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=this_summary,
        )

        response.stream_to_file(speech_file_path)
