from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for users
users = []

# Home route
@app.route('/')
def home():
    return "Flask REST API is running!"

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET single user
@app.route('/users/<int:index>', methods=['GET'])
def get_user(index):
    if index < len(users):
        return jsonify(users[index]), 200
    return jsonify({"error": "User not found"}), 404

# POST (Add new user)
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    users.append(data)
    return jsonify({
        "message": "User added successfully",
        "user": data
    }), 201

# PUT (Update user)
@app.route('/users/<int:index>', methods=['PUT'])
def update_user(index):
    if index < len(users):
        data = request.json
        users[index] = data
        return jsonify({
            "message": "User updated successfully",
            "user": data
        }), 200
    
    return jsonify({"error": "User not found"}), 404

# DELETE user
@app.route('/users/<int:index>', methods=['DELETE'])
def delete_user(index):
    if index < len(users):
        deleted_user = users.pop(index)
        return jsonify({
            "message": "User deleted successfully",
            "user": deleted_user
        }), 200
    
    return jsonify({"error": "User not found"}), 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)