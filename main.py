from flask import flask

app = flask(__name__)

@app.route("/")
def home():
  return "hello, this is your bank challenge"

if __name__ == "__main__":
  app.run()
