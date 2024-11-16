import json

person = {"animal": "cat", "car": "toyota", "title": ["programmer", "engineer"], "hascar": True}

personJSON = json.dumps(person, indent= 4, sort_keys=True) #ENCODING OR SERIALIZATION,I.E CONVERTING PYTHON TO JSON
#print(personJSON)

#CREATING A FILE OF THE PERSON JSON OBJECT 

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4) 

#converting from json to python is called decoding or deserialization

person = json.loads(personJSON)
#print(person)

#CREATING A FILE OF THE PERSON PYTHON DICT
with open('person.json', 'r') as file:
    json.load(file)
    #print(person)


#CREATING A CUSTOM CLASS
class User:

    def __init__(self,name,age):
        self.name = name
        self.age = age

user = User("leo", 14)

def encode_user(o):
    if isinstance(o, User):
        return{'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        return TypeError('Object of type User is not JSON serializable')

#encoding
userJSON = json.dumps(user, default=encode_user)
print(userJSON)

#decoding
user = json.loads(userJSON)
print(type(user))  