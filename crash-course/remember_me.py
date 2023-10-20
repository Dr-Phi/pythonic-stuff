from pathlib import Path
import json

def get_stored_user(path):
    """Get stored user if available."""
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None

def get_new_user(path):
    """Prompt for a new user."""
    usn = input('What is your name? ').title()
    cnt = input('What is your country? ').title()
    prof = input('What is your profession? ').title()
    user = {
        'name': usn,
        'country': cnt,
        'profession': prof
    }
    contents = json.dumps(user)
    path.write_text(contents)
    return user

def greet_user():
    """Greet the user by name."""
    path = Path('user.json')
    user = get_stored_user(path)
    if user:
        right_account = input(f'Is {user["name"]} your name? (y/n) ').lower()
        if right_account == 'y':
            print(f'Welcome back, {user["profession"]} {user["name"]} from {user["country"]}!')
        else:
            user = get_new_user(path)
            print(f'we will remember you, when you come back, {user["name"]}')


greet_user()
