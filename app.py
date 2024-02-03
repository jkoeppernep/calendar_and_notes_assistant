"""
app.py
2024-01-10, JK
Purpose: Generate dailiy briefing and provide it in the way specified in the foloowing.
Start with dummy data from HardcodedPersonalDataHub clas.
"""
from classes.personal_data_hub import HardcodedPersonalDataHub as DataHub
from classes.data_extractor import DataExtractor
from classes.report_generator import ReportGenerator
from classes.report_token_usage import ReportTokenUsage

from methods.openai_functions import set_up_logger
from methods.helper_functions import load_yaml_file, propare_environment

from dotenv import load_dotenv, find_dotenv
import os
import yaml


# -------------------------------------------------------
## Parameters
# -------------------------------------------------------
control_parameters = {
    "print_data_hub": True,
    "skip_summarization": True,
    "skip_audio_generation": True,
}


# -------------------------------------------------------
## App
# -------------------------------------------------------
# Logger
logger = set_up_logger(originator="JK")

# Load environmaent and configuration variables ------------------------------------------------------------------
resources, credentials = propare_environment(logger=logger)

# Objects (using dependency injection) ------------------------------------------------------------------
data_hub = DataHub(credentials=credentials, logger=logger)

extractor = DataExtractor(
    data_hub, resources=resources, credentials=credentials, logger=logger
)

report_generator = ReportGenerator(
    resources=resources, credentials=credentials, extractor=extractor, logger=logger
)

token_usage_reporter = ReportTokenUsage(credentials=credentials)

# Update user data ------------------------------------------------------------------
data_hub.update_data(i_day_from_yaml=0)

if control_parameters["print_data_hub"]:
    data_hub.print_data()

# Create summary
if not control_parameters["skip_summarization"]:
    extractor.create_summary()
else:
    extractor.mock_create_summary()

extractor.get_summary()

if control_parameters["print_data_hub"]:
    print(extractor.get_summary())


# Generate report
if not control_parameters["skip_audio_generation"]:
    report_generator.generate_audio_report()

token_usage_reporter.get_token_usage()
