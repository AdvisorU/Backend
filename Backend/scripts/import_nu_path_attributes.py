from Backend.models.course_model import NUPathAttribute

json = [
    {
        'name': 'Engaging with the Natural and Designed World', 
        'short_name': 'Natural and Designed World',
        'user_code': 'ND',
        'description': 'Students study and practice scientific investigation and/or engineering design in order to understand the natural world and to effect changes in it to meet human and societal needs and wants. They learn critical thinking and analytical problem solving; the biological, chemical, and/or physical principles that govern the natural world; and the efforts that underlie the origins, development, acceptance, and applications of those principles.', 
    }, 
    {
        'name': 'Exploring Creative Expression and Innovation', 
        'short_name': 'Creative Expression/Innovation', 
        'user_code': 'EI',
        'description': 'Students study and practice creative expression and innovation. They learn about traditions of creative expression and innovation in any of a number of modes (texts, image, sounds, design, etc.) and products (poems, paintings, prototypes, business plans, games, apps, medical devices and procedures, etc.) and develop their own creative processes and products as a means of seeing and experiencing the world in new ways and communicating those experiences to others.',
    }, 
    {
        'name': 'Interpreting Culture', 
        'short_name': 'Interpreting Culture', 
        'user_code': 'IC',
        'description': 'Students study and analyze cultural practices, artifacts, and texts (e.g., visual art, literature, theatrical performances, musical compositions, architectural structures). They learn critical reading and observation strategies and how traditions of theoretical, aesthetic, and/or literary criticism provide different lenses for the interpretation of cultural objects and practices.',
    }, 
    {
        'name': 'Conducting Formal and Quantitative Reasoning', 
        'short_name': 'Formal/Quantitative Reasoning', 
        'user_code': 'FQ',
        'description': 'Students study and practice systematic formal reasoning using either the symbolic languages of mathematics and logic or the combinations of text and symbols characteristic of computer software. They learn when and how to apply formal reasoning to particular problems and subject matters.',
    }, 
    {
        'name': 'Understanding Societies and Institutions', 
        'short_name': 'Societies and Institutions', 
        'user_code': 'SI',
        'description': 'Students study and practice social science, historical, and/or literary methods of inquiry and theories in order to understand human behavior and cultural, social, political, and economic institutions, systems, and processes. They learn theories of social behavior as they relate to phenomena such as globalization, social change, and civic sustainability.',
    }, 
    {
        'name': 'Analyzing and Using Data', 
        'short_name': 'Analyzing and Using Data', 
        'user_code': 'AD',
        'description': 'Students study and practice methods and tools of data analysis and use. Students learn about the structure and analysis of at least one type of data (e.g., numbers, texts, documents, web data, images, videos, sounds, maps) and acquire the skills to examine, evaluate, and critique such data, extract patterns, summarize features, create visualizations, and provide insight not obvious from the raw data itself. Students also learn to be sensitive to ethical concerns associated with data: security, privacy, confidentiality, and fairness.',
    }, 
    {
        'name': 'Engaging Differences and Diversity', 
        'short_name': 'Differences and Diversity', 
        'user_code': 'DD',
        'description': 'Students study and practice methods for recognizing and understanding human diversity of various kinds in global, local and organizational contexts. They learn theories and perspectives of human difference, civic sustainability and multiculturalism, how social arrangements shape and are shaped by difference, and the histories, cultures and interactions of diverse groups.',
    }, 
    {
        'name': 'Employing Ethical Reasoning', 
        'short_name': 'Ethical Reasoning', 
        'user_code': 'ER',
        'description': 'Students study and practice methods of analyzing and evaluating the moral dimensions of situations and conduct. They learn ethical theories and frameworks; explore how conceptions of morals and ethics shape interpretation of concepts such as justice, fairness, rights and responsibilities, virtue, and the good life; and apply these to personal, professional, social, political, historical or economic questions and situations.',
    }, 
    {
        'name': 'Writing Across Audiences and Genres', 
        'short_name': 'Writing Across Audiences/Genres', 
        'user_code': 'WX', # TODO: There are three user codes for this attribute. May support multiple user codes in one attribute in the future.
        'description': 'Students study and practice writing for multiple public, academic, and professional audiences and contexts. They learn to use writing strategies, conventions, genres, technologies, and modalities (e.g., text, sounds, image, video) to communicate effectively.',
    }, 
    {
        'name': 'Integrating Knowledge and Skills Through Experience', 
        'short_name': 'Integration of Experience', 
        'user_code': 'EX',
        'description': 'Students study and practice the principles and strategies of experiential learning. Through direct experience and reflection on that experience, they learn to recognize and articulate their knowledge and skills, to apply the knowledge and skills they learn in one context to another context, and to determine what knowledge and skills they need to develop to meet their goals.',
    }, 
    {
        'name': 'Demonstrating Thought and Action in a Capstone', 
        'short_name': 'Capstone Experience', 
        'user_code': 'CE',
        'description': 'Each student must take at least one course designated as a capstone experience.  Capstone courses may be designed for a specific degree program, for a department, or for a college.  The learning goals for a capstone will be developed by the unit that is designing the capstone.  Students must complete a capstone in their major.  In cases where a student has multiple majors (such as in a combined or double major), the units may specify in which major to take the capstone or may leave the choice to the student.',
    }, 
]

for item in json:
    NUPathAttribute.objects.create(**item)

print('NUPathAttributes imported')
