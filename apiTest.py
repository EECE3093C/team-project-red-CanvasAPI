# imports
from canvasapi import Canvas
from canvasapi.todo import Todo #imports to do list for specific courses 
from canvasapi.canvas_object import CanvasObject  
from canvasapi.util import( #Probably do not need all of these can go through and delete excess info
    combine_kwargs,
    file_or_path,
    is_multivalued,
    normalize_bool,
    obj_or_id,
    obj_or_str,
)

# API URL
API_URL = 'https://uc.instructure.com'
# User input for API Key
API_KEY = '1109~8XCwn02uDMRouJecaJILOnr17FPD16u67HxaPHYS6yhh4XVeJmF1y0mOrQOHy08f' # chloe's for testing

canvas = Canvas(API_URL, API_KEY)
user = canvas.get_current_user()

# Get the default calendar for the user
courses = user.get_courses()
for course in courses:
    print(course)
    
# the canvas API class for getting the calendar events, don't want to do autoclass
class canvasapi.calendar_event.CalendarEvent(canvasapi.requester.Requester, dict) 

# Here is the requester class for the calendar events, don't want to do autoclass
class canvasapi.requester.Requester('https://uc.instructure.com','1109~8XCwn02uDMRouJecaJILOnr17FPD16u67HxaPHYS6yhh4XVeJmF1y0mOrQOHy08f')  

# Here is the API class for getting the assignments
def get_todo_items(self, **kwargs):
        """
        Returns the current user's course-specific todo items.
        :calls: `GET /api/v1/courses/:course_id/todo \
        <https://canvas.instructure.com/doc/api/courses.html#method.courses.todo_items>`_
        :rtype: :class:`canvasapi.paginated_list.PaginatedList` of
            :class:`canvasapi.todo.Todo`
        """

        return PaginatedList(
            Todo,
            self._requester,
            "GET",
            "courses/{}/todo".format(self.id),
            _kwargs=combine_kwargs(**kwargs),
        )
      
class Course(CanvasObject):
    def __str__(self):
        return "{} {} ({})".format(self.course_code, self.name, self.id)

    def add_grading_standards(self, title, grading_scheme_entry, **kwargs):
        """
        Create a new grading standard for the course.
        :calls: `POST /api/v1/courses/:course_id/grading_standards \
        <https://canvas.instructure.com/doc/api/grading_standards.html#method.grading_standards_api.create>`_
        :param title: The title for the Grading Standard
        :type title: str
        :param grading_scheme: A list of dictionaries containing keys for "name" and "value"
        :type grading_scheme: list of dict
        :rtype: :class:`canvasapi.grading_standards.GradingStandard`
        """
        if not isinstance(grading_scheme_entry, list) or len(grading_scheme_entry) <= 0:
            raise ValueError("Param `grading_scheme_entry` must be a non-empty list.")

        for entry in grading_scheme_entry:
            if not isinstance(entry, dict):
                raise ValueError("grading_scheme_entry must consist of dictionaries.")
            if "name" not in entry or "value" not in entry:
                raise ValueError(
                    "Dictionaries with keys 'name' and 'value' are required."
                )
        kwargs["grading_scheme_entry"] = grading_scheme_entry

        response = self._requester.request(
            "POST",
            "courses/%s/grading_standards" % (self.id),
            title=title,
            _kwargs=combine_kwargs(**kwargs),
        )
        return GradingStandard(self._requester, response.json())
