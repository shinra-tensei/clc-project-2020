from flask import Flask
import math
app = Flask(__name__)

req_count = 0

@app.route('/')
def hello_world():
    req_count = req_count + 1
    return 'Hey, we have Flask in a Docker container!' + str(req_count)

@app.route('/calculate')
def calculate():
    phi = (1+math.sqrt(5))/5
    limit = 10000000
    n = 1250
    res = 0
    for i in range(limit):
        f = ((phi**n) - (-1/phi)**n)/math.sqrt(5)
        res += f
    return str(res)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')