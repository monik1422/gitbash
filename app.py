from flask import Flask
import nginx

app = Flask(__name__)

@app.route("/")
def hello():
    return "updated Flask sample application on AWS High Availability service, updated version-5."


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 443))

    app.run(debug=True,host='0.0.0.0',port=port)
