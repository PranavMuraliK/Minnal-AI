import time
import os
import schedule
import yaml
import sys

# Add parent dir to path so we can import brain
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from brain.logger import BrainLogger

def load_config():
    with open(os.path.join(os.path.dirname(__file__), 'config.yaml'), 'r') as f:
        return yaml.safe_load(f)

class AICEO:
    def __init__(self):
        self.config = load_config()
        self.logger = BrainLogger(log_dir=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs'))
        
        self.logger.log_action("SYSTEM", "Initialization", {"status": "Starting AI CEO Engine..."})
    
    def run_content_pipeline(self):
        self.logger.log_action("CONTENT", "Started Content Creation Pipeline")
        # completely automated hook, script, video gen here
        time.sleep(2)
        self.logger.log_action("CONTENT", "Completed Content Pipeline", {"videos_generated": 1})

    def run_dropshipping_check(self):
        self.logger.log_action("ECOM", "Started Product/Price Optimization")
        # analyze trends, modify listings
        time.sleep(1)
        self.logger.log_action("ECOM", "Completed Dropshipping Check", {"products_updated": 0})
        
    def generate_daily_report(self):
        self.logger.log_action("SYSTEM", "Generating Daily Actions Report")
        actions = self.logger.get_todays_actions()
        # summarize actions, create strategy report
        time.sleep(1)
        self.logger.log_action("SYSTEM", "Daily Report Generated")

    def run(self):
        self.logger.log_action("SYSTEM", "Entering Main Engine Loop")
        
        # Scheduling
        schedule.every(self.config['schedule']['shorts_upload_frequency_hours']).hours.do(self.run_content_pipeline)
        schedule.every(6).hours.do(self.run_dropshipping_check)
        schedule.every().day.at("23:00").do(self.generate_daily_report)
        
        # Initial run on startup
        self.run_content_pipeline()
        self.run_dropshipping_check()
        
        while True:
            schedule.run_pending()
            time.sleep(60)

if __name__ == "__main__":
    ceo = AICEO()
    try:
        ceo.run()
    except KeyboardInterrupt:
        ceo.logger.log_action("SYSTEM", "Shutdown", {"status": "Manual termination"})
        print("AI CEO Engine stopped.")
