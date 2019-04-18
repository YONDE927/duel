from flask import Flask , render_template, redirect, request
import sqlite3
import bt

app = Flask(__name__)

bt.create_db()

@app.route('/')
def index():
    data = bt.load_db()
    lists= []
    for i in data:
        seg = {}
        seg["id"] =i[0]
        seg["he"] = i[1]
        seg["she"] = i[2]
        seg["contract"] = i[3]
        lists.append(seg)
    return render_template('index.html',lists=lists)

@app.route('/added', methods=['POST'])
def add():
    he= request.form['he']
    she= request.form['she']
    text= request.form['contract']
    data=(he,she,text)
    bt.insert(data)
    return redirect('/')

@app.route('/deleted',methods=['POST'])
def fname():
    id = request.form['id']
    bt.delete(id)
    return redirect('/')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
