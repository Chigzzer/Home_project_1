import flask
import logging
import os
logging.basicConfig(filename="login_web_log.log", level=logging.INFO)
log = logging.getLogger(__name__)
app = flask.Flask(__name__)
user_names = []
passwords = []
app.secret_key = os.urandom(24)



@app.route("/test")
def test():
    flask.flash("hello")
@app.route("/home")
def home():
    if not flask.session.get("logged in"):
        return flask.redirect("/login")
    else:
        return "Go to /voting to vote and /results to see the current results."


@app.route("/register", methods=["GET", "POST"])
def register():
    if flask.request.method == "POST":
        user = flask.request.form["user"]
        passw = flask.request.form["password"]
        log.info("Obtaining the submitted username and password.")
        if user in user_names:
            log.info("Checking if the username is already taken")
            print("That username is taken, please try again")
        else:
            user_names.append(user)
            passwords.append(passw)
            log.info("Adding the new username and password to the system.")
            return flask.render_template("registered.html")
    return flask.render_template("registering.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "POST":
        user = flask.request.form["user"]
        password = flask.request.form["password"]
        if user in user_names and password == passwords[user_names.index(user)]:
            flask.session["Logged in"] = True
            return flask.redirect("/home")
        # TODO create a logged in html and check if access home works.
        else:
            return flask.redirect("/register")
    return flask.render_template("log_in.html")





if __name__ == "__main__":
    app.debug = True
    app.run()
