# imports
from canvasapi import Canvas
from canvasapi.canvas_object import CanvasObject
from canvasapi.exceptions import CanvasException, RequiredFieldMissing
from canvasapi.calendar_event import CalendarEvent
from canvasapi.grade_change_log import GradeChangeEvent
from canvasapi.paginated_list import PaginatedList
from canvasapi.peer_review import PeerReview
from canvasapi.progress import Progress
from canvasapi.submission import Submission
from canvasapi.upload import FileOrPathLike, Uploader
from canvasapi.user import User, UserDisplay
from canvasapi.util import combine_kwargs, obj_or_id

# API URL
API_URL = 'https://uc.instructure.com'

# User input for API Key
API_KEY = '1109~8XCwn02uDMRouJecaJILOnr17FPD16u67HxaPHYS6yhh4XVeJmF1y0mOrQOHy08f' # chloe's for testing
''' API_KEY = input("Enter your API key for canvas: ")'''

# Initializing canvas object
canvas = Canvas(API_URL, API_KEY)

# Initializing canvas user
user = canvas.get_current_user()
print("Logged in as: ", user.name)

# Get a paginated list of courses
course_list = user.get_courses()
current_courses = []

# Loop through each page of the course list
for course_page in course_list:
    # Find classes in current semester
    if "2231" in course_page.course_code:
        id = course_page.id
        current_courses.append(id)

# Get Current Assignments
current_assignments = []

for id in current_courses:
    course = canvas.get_course(id)
    # retrieve all assignments in the course with due dates included
    assignments = course.get_assignments(include=['due_dates'])
    # Iterate over assignments, selecting only the ones with due dates
    for assignment in assignments:
        if assignment.due_at:
            x = [assignment.due_at, course.name, assignment.name]
            current_assignments.append(x)
sorted_assignments = sorted(current_assignments, key = lambda x: x[0]) # This is too slow

## to view assignments 
""" for assignment in sorted_assignments:
    print(assignment[0], assignment[1], assignment[2]) """

events = canvas.get_calendar_events()
print('x')
for event in events:
    print('test')    

