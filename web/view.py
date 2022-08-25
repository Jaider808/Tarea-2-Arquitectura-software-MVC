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


def set_index():
    return render_template('index.html')


def set_person():
    return render_template('person.html')


def get_person_detail():
    id_employee = request.form['id_employee']
    first_name = request.form['first_name']
    last_name = request.form['last_name']

    Person.append_employee(id_employee, first_name, last_name)
    return render_template('person_detail.html', value="Was append")


def set_person_update(id_person):
    return render_template('person_update.html', value=Person.search_person(id_person))


def set_person_edit():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    id_employee = request.form['id_employee']
    Person.update_person(id_employee, first_name, last_name)
    return render_template('person_detail.html', value='Was update')


def set_person_delete(id_person):
    Person.delete_person(id_person)
    return render_template('person_detail.html', value=id_person)


def get_people():
    # Unico ruta que se que funciona
    data = [(i.id_person, i.first_name, i.last_name) for i in Person.get_all()]
    print(data)
    return render_template('people.html', value=data)
