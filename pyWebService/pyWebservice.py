#!/usr/bin/env python3
import os
import requests
import sys
import csv
import time
start_time = time.time()
feedback = {}


def build_feedback(filename):

    idx = 0
    with open(filename) as csvfile:
        lines = csv.reader(csvfile)
        for row in lines:
            if idx == 0:
                idx += 1
                feedback["title"] = row[0]
            elif idx == 1:
                idx += 1
                feedback["name"] = row[0]
            elif idx == 2:
                idx += 1
                feedback["date"] = row[0]
            elif idx == 3:
                idx += 1
                feedback["feedback"] = row[0]

    return feedback


def main():

    # path = "/data/feedback"
    path = "C:\\Users\\jcste\\googleAutomation\\pyAutomate\\pyWebService\data\\"

    for file in os.listdir(path):
        if not file.startswith('.'):
            build_feedback(path + file)
            print(feedback)
            response = requests.post(
                'http://35.193.87.211/feedback/', data=feedback)
            response.raise_for_status()
            print(response.text)
            print(response.status_code)

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()

# list_of_files = os.listdir('/data/feedback')
# for file in list_of_files:
#         fp = open('/data/feedback/'+file)
#         data = fp.read()
#         data = data.split('\n')
#         dic = {"title":data[0], "name":data[1], "date":data[2], "feedback":data[3]}
#         response = requests.post('http://104.197.6.205/feedback/', json=dic)
#         print(response.status_code)

# feedback_dir = "/data/feedback/"
# website_dir = "/projects/corpweb/"
# url = "http://34.68.197.162/feedback/"
# feedback_dic = {}

# for feedback_file in os.listdir(feedback_dir):
#     with open(feedback_dir + feedback_file,"r") as f:
#         lines = f.readlines()
#         feedback_dic["title"] = lines[0]
#         feedback_dic["name"] = lines[1]
#         feedback_dic["date"] = lines[2]
#         feedback_dic["feedback"] = lines[3]
#         response = requests.post(url, data=feedback_dic)
#         print(response.status_code)
#         print(response.ok)
