import csv
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL


class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location_URL = StringField(
        "Location URL",
        validators=[
            DataRequired(),
            URL(require_tld=True, message="Please enter a valid URL."),
        ],
    )
    open_time = StringField("Open Time", validators=[DataRequired()])
    closing_time = StringField("Closing Time", validators=[DataRequired()])
    coffee_rating = SelectField(
        "Coffee Rating",
        choices=["✘", "☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],
        validators=[DataRequired()],
    )
    wifi_rating = SelectField(
        "WiFi Rating",
        choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
        validators=[DataRequired()],
    )
    power_outlets = SelectField(
        "Power Outlet Rating",
        choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
        validators=[DataRequired()],
    )
    submit = SubmitField("Submit")

    def write_to_csv(self) -> None:
        with open("cafe-data.csv", mode="a", newline="", encoding="utf-8") as f:
            current_data = csv.writer(f)
            current_data.writerow(
                [
                    self.cafe.data,
                    self.location_URL.data,
                    self.open_time.data,
                    self.closing_time.data,
                    self.coffee_rating.data,
                    self.wifi_rating.data,
                    self.power_outlets.data,
                ]
            )
