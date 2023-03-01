# imports
from canvasapi import Canvas

import datetime
# API URL
API_URL = 'https://uc.instructure.com'
# User input for API Key
API_KEY = '1109~8XCwn02uDMRouJecaJILOnr17FPD16u67HxaPHYS6yhh4XVeJmF1y0mOrQOHy08f' # chloe's for testing

canvas = Canvas(API_URL, API_KEY)
user = canvas.get_current_user()
# Get the default calendar for the user
print(canvas.get_current_user())
todo_list = canvas.get_todo_items()
print(todo_list)
courses = user.get_courses()
for course in courses:
    print(course)