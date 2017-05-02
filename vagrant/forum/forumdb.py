# "Database code" for the DB Forum.

import datetime

# POSTS = [("This is the first post.", datetime.datetime.now())]

## Database connection
DB = []

# Get posts from database.
def GetALLPosts():
  """Return all posts from the 'database', most recent first."""
  DB = psycopg2.connect("dbname=forum")
  posts = [{'content': str(row[1]),
  'time': str(row[0])} for row in DB]
  posts.sort(key=lambda row: row['time'], reverse = True)
  return posts
#  return reversed(POSTS)

# Add a post to the database.
def AddPost(content):
  """Add a post to the 'database' with the current timestamp."""
  t = time.strftime('%', time.localtime())
  DB.append((t, content))
 # POSTS.append((content, datetime.datetime.now()))


