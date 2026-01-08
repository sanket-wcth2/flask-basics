"""
Part 6: Homework - Personal To-Do List App
==========================================
See Instruction.md for full requirements.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Sample data with due dates
TASKS = [
    {'id': 1, 'title': 'Learn Flask', 'status': 'In Progress', 'priority': 'High', 'due_date': '2024-12-31'},
    {'id': 2, 'title': 'Build To-Do App', 'status': 'In Progress', 'priority': 'Medium', 'due_date': '2024-12-25'},
    {'id': 3, 'title': 'Push to GitHub', 'status': 'Completed', 'priority': 'Medium', 'due_date': '2024-11-30'},
]

def get_next_id():
    return max([task['id'] for task in TASKS], default=0) + 1

@app.route('/')
def index():
    return render_template('index.html', tasks=TASKS)


@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        new_task = {
            'id': get_next_id(),
            'title': request.form['title'],
            'status': request.form['status'],
            'priority': request.form['priority'],
            'due_date': request.form.get('due_date', '')
        }
        TASKS.append(new_task)
        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/task/<int:id>')
def task_detail(id):
    task = next((t for t in TASKS if t['id'] == id), None)
    return render_template('task.html', task=task)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    task = next((t for t in TASKS if t['id'] == id), None)
    
    if not task:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        task['title'] = request.form['title']
        task['status'] = request.form['status']
        task['priority'] = request.form['priority']
        task['due_date'] = request.form.get('due_date', '')
        return redirect(url_for('task_detail', id=id))
    
    return render_template('edit.html', task=task)


@app.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    task = next((t for t in TASKS if t['id'] == id), None)
    
    if task:
        TASKS.remove(task)
    
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)