from pathlib import Path
import json

def get_stored_number(path):
    if path.exists():
        content = path.read_text()
        number = json.loads(content)
        return number
    else:
        return None


def add_number(path):
    number = int(input('What is your favorite number? '))
    print('I will remember it for later!')
    contents = json.dumps(number)
    path.write_text(contents)
    return number

def read_number():
    path = Path('fav_number.json')
    number = get_stored_number(path)
    if number:
        print(f'I know your favorite number! It is: {number}')
    else:
        number = add_number(path)

read_number()
