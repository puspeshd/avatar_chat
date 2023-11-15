from flask import Flask, request, jsonify
import requests
import random
import string

app = Flask(__name__)

# DiceBear API endpoint
dicebear_api = 'https://avatars.dicebear.com/api/bottts/'

# Simple in-memory user store
users = {}


def generate_seed():
    return str(random.randint(1, 1000000))


def generate_random_username():
    return ''.join(random.choices(string.ascii_letters, k=8))


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username', generate_random_username())

    seed = generate_seed()
    avatar_url = f'{dicebear_api}{seed}.svg'

    users[username] = {'avatar_url': avatar_url, 'seed': seed}

    return jsonify({'username': username, 'avatar_url': avatar_url})


@app.route('/user/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({'username': username, 'avatar_url': user['avatar_url']})


if __name__ == '__main__':
    app.run(debug=True)
