"""
Part 3: Jinja2 Variables - Passing Data from Python to HTML
============================================================
How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    student_name = "Sanket"
    return render_template('index.html', name=student_name)  # Pass variable to template as {{ name }}


@app.route('/profile')
def profile():
    user_data = {
        'name': 'Sanket',
        'age': 21,
        'course': 'Web Development',
        'email': 'sanket@example.com',
        'city': 'Pune',
        'is_enrolled': True
    }
    return render_template('profile.html',  # Pass multiple variables to template
                           name=user_data['name'],
                           age=user_data['age'],
                           course=user_data['course'],
                           email=user_data['email'],
                           city=user_data['city'],
                           is_enrolled=user_data['is_enrolled'])


@app.route('/skills')
def skills():
    programming_skills = ['Python', 'HTML', 'CSS', 'JavaScript', 'Flask']
    return render_template('skills.html', skills=programming_skills)  # Pass list to loop through in template


@app.route('/grades')
def grades():
    student_grades = {
        'AI': 'A',
        'DBMS': 'B+',
        'DSA': 'A+',
        'ANN': 'A'
    }

    return render_template('grades.html', grades=student_grades)


if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# JINJA2 SYNTAX QUICK REFERENCE:
# =============================================================================
#
# {{ variable }}          - Output a variable
# {{ variable|upper }}    - Use a filter (uppercase)
# {{ variable|default('N/A') }} - Default value if variable is empty
#
# {% if condition %}      - If statement
#   ...
# {% endif %}
#
# {% for item in list %}  - For loop
#   {{ item }}
# {% endfor %}
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 3.1: Add more data                                                     #done
#   - Add more fields to the profile (email, city, etc.)
#   - Display them in profile.html
#
# Exercise 3.2: Conditional display                                                #done
#   - In profile.html, show "Enrolled" or "Not Enrolled" based on is_enrolled
#   - Use {% if is_enrolled %} ... {% else %} ... {% endif %}
#
# Exercise 3.3: Create a grades page                                               #done
#   - Create a new route /grades
#   - Pass a dictionary of subjects and grades
#   - Display them in a table using a for loop
#
# =============================================================================
