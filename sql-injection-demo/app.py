from flask import Flask
from flask import request, jsonify
import psycopg2
import json

app = Flask(__name__)

@app.route('/checkUser')
def checkUser():
    user_arg = request.args.get('user')
    pass_arg = request.args.get('pass')

    print(user_arg, pass_arg)

    conn = psycopg2.connect(
        database="security", user='postgres', password='postgres', host='127.0.0.1', port= '5432'
    )

    cursor = conn.cursor()

    cursor.execute("""SELECT user_name FROM user_data WHERE user_name = %(user)s and user_password = %(pass)s""", {'user': user_arg, 'pass': pass_arg } )

    record = cursor.fetchall()

    cursor.close()
    conn.close()

    print(record)

    if not record:
        return jsonify({'error': 'user not found'})
    else:
        return jsonify(json.dumps(record, indent = 4) )

if __name__ == "__main__":
    app.run(debug=True, port=6000)

# readme 
# pip install flask
# pip install flask-mongoengine
###
#Schema MongoDB:
#{
#  "_id": {
#    "$oid": "644093d44100e8d352e8ee06"
#  },
#  "user": "some_user",
#  "password": "password"
#}
###