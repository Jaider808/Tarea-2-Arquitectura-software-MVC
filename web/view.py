from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request
from logic.model import Person

app = Flask(__name__)
bootstrap = Bootstrap(app)


def show_all_view(data: list):
    print('In our db we have %i users. Here they are:' % len(data))
    for item in data:
        print(item.print_name(), item.id_person)


def start_view():
    print('MVC - the simplest example')
    print('Do you want to see everyone in my db?[y/n]')


def end_view():
    print('Goodbye!')


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)


@app.route('/person_update/<id_person>')
def person_update(id_person):
    for person in model:
        if person.id_person == id_person:
            edit_person = person
            return render_template('person_update.html', value=edit_person)
    return render_template('404.html')


@app.route('/person_edit', methods=['POST'])
def person_edit():
    return render_template('person_detail.html', value='msg')


@app.route('/person_delete/<id_person>', methods=['GET'])
def person_delete(id_person):
    Person.delete_person(id_person)
    return render_template('person_detail.html', value=id_person)


@app.route('/people')
def people():
    # Unico ruta que se que funciona
    data = [(i.id_person, i.first_name, i.last_name) for i in Person.get_all()]
    print(data)
    return render_template('people.html', value=data)
