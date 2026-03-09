import subprocess
import sys
import os

if __name__ == "__main__":
    print("🔮 Starting Drishyamitra Backend Server...")
    os.environ.setdefault('FLASK_ENV', 'production')
from app import app
app.run(host='0.0.0.0', port=5000, debug=False)