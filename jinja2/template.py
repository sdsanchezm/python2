from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')
env = Environment(loader = file_loader)
template = env.get_template('template.davs')

user_post = [{'title': 'Title 1- Breakfast nice', 'author': 'Kraus'},
            {'title': 'Title 2- Pizza at noon', 'author':'Mark'}]

result = template.render({'user':'this is the user',
                          'user_id':'this is the user_id!',
                          'user_credential':'this is the user credential',
                          'user_number': '2121422142',
                          'good_day': True, #could be False as well
                          'user_post': user_post
                         })

with open('index.html','w') as index:
    index.write(result)
