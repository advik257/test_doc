import logging
import os
from datetime import datetime

class CustomLogger:
    def __init__(self,log_dir='logs'):
         # Ensure logs directory exists
        self.logs_dir = os.path.join(os.getcwd(), log_dir)
        os.makedirs(self.logs_dir, exist_ok=True)

        # Create a log file with the current date and time
        # Format: year-month-day_hour-minute-second.log
        Log_FILE =f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
        Log_FILE = os.path.join(log_dir, Log_FILE)
        # configure the logging++++++
        logging.basicConfig(
            filename=Log_FILE,
            format='[ %(asctime)s ]- %(levelname)s  %(name)s (line :%(lineno)d)- %(message)s',
            level=logging.INFO
        )

    def get_logger(self, name=__file__):
        return logging.getLogger(os.path.basename(name))

# Move this block outside the class
if __name__ == "__main__":
    logger_instance = CustomLogger()
    logger = logger_instance.get_logger(__file__)
    logger.info("Custom logger initialized successfully.")