from flask import Flask, render_template, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

def get_logs():
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
    date_str = datetime.now().strftime('%Y-%m-%d')
    log_file = os.path.join(log_dir, f'daily_actions_{date_str}.log')
    logs = []
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            for line in f:
                try:
                    logs.append(json.loads(line))
                except:
                    pass
    return logs

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stats')
def stats():
    logs = get_logs()
    
    # Mocking some metrics for the dashboard feel
    data = {
        "revenue": "$1,402.50",
        "videos_posted": 3,
        "views": "45.2K",
        "orders": 24,
        "recent_logs": list(reversed(logs))[:15]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
