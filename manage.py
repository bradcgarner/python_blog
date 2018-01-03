import os
from flask_script import Manager

from blog import app
from blog.database import session, Entry

manager = Manager(app) # this allows us to type $ python3 manage.py run to execute the command (filename, then function)

@manager.command
def run():
  port = int(os.environ.get('PORT', 8080))
  app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
  manager.run()

@manager.command
def seed():
  content = '''Lorem ipsum'''

  for i in range(25):
    entry = Entry(
      title='Test Entry #{}'.format(i),
      content=content
    )
    session.add(entry)
  session.commit()
