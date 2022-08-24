from past.builtins import raw_input

from model import Person
import view


def show_all():
    # gets list of all Person objects
    people_in_db = Person.get_all() 
    # calls view
    return view.show_all_view(people_in_db)


def start():
    view.start_view()
    input = raw_input()
    if input == 'y':
        return show_all()
    else:
        return view.end_view()


if __name__ == "__main__":
    # running controller function
    start()
