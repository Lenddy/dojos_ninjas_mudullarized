from flask import Flask, session
app = Flask(__name__)
app.secret_key = "secret"
db = "dojos_ninjas_schema"