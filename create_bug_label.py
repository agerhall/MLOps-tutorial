import os
from ghapi.all import GhApi

issue_num = int(os.getenv('NUMBER'))
owner, repo = os.getenv('REPO').split('/')

api = GhApi(owner=owner, repo=repo)
comments = api.issues.list_comments(issue_num)

for comment in comments:
  print(comment["body"])
  if comment["body"]=="\\bug":
    print("set label")
    
    api.issues.set_labels(issue_number=issue_num, labels=["bug"])
