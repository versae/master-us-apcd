"""First hug API (local, command-line, and HTTP access)"""
import hug


api = hug.API(__name__)

@hug.cli()
@hug.get(examples='name=Timothy&age=26')
@hug.local()
def happy_birthday(name: hug.types.text, age: hug.types.number, hug_timer=3):
    """Says happy birthday to a user"""
    return {'message': 'Happy {0} Birthday {1}!'.format(age, name),
            'took': float(hug_timer)}


@hug.cli()
@hug.get()
@hug.local()
def happy_anniversary(name: hug.types.text, age: hug.types.number, hug_timer=3):
    """Says happy anniversary to a user"""
    return {'message': 'Happy {0} Anniversary {1}!'.format(age, name),
            'took': float(hug_timer)}

if __name__ == '__main__':
    api.cli()