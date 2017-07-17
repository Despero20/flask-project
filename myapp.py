from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def index():
        return render_template("index.html")

@app.route('/wheream')
def whereami():
        return "kdua" 

@app.route("/linux")
def linux():
       return render_template("linux1.html")
@app.route("/python")
def python():    
       return render_template("python.html")
if __name__ == '__main__':
        app.run(host="0.0.0.0") 
