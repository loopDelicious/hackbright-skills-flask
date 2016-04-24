from flask import Flask, render_template, request
import jinja2

app = Flask(__name__)



@app.route("/")
def index_page():
    """Show an index page."""

    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")

@app.route("/application-form")
def display_application():
    """Displays application form fields."""

    return render_template("application-form.html")



@app.route("/application", methods=["POST"])
def show_response():
    """Submits user info as an application."""

    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    salary = request.form.get("salary")
    select = request.form.get("select")

    return render_template("application-response.html",
                            firstname=firstname,
                            lastname=lastname,
                            salary=salary,
                            select=select)


if __name__ == "__main__":
    app.run(debug=True)
