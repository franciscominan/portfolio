from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def info_file(data):
	with open('database.txt', 'a') as data_base:
		name = data['name']
		email = data['email']
		subject = data['subject']
		message = data['message']
		data_base.write('')
		file = data_base.write(f'\nName: {name} \nEmail: {email} \nSubject: {subject} \nMessage: {message}')
		data_base.write('')


def info_file_csv(data):
	with open('database.csv', 'a') as data_base1:
		name = data['name']
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(data_base1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([name,email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form_csv():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			info_file_csv(data)
			return redirect('index.html')
		except:
			return 'Did not save to database.'

	else:
		return 'something went wrong.'

