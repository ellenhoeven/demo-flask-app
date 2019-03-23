from flask import Flask, render_template, request, redirect
import os
import random
import numpy as np

CAT_FOLDER = os.path.join('static', 'img')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = CAT_FOLDER

email_addresses = []

@app.route('/')
def hello_world():
	author = "me"
	name = "ellen"
	return render_template('index.html', author=author, name=name)

@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    # dog_newsletter = request.form['dog_newsletter']
    # cat_newsletter = request.form['cat_newsletter']
    # print("The email address is '" + email + "'")
    # print("Newsletter chosen '" + dog_newsletter + cat_newsletter + "'")
    email_addresses.append(email)
    print(email_addresses)
    return redirect('/')

@app.route('/emails.html')
def emails():
    return render_template('emails.html', email_addresses=email_addresses)

@app.route('/catoftheday.html')
def random_cat():
	n_cats = 9
	idx = random.randint(0, n_cats)
	full_filename = os.path.join(app.config['UPLOAD_FOLDER'], str(idx) + '.gif')
	return render_template("catoftheday.html", user_image=full_filename)





if __name__ == '__main__':
    app.run()
