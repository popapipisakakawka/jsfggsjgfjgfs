from flask import Flask, render_template
import sqlite3
import os

DB_PATH = "shop.db"
COOKIES_DIR = "cookies"
LOGS_DIR = "logs"

app = Flask(__name__)

def get_users():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT uid, user_id, balance, banned FROM users")
    rows = cur.fetchall()
    conn.close()
    return rows

def get_cookies():
    if not os.path.exists(COOKIES_DIR):
        return []
    return os.listdir(COOKIES_DIR)

@app.route("/")
def admin_panel():
    users = get_users()
    cookies = get_cookies()
    return render_template(
        "admin.html",
        users=users,
        cookies=cookies
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
