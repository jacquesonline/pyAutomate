#!/usr/bin/env python3
import os
import requests
import sys
import csv


def build_feedback(filename):
    print(filename)
#     """Populate a dictionary with name/email pairs for easy lookup."""
#     feedback = {}
#     with open(filename) as csvfile:
#         lines = csv.reader(csvfile, delimiter=',')
#         for row in lines:
#             name = str(row[0].lower())
#             email_dict[name] = row[1]
# feedback = {"title": "Test",
#             "name": "Jack I.",
#             "date": "2021-09-01",
#             "feedback": "Good time to test  "}
#     return feedback


def main():

    # path = "/data/feedback"
    path = "C:\\Users\\jcste\\googleAutomation\\pyWebService\data"

    for file in os.listdir(path):
        if not file.startswith('.'):
            # print(file)
            build_feedback(file)
            # response = requests.post(
            #     'http://34.66.203.174/feedback/', data=feedback)
            # response.raise_for_status()
            # print(response.text)
            # print(response.status_code)


if __name__ == "__main__":
    main()

# 1. You should now have a list that contains all of the feedback files from the path /data/feedback. Traverse over each file and, from the contents of these text files,
# create a dictionary by keeping title, name, date, and feedback as keys for the content value, respectively.
# 2. Now, you need to have a dictionary with keys and their respective values (content from feedback files). This will be uploaded through the Django REST API.
# 3. Use the Python requests module to post the dictionary to the company's website. Use the request.post() method to make a POST request to http://<corpweb-external-IP>/feedback.
#  Replace <corpweb-external-IP> with corpweb's external IP address.
# Make sure an error message isn't returned. You can print the status_code and text of the response objects to check out what's going on.
# You can also use the response status_code 201 for created success status response code that indicates the request has succeeded.
