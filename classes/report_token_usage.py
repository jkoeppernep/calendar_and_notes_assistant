"""
report_token_usage.py
2024-01-14, JK
These class parse the log file for information about token usage.
They are written to a pandas dataframe and analyzed.
"""
import os
import pandas as pd
import re


class ReportTokenUsage:
    def __init__(self, credentials):
        self.__credentials = credentials

        self.__log_file_path = credentials["filename_log"]

        self.__df_token_usage = None

    def get_token_usage(self):
        # Initialize lists to store the extracted data
        models = []
        completion_tokens = []
        prompt_tokens = []
        total_tokens = []

        # Regular expression pattern to extract the needed information
        pattern = r"Token usage: (gpt-\d+-\d+), CompletionUsage\(completion_tokens=(\d+), prompt_tokens=(\d+), total_tokens=(\d+)\)"

        with open(self.__log_file_path, "r") as file:
            for line in file:
                if "Token usage:" in line:
                    match = re.search(pattern, line)
                    if match:
                        # Extract and append the data
                        models.append(match.group(1))
                        completion_tokens.append(int(match.group(2)))
                        prompt_tokens.append(int(match.group(3)))
                        total_tokens.append(int(match.group(4)))

                # Create a DataFrame
                df = pd.DataFrame(
                    {
                        "Model": models,
                        "Completion Tokens": completion_tokens,
                        "Prompt Tokens": prompt_tokens,
                        "Total Tokens": total_tokens,
                    }
                )

        print(df)
