import os
import json
from datetime import datetime

class BrainLogger:
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)
        
    def _get_daily_log_path(self):
        date_str = datetime.now().strftime("%Y-%m-%d")
        return os.path.join(self.log_dir, f"daily_actions_{date_str}.log")
        
    def log_action(self, category, action, details=None, status="SUCCESS"):
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "category": category,
            "action": action,
            "status": status,
            "details": details or {}
        }
        
        filepath = self._get_daily_log_path()
        with open(filepath, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
            
        print(f"[{log_entry['timestamp']}] [{category}] {action} - {status}")

    def get_todays_actions(self):
        filepath = self._get_daily_log_path()
        if not os.path.exists(filepath):
            return []
        with open(filepath, "r") as f:
            return [json.loads(line) for line in f.readlines()]
