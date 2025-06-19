from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/result")
def result():
  id = request.args.get("id")
  conn = sqlite3.connect("data.db")
  c = conn.cursor()
  c.execute("SELECT * FROM result WHERE id = ?", (id,))
  data = c.fetchone()
  conn.close()
  return render_template("result.html", data=data)
