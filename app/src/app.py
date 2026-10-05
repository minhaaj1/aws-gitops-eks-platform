from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevOps Platform</title>
        </head>
        <body>
            <h1>🚀 AWS DevOps GitOps Platform</h1>
            <p>Application deployed using Docker, Jenkins, Kubernetes and ArgoCD.</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
