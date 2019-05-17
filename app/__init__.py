import os
from flask import Flask, request
import socket

app = Flask(__name__)

# a simple page that says hello
@app.route('/', methods=['GET'])
def hello():
    html = """
            <h3>Hello World from {hostname}!</h3>
            <h4>Job ID: {job_id}</h4>
"""
    job_id = request.args.get('job_id')
    return html.format(hostname=socket.gethostname(), job_id=job_id)
