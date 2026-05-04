from flask import Flask, request, jsonify, render_template, session, redirect, send_from_directory
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "super_secret_key"

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ================= DB =================
# ================= DB =================
def db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = db()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY,
        filename TEXT,
        owner TEXT,
        filepath TEXT,
        folder TEXT,
        is_public INTEGER DEFAULT 1,
        title TEXT DEFAULT '',
        description TEXT DEFAULT '',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        creator TEXT DEFAULT ''
    )
    """)

    # добавление колонки если её нет
    c.execute("PRAGMA table_info(files)")
    cols = [col[1] for col in c.fetchall()]

    if "creator" not in cols:
        c.execute("ALTER TABLE files ADD COLUMN creator TEXT DEFAULT ''")

    conn.commit()
    conn.close()

# ================= AUTH =================
@app.route("/login_page")
def login_page():
    return render_template("login.html")


@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = generate_password_hash(request.form["password"])

    conn = db()
    c = conn.cursor()

    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
    except:
        return "User exists"

    return redirect("/login_page")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    conn = db()
    c = conn.cursor()

    c.execute("SELECT password FROM users WHERE username=?", (username,))
    user = c.fetchone()

    if user and check_password_hash(user["password"], password):
        session["user"] = username
        return redirect("/")

    return redirect("/login_page")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login_page")


# ================= MAIN =================
@app.route("/")
def index():
    return render_template("index.html", user=session.get("user"))


# ================= UPLOAD =================
@app.route("/upload", methods=["POST"])
def upload():
    user = session.get("user", "guest")

    file = request.files["file"]
    filename = file.filename

    title = request.form.get("title", filename)
    description = request.form.get("description", "")
    is_public = 1 if request.form.get("public") else 0

    folder = "images"
    user_folder = os.path.join(UPLOAD_FOLDER, user, folder)
    os.makedirs(user_folder, exist_ok=True)

    filepath = os.path.join(user_folder, filename)
    file.save(filepath)

    conn = db()
    c = conn.cursor()

    c.execute("""
    INSERT INTO files (filename, owner, filepath, folder, is_public, title, description, creator)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", (filename, user, filepath, folder, is_public, title, description, request.form.get("creator", "")))

    conn.commit()
    conn.close()

    return "ok"


# ================= FILES =================
@app.route("/files")
def files():
    conn = db()
    c = conn.cursor()

    c.execute("SELECT * FROM files WHERE is_public=1 ORDER BY created_at DESC")
    rows = c.fetchall()

    return jsonify([
        {
            "id": r["id"],
            "url": "/" + r["filepath"].replace("\\", "/"),
            "title": r["title"],
            "description": r["description"],
            "created_at": r["created_at"],
            "uploaded_by": r["owner"],
            "creator": r["owner"]
        }
        for r in rows
    ])


@app.route("/my_files")
def my_files():
    user = session.get("user")
    if not user:
        return jsonify([])

    conn = db()
    c = conn.cursor()

    c.execute("SELECT * FROM files WHERE owner=? ORDER BY created_at DESC", (user,))
    rows = c.fetchall()

    return jsonify([
        {
            "id": r["id"],
            "url": "/" + r["filepath"].replace("\\", "/"),
            "title": r["title"],
            "description": r["description"],
            "created_at": r["created_at"],
            "uploaded_by": r["owner"],
            "creator": r["owner"]
        }
        for r in rows
    ])


# ================= STATIC FILES =================
@app.route("/uploads/<path:filename>")
def uploads(filename):
    return send_from_directory("uploads", filename)


# ================= DELETE =================
@app.route("/delete_file/<int:file_id>", methods=["DELETE"])
def delete_file(file_id):
    user = session.get("user")
    if not user:
        return "Unauthorized", 403

    conn = db()
    c = conn.cursor()

    c.execute("SELECT owner, filepath FROM files WHERE id=?", (file_id,))
    f = c.fetchone()

    if not f:
        return "Not found", 404

    if f["owner"] != user:
        return "Forbidden", 403

    if os.path.exists(f["filepath"]):
        os.remove(f["filepath"])

    c.execute("DELETE FROM files WHERE id=?", (file_id,))

    conn.commit()
    conn.close()

    return "ok"


# ================= UPDATE =================
@app.route("/update_file", methods=["POST"])
def update_file():
    user = session.get("user")
    if not user:
        return "Unauthorized", 403

    data = request.json

    conn = db()
    c = conn.cursor()

    c.execute("""
        UPDATE files
        SET title=?, description=?, creator=?
        WHERE id=?
    """, (
        data.get("title", ""),
        data.get("description", ""),
        data.get("creator", ""),
        data["id"]
    ))

    conn.commit()
    conn.close()

    return "ok"

@app.route("/file_meta/<int:file_id>")
def file_meta(file_id):
    conn = db()
    c = conn.cursor()

    c.execute("SELECT * FROM files WHERE id=?", (file_id,))
    r = c.fetchone()

    if not r:
        return "Not found", 404

    c2 = conn.cursor()
    c2.execute("""
        SELECT name FROM tags
        JOIN file_tags ON tags.id = file_tags.tag_id
        WHERE file_tags.file_id=?
    """, (file_id,))
    tags = [t["name"] for t in c2.fetchall()]

    return jsonify({
	"id": r["id"],
	"title": r["title"],
	"description": r["description"],
	"created_at": r["created_at"],
	"owner": r["owner"],
	"uploaded_by": r["owner"],
	"creator": r["creator"],   # 👈 теперь из БД
	"tags": tags,
	"url": "/" + r["filepath"].replace("\\", "/")
    })
# ================= INIT =================
if __name__ == "__main__":
    init_db()
    app.run(debug=True)
