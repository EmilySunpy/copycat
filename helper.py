import json
import glob
import MySQLdb
import MySQLdb.cursors

def loadConfig():
    with open("config.json", "r") as f:
        glob.config = json.load(f)

def connectSQL():
    try:
        glob.sql = MySQLdb.connect(**glob.config["sql"], cursorclass = MySQLdb.cursors.DictCursor)
    except Exception:
        print("Unable to connect to sql server")