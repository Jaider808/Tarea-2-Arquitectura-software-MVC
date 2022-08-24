import json


class Person(object):

    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    # returns Person name, ex: John Doe
    def name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    @classmethod
    # returns all people inside db.txt as list of Person objects
    def get_all(cls):
        result = list()
        with open('db.json') as json_file:
            data = json.load(json_file)
            for p in data['employees']:
                person = Person(p['first_name'], p['last_name'])
                result.append(person)
        return result
