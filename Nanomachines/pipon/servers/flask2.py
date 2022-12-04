from flask import Flask, render_template
app = Flask(__name__)
@app.route('/echo/<think>')
def echo(think):
 return render_template('flask2.html', think=think)
app.run(port=9999, debug=True)