import sqlite3, subprocess

password = "admin123"

def get_user(name):
    conn = sqlite3.connect("db.sqlite")
    return conn.execute("SELECT * FROM users WHERE name = '" + name + "'")

def ping(host):
    subprocess.call("ping " + host, shell=True)