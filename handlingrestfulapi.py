# HOW TO ACCESS RESTFUL API
# to open the restful api url
from urllib.request import urlopen
# the restful api will give us JSON data
# which needs to be converted into list of dictionary in python
import json
# we want to write the json data into a csv file
import csv

# Restful URL
url = "https://jsonplaceholder.typicode.com/posts"
response = urlopen(url)
data = response.read()
# print(type(data), data) # '["apple", "orange", "mango"]'
# now what we got is a string data

# We don't want bytes array we want list of dictionaries
url = "https://jsonplaceholder.typicode.com/posts"
response = urlopen(url)
data = json.loads(response.read())
for post in data:
    print("Post Id:", post["id"])
    print("User Id:", post["userId"])
    print("Title:", post["title"])
    print("Body:", post["body"])

# Let us write it into CSV file
url = "https://jsonplaceholder.typicode.com/posts"
response = urlopen(url)
data = json.loads(response.read())
try:
    with open("jsonplaceholder.csv", "wt", newline='') as handler:
        csv_writer = csv.writer(handler, delimiter="|")
        for post in data:
            id, userId, title, body = post.values()
            body = body.replace("\n", " ").replace("\r", "")
            csv_writer.writerow([id, userId, title, body])
except Exception as e:
    print("Something went wrong", e)
