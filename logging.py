# monitoring_logging.py

import logging

logging.basicConfig(filename='device_activity.log', level=logging.INFO)

def log_activity(activity):
    logging.info(activity)
