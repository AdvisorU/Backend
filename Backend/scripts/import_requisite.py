# exec(open('Backend/scripts/import_requisite.py').read())

from Backend.models.course_model import Course, CourseCoRequisite, CoursePreRequisite, CoursePreRequisiteType

import json

with open('Backend/scripts/courses_data.json', 'r', encoding = 'utf-8') as f:
    courses = json.load(f)

    # courses = [
    #     {
    #         "course_tag": "CS",
    #         "course_number": "4180",
    #         "course_name": "Reinforcement Learning",
    #         "credit_hours": "4",
    #         "prerequisites": "CS 3000 with a minimum grade of D- ;  (ECON 2350 with a minimum grade of D-  or  ENVR 2500 with a minimum grade of D-  or  MATH 3081 with a minimum grade of D-  or  PSYC 2320 with a minimum grade of D-  or  CS 2810 with a minimum grade of D- );  (MATH 2331 with a minimum grade of D-  or  CS 2810 with a minimum grade of D- )",
    #         "corequisites": [],
    #         "attributes": [],
    #         "description": "Introduces reinforcement learning and the Markov decision process (MDP) framework. Covers methods for planning and learning in MDPs such as dynamic programming, model-based methods, and model-free methods. Examines commonly used representations including deep-learning representations. Students are expected to have a working knowledge of probability, to complete programming assignments, and to complete a course project that applies some form of reinforcement learning to a problem of interest."
    #     }
    # ]

    missing_courses = []

    for course in courses:
        print('Creating course: ', course['course_tag'], course['course_number'])

        course_instance = Course.objects.get(major = course['course_tag'], number = course['course_number'])

        # create course's co-requisites
        for co_requisite in course['corequisites']:
            co_requisite_parts = co_requisite.split(' ')
            print('Co-requisite: ', co_requisite_parts)

            co_requisite_instance = Course.objects.get(major = co_requisite_parts[0], number = co_requisite_parts[1])

            # check if co-requisite course exists
            if not co_requisite_instance:
                print('Co-requisite not found: ', co_requisite)
                missing_courses.append([
                    co_requisite_parts[0],
                    co_requisite_parts[1]
                ])
                continue
            
            CourseCoRequisite.objects.create(
                course = course_instance, 
                co_requisite = co_requisite_instance
            )

        # create course's pre-requisites
        if course['prerequisites'] != '':
            prerequisites = course['prerequisites'].split(';')
            for prerequisite in prerequisites:
                prerequisite = prerequisite.strip()

                if prerequisite == '':
                    continue

                # check if prerequisite is a group
                if prerequisite[0] == '(' and prerequisite[-1] == ')':
                    parent_pre_requisite_instance = CoursePreRequisite.objects.create(
                        course = course_instance, 
                        type = CoursePreRequisiteType.GROUP
                    )

                    # remove the brackets
                    prerequisite = prerequisite[1:-1]

                    # split the group into individual prerequisites
                    prerequisite_parts = prerequisite.split('or')

                    for i in range(len(prerequisite_parts)):
                        prerequisite_parts[i] = prerequisite_parts[i].strip().split(' ', 2)

                        print('Course in group: ', prerequisite_parts[i])

                        # check if prerequisite course exists
                        prerequisite_instances = Course.objects.filter(major = prerequisite_parts[i][0], number = prerequisite_parts[i][1])

                        if not prerequisite_instances.exists():
                            print('Prerequisite not found: ', prerequisite_parts[i])
                            missing_courses.append([
                                prerequisite_parts[i][0],
                                prerequisite_parts[i][1]
                            ])
                            continue
                        
                        if len(prerequisite_parts[i]) == 3:
                            minimum_grade = prerequisite_parts[i][2].split('with a minimum grade of ')[1]
                            CoursePreRequisite.objects.create(
                                type = CoursePreRequisiteType.COURSE, 
                                parent_pre_requisite = parent_pre_requisite_instance, 
                                pre_requisite = prerequisite_instances.first(), 
                                minimum_grade = minimum_grade
                            )
                        else:
                            CoursePreRequisite.objects.create(
                                type = CoursePreRequisiteType.COURSE, 
                                parent_pre_requisite = parent_pre_requisite_instance, 
                                pre_requisite = prerequisite_instances.first()
                            )
                else:
                    # split the prerequisite into major and number
                    prerequisite_parts = prerequisite.split(' ', 2)

                    print('Course: ', prerequisite_parts)

                    # check if prerequisite course exists
                    prerequisite_instances = Course.objects.filter(major = prerequisite_parts[0], number = prerequisite_parts[1])

                    if not prerequisite_instances.exists():
                        print('Prerequisite not found: ', prerequisite)
                        missing_courses.append([
                            course_instance.major, 
                            course_instance.number
                        ])
                        continue
                    
                    if len(prerequisite_parts) == 3:
                        minimum_grade = prerequisite_parts[2].split('with a minimum grade of ')[1]
                        CoursePreRequisite.objects.create(
                            type = CoursePreRequisiteType.COURSE, 
                            course = course_instance, 
                            pre_requisite = prerequisite_instances.first(), 
                            minimum_grade = minimum_grade
                        )
                    else:
                        CoursePreRequisite.objects.create(
                            course = course_instance, 
                            type = CoursePreRequisiteType.COURSE, 
                            pre_requisite = prerequisite_instances.first()
                        )
    
    print('Missing courses: ', missing_courses)
    print('Done')
