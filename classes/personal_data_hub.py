# personal_data_hub.py
# 2024-01-10, JK
# The class PersonalDataHub is a singleton class that is used to store and retrieve personal data.
# Data are the user's name, private calendar, work calendar and so on.
from methods.helper_functions import load_yaml_file
import os


# PersonalDataHub ------------------------------------------------------------------
# @Nico, bitte lösche diesen Kommentar, wenn du ihn gelesen hast.
# Ich wollte das Arbeiten mit einer Baxsisklasse in Python ausprobieren, auch wenn ich, Deinem Rat folgend, nicht mit der Archtiektur in voller Schönheit imersten Schritt beginnen will.
# Bei den anderen Klassen werde ich anders verfahren.
class PersonalDataHub:
    def __init__(self, credentials, logger=None):
        self.__user_name = None
        self.__personal_calendar_today = None
        self.__professional_calendar_today = None
        self.__notes_previous_days = None
        self.__date_for_summary = None
        self.__logger = logger
        self.__credentials = credentials

    # Remember to update the rest of your methods to use the new private variables
    # For example:
    def get_data(self):
        data = {
            "user_name": self._PersonalDataHub__user_name,
            "personal_calendar_today": self._PersonalDataHub__personal_calendar_today,
            "professional_calendar_today": self._PersonalDataHub__professional_calendar_today,
            "notes_previous_days": self._PersonalDataHub__notes_previous_days,
            "date_for_summary": self._PersonalDataHub__date_for_summary,
        }

        data_str = ""

        for key, value in data.items():
            data_str += f"# {key}\n{str(value).replace(' #', ' ##')}\n\n"

        return data, data_str

    def print_data(self):
        _, data_str = self.get_data()

        print(data_str)


# HardcodedPersonalDataHub ------------------------------------------------------------------
class HardcodedPersonalDataHub(PersonalDataHub):
    def get_mocked_summary(self):
        return self.__mocked_summary

    def update_data(self, i_day_from_yaml=0):
        # load yaml file base_dir/ + environment variable DEMO_DATA_FILE
        rel_path = os.getenv("DEMO_DATA_FILE")

        abs_path = os.path.join(
            self._PersonalDataHub__credentials["base_dir"], rel_path
        )

        pesonal_data = load_yaml_file(
            abs_path, self._PersonalDataHub__credentials, self._PersonalDataHub__logger
        )

        # Fill attributes with data from yaml file, day i_day_from_yaml
        this_pesonal_data = pesonal_data["days"][i_day_from_yaml]

        self._PersonalDataHub__user_name = "Max"

        self.__mocked_summary = this_pesonal_data["mocked_summary"]

        self._PersonalDataHub__personal_calendar_today = this_pesonal_data[
            "personal_calendar"
        ]

        self._PersonalDataHub__professional_calendar_today = this_pesonal_data[
            "professional_calendar"
        ]

        self._PersonalDataHub__notes_previous_days = this_pesonal_data[
            "previous_day_notes"
        ]

        self._PersonalDataHub__date_for_summary = this_pesonal_data["date"]
