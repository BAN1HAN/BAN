from flask import Flask, render_template

app = Flask(name)

@app.route('/')
def home():
    return 'مرحبا بك في موقع التحديات!'

@app.route('/admin')
def admin():
    return render_template('admin.html')

if name == 'main':
    app.run(host='0.0.0.0', port=10000)
