from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(name)
app.secret_key = "secretkey"

# مستخدم مبرمج
users = {
    "BAN1HAN": "admin"
}

# قائمة التحديات
challenges = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            session["user"] = username
            return redirect(url_for("index"))
        else:
            return "اسم المستخدم أو كلمة المرور غير صحيحة"
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users:
            return "اسم المستخدم مستخدم مسبقاً"
        users[username] = password
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("index"))

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if "user" in session and session["user"] == "BAN1HAN":
        if request.method == "POST":
            title = request.form["title"]
            description = request.form["description"]
            challenges.append({"title": title, "description": description})
        return render_template("admin.html", users=users, challenges=challenges)
    else:
        return "ممنوع الدخول", 403

if name == "main":
    app.run(debug=True)
