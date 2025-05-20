from flask import Flask, request
import os
import time

app = Flask(__name__)

@app.route('/shutdown', methods=['GET'])
def safe_shutdown_test():
    auth = request.args.get('auth')
    if auth != "test123":  # Simple auth for security
        return "Unauthorized. Provide correct auth parameter.", 401
    
    try:
        # Simulate shutdown command (Render containers don’t support Windows shutdown)
        print("Simulating shutdown command for Windows: shutdown /s /t 20")
        # Note: Actual shutdown won’t work in Render’s Linux container
        # os.system("shutdown /s /t 20")  # Uncomment for local Windows testing
        return "Shutdown command simulated (20-second delay). In a Windows environment, cancel with 'shutdown /a'.", 200
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
