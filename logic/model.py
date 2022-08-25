import json


class Person(object):

    def __init__(self, first_name=None, last_name=None, id_person=None):
        self._first_name = first_name
        self._last_name = last_name
        self._id_person = id_person

    # returns Person name, ex: John Doe
    def print_name(self) -> str:
        return "{0} {1}".format(self._first_name, self._last_name)

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, name: str) -> None:
        self._first_name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def id_person(self):
        return self._id_person

    @id_person.setter
    def id_person(self, id_person):
        self._id_person = id_person

    @classmethod
    # returns all people inside db.txt as list of Person objects
    def get_all(cls):
        result = list()
        with open('../logic/db.json') as json_file:
            data = json.load(json_file)
            for p in data['employees']:
                person = Person(p['first_name'], p['last_name'], p['id_employee'])
                result.append(person)
        return result

    @classmethod
    def delete_person(cls, id_person):
        with open('../logic/db.json') as json_file:
            data = json.load(json_file)
            for p in data['employees']:
                if p['id_employee'] == id_person:
                    data['employees'].remove(p)
                    break
            new_data = data
        updated = json.dumps(new_data)
        s = open('../logic/db.json', 'w')
        s.write(updated)
