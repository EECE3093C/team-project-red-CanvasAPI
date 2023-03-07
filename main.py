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


class CanvasAPI(object):
    def __init__(self, API_KEY, API_URL):
        # API URL
        self.canvas = Canvas(API_URL, API_KEY)
        self.user = self.canvas.get_current_user()
    
    def get_courses(self):
        # Get a paginated list of courses
        course_list = self.user.get_courses()
        courses = []
        # Loop through each page of the course list
        for course_page in course_list:
            # Find classes in current semester
            if "2231" in course_page.course_code:
                id = course_page.id
                courses.append(id)
        return courses
    
    def get_assignments(self):
        current_assignments = []
        for id in CanvasAPI.get_courses(self):
            course = self.canvas.get_course(id)
            # retrieve all assignments in the course with due dates included
            assignments = course.get_assignments(include=['due_dates'])
            # Iterate over assignments, selecting only the ones with due dates
            for assignment in assignments:
                if assignment.due_at:
                    x = [assignment.due_at, course.name, assignment.name]
                    current_assignments.append(x)
        sorted_assignments = sorted(current_assignments, key = lambda x: x[0]) # This is too slow
        
        return sorted_assignments
    
    def get_todo(self):
        todo = []
        for things in self.canvas.get_todo_items():
            x = [things.type, things.html_url]
            todo.append(x)
        return todo
    
    def get_all_calendar_events(self):
        calendar_events = []
        events = self.canvas.get_upcoming_events()
        for event in self.canvas.get_upcoming_events(excludes=['description']):
            x = [event]
            calendar_events.append(x)
        return calendar_events

if __name__ == '__main__':
   
    API_KEY = '1109~8XCwn02uDMRouJecaJILOnr17FPD16u67HxaPHYS6yhh4XVeJmF1y0mOrQOHy08f' # chloe's for testing
    API_URL = 'https://uc.instructure.com' # API URL

    chloe = CanvasAPI(API_KEY, API_URL)
    print(chloe.get_assignments())
    