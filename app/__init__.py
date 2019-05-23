# launches Python Flask application to serve a sample web page that
# displays content from a MySQL database

import os
from flask import Flask, request, app
import socket
import mysql.connector
import yaml

# import configuration settings
app = Flask(__name__)
cfg_file = os.path.join('config', 'settings.yml')
with open(cfg_file) as yml:
    config = yaml.load(yml, Loader=yaml.FullLoader)

# create initial sql connector
db_conn = mysql.connector.connect(
    host     = config['db_host'],
    port     = config['db_port'],
    user     = config['db_user'],
    passwd   = config['db_pass'],
    database = config['db_name']
)

# a simple page that says hello
@app.route('/', methods=['GET'])
def hello():
    hostname = request.args.get('hostname')
    job_id   = request.args.get('job_id')
    mysql_results = ""

    # query MySQL database
    c = db_conn.cursor(dictionary=True)
    c.execute("SELECT * FROM test_table")
    for row in c:
        mysql_results += "<tr><td>{}</td></tr>".format(row['test_col'])

    html = """
            <h3>Hello World from {}!</h3>
            <h4>Job ID: {}</h4>
            <h4>MySQL DB: {}@{}:{}/{}</h4>
            <table style='border: 1px solid black;'>
                <thead>
                    <tr>
                        <th>Data from Database</th>
                    </tr>
                </thead>
                <tbody>
                    {}
                </tbody>
            </table>
""".format(hostname, job_id, config['db_user'], config['db_host'], config['db_port'], config['db_name'], mysql_results)

    return html.format(hostname=socket.gethostname(), job_id=job_id)
