from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Handle form submission
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    return f"<h1>Hello, {name}!</h1><a href='/'>Go Back</a>"

if __name__ == "__main__":
    app.run(debug=True)
