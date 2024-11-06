from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index()->None:
    return render_template("index.html",pagetitle="Student information")
    
if __name__=="__main__":
    app.run(debug=True)