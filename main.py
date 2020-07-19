from flask import Flask, render_template, request
import csv

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


def write_csv(data):
    with open('email-database.csv', mode='a', newline='') as database:
        email = data["email"]
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email])


@app.route('/signup', methods=['POST'])
def sign_up():
    error = None
    if request.method == 'POST':
        html_data = request.form.to_dict()
        write_csv(html_data)
    else:
        return 'Something\'s gone horribly wrong!'
