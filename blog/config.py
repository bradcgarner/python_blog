import os
class DevelopmentConfig(object):
  SQLALCHEMY_DATABASE_URI = 'postgresql://ubuntu:thinkful@localhost:5432/blogful'
  DEBUG = True

# You use this class to contain the configuration variables which control the Flask app. You tell Flask to use its debug mode to help you track down any errors in your application, and set the location of your database. Note that you might find that PostgreSQL isn't running; if you see errors referring to port 5432 and "connection refused", execute sudo service postgresql start. Section 2.1.3 has further information about this, if you aren't sure.