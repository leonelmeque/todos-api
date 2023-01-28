import random
import json


def id_generator(size=6):
    return ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "0123456789") for _ in range(size))


def write_to_json_db(json_data):
    with open('data.json', 'w') as outfile:
        outfile.write(json_data)


def read_json_db():
    with open('data.json') as json_file:
        data = json.load(json_file)
        print(data)
