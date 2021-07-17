"""
"""
import csv
import os.path

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def load_start_page(page_name):
    return render_template(page_name)


def write_to_database(data):
    """
    Saves the data from the contact form to a txt file.
    """
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message} ')


def write_to_database_csv(data):
    """
    Saves the data from the contact form to a csv file.
    """
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=(','), quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_database_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'The information didn\'t save.'
    else:
        return 'Something went wrong....'


#
#
# # Each route is used for different hyper-link address.
# @app.route('/about.html')
# def about_us():
#     return render_template('about.html')
#
#
# @app.route('/works.html')
# def work():
#     return render_template('works.html')
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
#
# @app.route('/components.html')
# def components():
#     return render_template('components.html')
