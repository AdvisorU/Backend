# exec(open('Backend/scripts/import_courses_from_catalog.py').read())

from Backend.models.course_model import Course, NUPathAttribute, CourseNUPathAttribute

import json

NU_PATH_ATTRIBUTES = {
    'naturaldesignedworld': 1765232584108937216, 
    'creativeexpressinnov': 1765232584339623936, 
    'interpretingculture': 1765232584389955584, 
    'formalquantreasoning': 1765232584440287232, 
    'societiesinstitutions': 1765232584486424576, 
    'analyzingusingdata': 1765232584553533440, 
    'differencediversity': 1765232584595476480, 
    'ethicalreasoning': 1765232584645808128, 
    # All English Writing Courses(ENGW) are considered as WX
    'writingintensive': 1765232584691945472,
    'integrationexperience': 1765232584742277120, 
    'capstoneexperience': 1765232584792608768
}

with open('Backend/scripts/courses_data.json', 'r', encoding = 'utf-8') as f:
    courses = json.load(f)

    # courses = [
    #     {
    #         "course_tag": "CS",
    #         "course_number": "2510",
    #         "course_name": "Fundamentals of Computer Science 2",
    #         "credit_hours": "4",
    #         "prerequisites": "CS 2500",
    #         "corequisites": [
    #             "CS 2511"
    #         ],
    #         "attributes": [
    #             "NUpath Analyzing/Using Data",
    #             "NUpath Natural/Designed World"
    #         ],
    #         "description": "Continues CS 2500. Examines object-oriented programming and associated algorithms using more complex data structures as the focus. Discusses nested structures and nonlinear structures including hash tables, trees, and graphs. Emphasizes abstraction, encapsulation, inheritance, polymorphism, recursion, and object-oriented design patterns. Applies these ideas to sample applications that illustrate the breadth of computer science."
    #     }
    # ]

    for course in courses:
        print('Creating course: ', course['course_tag'], course['course_number'])

        credit_hours = course['credit_hours']
        if '-' in credit_hours:
            credit_hours_parts = credit_hours.split('-')
            credit_hours = None
            credit_hours_min = int(credit_hours_parts[0])
            credit_hours_max = int(credit_hours_parts[1])
        elif ',' in credit_hours:
            credit_hours_parts = credit_hours.split(',')
            credit_hours = None
            credit_hours_min = int(credit_hours_parts[0])
            credit_hours_max = int(credit_hours_parts[1])
        else:
            credit_hours = int(credit_hours)
            credit_hours_min = None
            credit_hours_max = None

        # create course
        course_instance = Course.objects.create(
            major = course['course_tag'], 
            number = course['course_number'], 
            name = course['course_name'], 
            description = course['description'], 
            credit_hours = credit_hours,
            credit_hours_min = credit_hours_min,
            credit_hours_max = credit_hours_max
        )

        print('Course created: ', course_instance)

        # create course's NUPathAttributes
        for attribute in course['attributes']:
            attribute_instance = NUPathAttribute.objects.get(id = NU_PATH_ATTRIBUTES[attribute.replace('NUpath', '').replace('/', '').replace(' ', '').lower()])
            
            # check if attribute exists
            if not attribute_instance:
                print('Attribute not found: ', attribute)
                exit()
            
            CourseNUPathAttribute.objects.create(
                course = course_instance, 
                attribute = attribute_instance
            )
