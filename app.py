from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = []
task_id_counter = 1

def find_task(task_id):
    return next((task for task in tasks if task['id'] == task_id), None)

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the To-Do List API! Use /tasks to interact.'}), 200

@app.route('/tasks', methods=['POST'])
def add_task():
    global task_id_counter
    data = request.get_json()
    if not data or 'title' not in data or not isinstance(data['title'], str):
        return jsonify({'error': 'Invalid input, title is required and must be a string'}), 400
    
    task = {
        'id': task_id_counter,
        'title': data['title'],
        'completed': data.get('completed', False)
    }
    tasks.append(task)
    task_id_counter += 1
    return jsonify({'message': 'Task added successfully', 'task': task}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks}), 200

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = find_task(task_id)
    
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    if 'title' in data and not isinstance(data['title'], str):
        return jsonify({'error': 'Invalid input, title must be a string'}), 400
    
    task['title'] = data.get('title', task['title'])
    task['completed'] = data.get('completed', task['completed'])
    return jsonify({'message': 'Task updated successfully', 'task': task}), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = find_task(task_id)
    
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'message': 'Task deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)