from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask App!"})

@app.route('/status')
def status():
    return jsonify({"status": "running", "version": "1.0"})

if __name__ == '__main__':
    app.run(debug=True)
