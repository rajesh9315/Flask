from flask import Flask
app = Flask(_name_)
@app.route('/')
def hello():
    return 'hello world !'

if _name== "main_":
    app.run(host='0.0.0.0', port=80)
