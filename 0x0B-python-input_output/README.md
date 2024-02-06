


6. Create object from a JSON file
mandatory

Write a function that creates an Object from a “JSON file”:

    Prototype: def load_from_json_file(filename):
    You must use the with statement
    You don’t need to manage exceptions if the JSON string doesn’t represent an object.
    You don’t need to manage file permissions / exceptions.
    

        guillaume@ubuntu:~/0x0B$ cat my_fake.json
        {"is_active": true, 12 }
        guillaume@ubuntu:~/0x0B$ cat 6-main.py
        #!/usr/bin/python3
        load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
        
        filename = "my_list.json"
        my_list = load_from_json_file(filename)
        print(my_list)
        print(type(my_list))
        
        filename = "my_dict.json"
        my_dict = load_from_json_file(filename)
        print(my_dict)
        print(type(my_dict))
        
        try:
            filename = "my_set_doesnt_exist.json"
            my_set = load_from_json_file(filename)
            print(my_set)
            print(type(my_set))
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
        
        try:
            filename = "my_fake.json"
            my_fake = load_from_json_file(filename)
            print(my_fake)
            print(type(my_fake))
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
        
        guillaume@ubuntu:~/0x0B$ cat my_list.json ; echo ""
        [1, 2, 3]
        guillaume@ubuntu:~/0x0B$ cat my_dict.json ; echo ""
        {"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, "info": {"average": 3.14, "age": 36}, "is_active": true}
        guillaume@ubuntu:~/0x0B$ cat my_fake.json ; echo ""
        {"is_active": true, 12 }
        guillaume@ubuntu:~/0x0B$ ./6-main.py
        [1, 2, 3]
        <class 'list'>
        {'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'id': 12, 'places': ['San Francisco', 'Tokyo'], 'is_active': True}
        <class 'dict'>
        [FileNotFoundError] [Errno 2] No such file or directory: 'my_set_doesnt_exist.json'
        [ValueError] Expecting property name enclosed in double quotes: line 1 column 21 (char 20)



7) Write a script that adds all arguments to a Python list, and then save them to a file:

        You must use your function save_to_json_file from 5-save_to_json_file.py
        You must use your function load_from_json_file from 6-load_from_json_file.py
        The list must be saved as a JSON representation in a file named add_item.json
        If the file doesn’t exist, it should be created
        You don’t need to manage file permissions / exceptions.

        guillaume@ubuntu:~/0x0B$ cat add_item.json
        cat: add_item.json: No such file or directory
        guillaume@ubuntu:~/0x0B$ ./7-add_item.py
        guillaume@ubuntu:~/0x0B$ cat add_item.json ; echo ""
        []
        guillaume@ubuntu:~/0x0B$ ./7-add_item.py Best School
        guillaume@ubuntu:~/0x0B$ cat add_item.json ; echo ""
        ["Best", "School"]
        guillaume@ubuntu:~/0x0B$ ./7-add_item.py 89 Python C
        guillaume@ubuntu:~/0x0B$ cat add_item.json ; echo ""
        ["Best", "School", "89", "Python", "C"]
        guillaume@ubuntu:~/0x0B$ 


8. Class to JSON

Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

    Prototype: def class_to_json(obj):
    obj is an instance of a Class
    All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean
    You are not allowed to import any module



9. Student to JSON

Write a class Student that defines a student by:

    Public instance attributes:
        first_name
        last_name
        age
    Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
    Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)
    You are not allowed to import any module



10. Student to JSON with filter
mandatory

Write a class Student that defines a student by: (based on 9-student.py)

    Public instance attributes:
        first_name
        last_name
        age
    Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
    Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
        If attrs is a list of strings, only attribute names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
    You are not allowed to import any module



Write a class Student that defines a student by: (based on 10-student.py)

    Public instance attributes:
        first_name
        last_name
        age
    Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
    Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
        If attrs is a list of strings, only attributes name contain in this list must be retrieved.
        Otherwise, all attributes must be retrieved
    Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
        You can assume json will always be a dictionary
        A dictionary key will be the public attribute name
        A dictionary value will be the value of the public attribute
    You are not allowed to import any module

Now, you have a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allow us to rebuild an object based on this representation)


12. Pascal's Triangle

Technical interview preparation:

    You are not allowed to google anything
    Whiteboard first

Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

    Returns an empty list if n <= 0
    You can assume n will be always an integer
    You are not allowed to import any module

