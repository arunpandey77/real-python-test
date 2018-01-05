from flask import Flask
app = Flask(__name__)
app.config["DEBUG"] = True
@app.route("/")
@app.route("/hello")
def hello_world():
    return "hello world"
@app.route("/test/<search_query>")
def search(search_query):
    return "hello world"
@app.route("/name/name")
def index(name):
    if name.lower()=="arun":
        return"hello {}".format(name)
    else:
        return "not found"
if __name__ == "__main__":
    app.run()