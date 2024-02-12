#!/usr/bin/python3
"""Define a the base of all models"""


class Base:
    """Creation de la class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convertit une liste de dictionnaires en une chaîne JSON"""
        import json

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Sauvegarde une liste d'instances dans un fichier JSON"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            file.write(cls.to_json_string([obj.to_dictionary()
                                           for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        import json

        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)
