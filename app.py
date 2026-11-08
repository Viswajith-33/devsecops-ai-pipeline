import os
import sqlite3
import subprocess
import ipaddress

password = os.environ.get("APP_PASSWORD")


def get_user(name):
    conn = sqlite3.connect("db.sqlite")
    return conn.execute("SELECT * FROM users WHERE name = ?", (name,))


def ping(host):
    ipaddress.ip_address(host)  # raises an error if host is not a valid IP
    subprocess.run(["ping", host], check=False)