from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Handle form submission
@app.route("/submit", methods=["POST"])
def submit():
    try:
        name = request.form.get("name")
        if not name:  # Handle empty input
            return (
                "<h1>Error: Name cannot be empty!</h1><a href='/'>Go Back</a>",
                400,
            )
        return render_template("greet.html", name=name)
    except Exception as e:
        return f"<h1>Something went wrong: {e}</h1><a href='/'>Go Back</a>", 500

# 404 Error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    # Ensure app runs on 0.0.0.0 for container environments
    app.run(host="0.0.0.0", port=5000, debug=True)
