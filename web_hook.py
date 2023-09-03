from flask import Flask, request, jsonify

import git

repo = git.Repo("./")
origin = repo.remote(name='origin')
origin.pull()

# app = Flask(__name__)

# @app.route('/webhook', methods=['POST'])
# def handle_webhook():
#     data = request.json
#     # You can add more processing logic here, like saving the data to a database, etc.
#     return jsonify({'status': 'success'}), 200


# if __name__ == '__main__':
#     app.run(debug=True, port=5000)