import csv
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from cafe_form import CafeForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    my_form = CafeForm()
    if my_form.validate_on_submit():
        my_form.write_to_csv()
        return redirect(url_for("cafes"))
    return render_template("add.html", form=my_form)


@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline="", encoding="UTF-8") as csv_file:
        csv_data = csv.reader(csv_file)
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
