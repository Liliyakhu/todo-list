# ToDoList Project

**Todo list** is a simple ToDoList application implemented in Python/Django.


## Features
+ Add tasks with due dates and descriptions
+ Mark tasks as completed
+ Edit task details
+ Delete tasks

## Technologies Used
+ **Backend:** Python, Django
+ **Frontend:** HTML5, CSS3, JavaScript
+ **Database:** SQLite3

## Installation
### Prerequisites
1. Python 3.8 or higher
2. SQLite3

## Setup
1. Clone the repository:
```
git clone https://github.com/Liliyakhu/todo-list.git
cd todo-list
```
2. Create a virtual environment and install dependencies:
```
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```
3. Set up the database:
```
python manage.py makemigrations
python manage.py migrate
```
4. Create a superuser for admin access:
```
python manage.py createsuperuser
```
5. Run the development server:
```
python manage.py runserver
```
6. Open your browser and navigate to http://127.0.0.1:8000.


## Screenshots

### Home page:
![Screenshot from 2025-01-12 21-58-52](https://github.com/user-attachments/assets/6481fcbf-ef47-49c6-87dd-9071ca014613)
### Tags page:
![Screenshot from 2025-01-12 21-59-45](https://github.com/user-attachments/assets/fdf33e44-147b-4dba-8ef9-c04992200aef)
