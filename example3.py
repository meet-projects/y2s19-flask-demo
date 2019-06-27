from flask import Flask, render_template
app = Flask(__name__)

# Flask app with basic template
@app.route('/')
def hello_world():
    return render_template("hello_with_css.html")

if __name__ == '__main__':
   app.run(debug = True)