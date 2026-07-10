from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>DevOps Technical Assignment</h1>
    <p>Application is running successfully!</p>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "message": "App is running"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)