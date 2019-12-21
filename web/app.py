from flask import Flask, render_template
import os

app = Flask(__name__)
 
 
@app.route('/')
def hello_whale():
    return render_template("whale_hello.html")

@app.route('/test')
def test_route():
    pwd = os.getcwd()
    files = os.listdir(pwd)
    files_str = ', '.join(files)
    return 'Hi there. Dir=%s. Files=%s' % (pwd, files_str)
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')