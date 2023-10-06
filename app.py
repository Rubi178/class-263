from flask import Flask, render_template, request
app=Flask(__name__)
@app.route("/")
def main():
    return render_template("index.html")
def math_operations():
    e=request.form["text"]
    o=request.form["operations"]
    result= "https://newton.now.sh/api/v2//" + o + "/" + e
    request.get(result).json()
if __name__=="__main__":
    app.run()