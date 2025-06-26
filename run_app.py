# run_app.py
from pyngrok import ngrok
import os
import subprocess

# 1. Set ngrok authtoken (replace with your token)
# ngrok config add-authtoken 2wlIHlziqi9P43uBWHjWneLwnCy_5VzDYXZZcyNYFTqUB1o8k
NGROK_AUTHTOKEN = "2wlIHlziqi9P43uBWHjWneLwnCy_5VzDYXZZcyNYFTqUB1o8k"
os.system(f"ngrok config add-authtoken {NGROK_AUTHTOKEN}")
print("Ngrok authtoken configured.")

# 2. Start ngrok tunnel
print("Setting up ngrok tunnel...")
ngrok.kill()  # Kill existing tunnels

try:
    public_url = ngrok.connect(8501)
    print("✅ Ngrok tunnel active.")
    print(f"Public URL: {public_url}")
except Exception as e:
    print(f"❌ Ngrok error: {e}")
    exit(1)

# 3. Run Streamlit
if os.path.exists("app.py"):
    print("\nStarting Streamlit app...")
    print("(Press Ctrl+C to stop both Streamlit and ngrok)")
    
    # Run Streamlit in the foreground (no 'nohup' or '&')
    subprocess.run([
        "streamlit", "run", "app.py",
        "--server.port", "8501",
        "--server.enableCORS", "false",
        "--server.enableXsrfProtection", "false"
    ])
else:
    print("❌ Error: app.py not found!")