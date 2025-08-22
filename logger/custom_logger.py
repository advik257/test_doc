import os
import logging
from datetime import datetime
import structlog

class CustomLogger:
    def __init__(self, log_dir="logs"):
        # Ensure logs directory exists
        self.logs_dir = os.path.join(os.getcwd(), log_dir)
        os.makedirs(self.logs_dir, exist_ok=True)
        
        # Timestamped log file (for persistence)
        log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
        self.log_file_path = os.path.join(self.logs_dir, log_file)

        # Configure the logging - moved from get_logger to __init__
        logging.basicConfig(
            filename=self.log_file_path,
            format="[%(asctime)s] [%(levelname)s] %(name)s (line:%(lineno)d) - %(message)s",
            level=logging.INFO,
            datefmt="%Y-%m-%d %H:%M:%S",
        )

    def get_logger(self, name=__file__):
        return logging.getLogger(os.path.basename(name))

# --- Usage Example ---
if __name__ == "__main__":
    logger = CustomLogger()
    log = logger.get_logger(__file__)
    log.info("custom logger initialized")

