# exec(open('Backend/scripts/import_majors.py').read())

from Backend.models.major_model import Major

json = [
    {
        'name': 'Computer Science',
        'short_name': 'CS',
        'description': '''Computer science involves the application of theoretical concepts in the context of software development to the solution of problems that arise in almost every human endeavor. Computer science as a discipline draws its inspiration from mathematics, logic, science, and engineering. From these roots, computer science has fashioned paradigms for program structures, algorithms, data representations, efficient use of computational resources, robustness and security, and communication within computers and across networks. The ability to frame problems, select computational models, design program structures, and develop efficient algorithms is as important in computer science as software implementation skill. Computer science is concerned with bringing together all of the intellectual resources needed to enable the rapid and effective development of software to meet the needs of business, research, and end users.
The goal of the undergraduate program in computer science is to teach students the conceptual and practical skills that will enable them to contribute to the development of computational principles and to play a productive role in the software community. To that end, the undergraduate program focuses on the fundamentals of program design including object-oriented design, software development, computer organization, systems and networks, theory of computation, principles of languages, and advanced algorithms and data. The program also offers a variety of electives at the upper undergraduate and beginning graduate levels ranging from more theoretical courses to those that focus on important applications.'''
    }, 
    {
        'name': 'Computer Science, BSCS', 
        'short_name': 'BSCS',
        'description': 'The Bachelor of Science in Computer Science focuses on the fundamentals of program design, software development, computer organization, systems and networks, theories of computation, principles of languages, and advanced algorithms and data. '
    }, 
    {
        'name': 'Information Science',
        'short_name': 'IS',
        'description': ''
    }
]

for major in json:
    Major.objects.create(
        name = major['name'],
        short_name = major['short_name'],
        description = major['description']
    )
    
    print('Major created: ', major['name'])
