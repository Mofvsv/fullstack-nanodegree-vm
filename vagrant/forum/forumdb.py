# "Database code" for the DB Forum.

import psycopg2

# Get posts from database.
def GetAllPosts():
  DB = psycopg2.connect("dbname=forum")
  c = DB.cursor()
  c.execute("SELECT time, content FROM posts ORDER BY time DESC")
  posts =({'content': str(row[1], 'time' str(row[0])}
           for row in c.fetchall()0
  DB.close()
  return posts

# Add a post to the database.
def AddPost(content):
  DB = psycopg2.connect("dbname=forum")
  c = DB.cursor()
  c.execute("INSERT INTO posts(content) VALUES ('%s')" % content)
  DB.commit()
  DB.close()
  









##import datetime
# POSTS = [("This is the first post.", datetime.datetime.now())]
## Database connection
## DB = []
### Get posts from database.
##def GetALLPosts():
##  """Return all posts from the 'database', most recent first."""
##  posts = [{'content': str(row[1]),
##  'time': str(row[0])} for row in DB]
##  posts.sort(key=lambda row: row['time'], reverse = True)
##  return posts
##  return reversed(POSTS)
##
### Add a post to the database.
##def AddPost(content):
##  """Add a post to the 'database' with the current timestamp."""
##  t = time.strftime('%', time.localtime())
##  DB.append((t, content))
## # POSTS.append((content, datetime.datetime.now()))


