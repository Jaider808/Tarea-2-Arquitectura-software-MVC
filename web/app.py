from past.builtins import raw_input

from logic.model import Person
import view
from view import app


def show_all():
    # gets list of all Person objects
    people_in_db = Person.get_all()
    # calls view
    print(Person.get_diccionary())
    return view.show_all_view(people_in_db)


def start():
    view.start_view()
    input_data = raw_input()
    if input_data == 'y':
        return show_all()
    else:
        return view.end_view()


if __name__ == "__main__":
    # running controller function
    start()
    app.run()
