# flask related imports
from flask import Flask
from flask import jsonify
from flask import request,abort


# other python libs
import sys
import sqlite3 as sql


def dict_factory(cursor,row):
    d = {}
    for idx,col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

app = Flask(__name__)
@app.route('/')
def index():
    return "Key Server"

@app.route('/test_api/', methods = ['POST'])
def test():
    tmp = request.get_json()
    return jsonify({'status': 'success'})

@app.route('/insert_users/',methods=['POST'])
def insert_users():
    if not request.json or not 'username' in request.json:
        print('aborted')
        abort(400)

    username = request.json['username']
    public_key = request.json['public_key']
    salt = request.json['salt']

    status = "failure"
    with sql.connect("database.db") as con:
        con.row_factory = dict_factory
        cur = con.cursor()

        cur.execute("SELECT * FROM users WHERE username=?",(str(username),))
        users = cur.fetchall()

        if users:
            status = "failure"
        else:
            print("inserting")
            cur.execute("INSERT INTO users (username,public_key,salt) VALUES (?,?,?)",(str(username),str(public_key),str(salt)))
            print("inserted")
            con.commit()
            print("comitted")
            status = "success"
    return jsonify({'status':status});

@app.route('/get_user/<username>',methods=['GET'])
def get_user(username):
    with sql.connect("database.db") as con:
        con.row_factory = dict_factory
        cur = con.cursor()

        cur.execute("SELECT * FROM users WHERE username=?",(str(username),))
        users = cur.fetchall()

        if not users:
            abort(404)
        else:
            user = {
                'username': users[0]['username'],
                'public_key':users[0]['public_key'],
                'salt':users[0]['salt']
            }
            return jsonify(user)


if __name__ == "__main__":
    host = sys.argv[1]
    port = sys.argv[2]

    app.run(
        host = host,
        port = port,
        debug = True
    )
