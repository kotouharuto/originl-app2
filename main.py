from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
 title = 'FitLab'
 msg = 'あなたのフィットネスを少しでも楽しくします'

 return render_template('home.html', title=title, msg=msg)

app.run(port=8000, debug=True)