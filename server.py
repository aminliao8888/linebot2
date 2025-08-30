from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!哈囉!!"
    
@app.route("/abc")
def hello1():
    a = request.args.get('a')
    
    return jsonify({'result': str(a)})
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
