from past.builtins import raw_input

from logic.model import Person
import view
from view import app


def show_all():
    # gets list of all Person objects
    people_in_db = Person.get_all()
    # calls view
    return view.show_all_view(people_in_db)


def start():
    view.start_view()
    input_data = raw_input()
    if input_data == 'y':
        return show_all()
    else:
        return view.end_view()

@app.route("/")
def index():
    return view.set_index()


@app.route('/person', methods=['GET'])
def person():
    return view.set_person()


@app.route('/person_detail', methods=['POST'])
def person_detail():
    return view.get_person_detail()


@app.route('/person_update/<id_person>')
def person_update(id_person):
    return view.set_person_update(id_person)


@app.route('/person_edit', methods=['POST'])
def person_edit():
    return view.set_person_edit()

@app.route('/person_delete/<id_person>', methods=['GET'])
def person_delete(id_person):
    return view.set_person_delete(id_person)


@app.route('/people')
def people():
    return view.get_people()


if __name__ == "__main__":
    # running controller function
    start()
    app.run()
