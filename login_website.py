import flask
#import login_system as ls

app = flask.Flask(__name__)
user_names = []
passwords = []

@app.route("/home")
def home():
    return "Go to /voting to vote and /results to see the current results."

@app.route("/register", methods=["GET", "POST"])
def register():
    if flask.request.method == "POST":
        user = flask.request.form["user"]
        passw = flask.request.form["password"]
        user_names.append(user)
        passwords.append(passw)
        return flask.render_template("registered.html")
    return flask.render_template("registering.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
