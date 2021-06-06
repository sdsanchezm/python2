from flask import Flask, render_template, request
from contact import Contacts

app = Flask(__name__)

@app.route(r'/', methods=['GET'])
def contactBook():
    #return 'Hola Mundo 3!'
    return render_template('contact_book.html')

@app.route(r'/add',methods=['GET', 'POST'])
def add_contact():

    if request.form:
        contact = Contact(name=request.form.get('name'),
                          phone=request.form.get('phone'),
                          email=request.form.get('email'))

        contact.put()

        print(request.form.get('name'))
        print(request.form.get('email'))
        print(request.form.get('phone'))

    return render_template('add_contact.html')

if __name__ == '__main__':
    app.run()