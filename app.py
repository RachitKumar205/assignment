from flask import Flask, render_template, jsonify
import subprocess
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script')
def run_script():
    try:
        result = subprocess.run(['python', 'selenium_script.py'], capture_output=True, text=True)
        result.check_returncode()  # Raises CalledProcessError if the script fails
        data = json.loads(result.stdout.strip())
        return jsonify({"message": "Script executed", "result": data})
    except subprocess.CalledProcessError as e:
        return jsonify({"message": "Script failed", "error": str(e), "stderr": result.stderr})
    except json.JSONDecodeError:
        return jsonify({"message": "Script executed but returned invalid JSON", "output": result.stdout.strip(), "stderr": result.stderr})
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
