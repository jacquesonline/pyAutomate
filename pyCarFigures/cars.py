#!/usr/bin/env python3
import json
import locale
import sys
import emails
import os
import reports


def load_data(filename):
    """Loads the contents of filename as a JSON file."""
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def format_car(car):
    """Given a car dictionary, returns a nicely formatted name."""
    return "{} {} ({})".format(
        car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
    """Analyzes the data, looking for maximums.

    Returns a list of lines that summarize the information.
    """
    max_revenue = {"revenue": 0}
    total_sales = {"sales": 0}
    popular_cars = {}

    for item in data:
        # Calculate the revenue generated by this model (price * total_sales)
        # We need to convert the price from "$1234.56" to 1234.56
        # print(item["car"]["car_make"])
        item_price = locale.atof(item["price"].strip("$"))
        item_revenue = item["total_sales"] * item_price
        if item_revenue > max_revenue["revenue"]:
            item["revenue"] = item_revenue
            max_revenue = item
            # print(max_revenue)
        # TODO: also handle max sales
        # Calculate the car model which had the most sales by completing the process_data method, and then appending a formatted string to the summary list in the below format:
        # "The {car model} had the most sales: {total sales}"
        item_total_sales = item["total_sales"]
        if item_total_sales > total_sales["sales"]:
            item["sales"] = item_total_sales
            total_sales = item
            # print(total_sales)
        # TODO: also handle most popular car_year
        # Calculate the most popular car_year across all car make/models (in other words, find the total count of cars with the car_year equal to 2005, equal to 2006, etc.
        # and then figure out the most popular year) by completing the process_data method, and append a formatted string to the summary list in the below format:
        # "The most popular year was {year} with {total sales in that year} sales."

        item_year = item["car"]["car_year"]

        if not item_year in popular_cars:
            popular_cars[item_year] = item_total_sales
        else:
            popular_cars[item_year] += item_total_sales

    sorted_total_years = sorted(popular_cars.items(), reverse=True)

    summary = [
        "The {} generated the most revenue: ${}".format(
            format_car(max_revenue["car"]), max_revenue["revenue"]),
        "The {} had the most sales: ${}".format(
            format_car(total_sales["car"]), total_sales["sales"]),
        "The most popular year was {} with {} sales.".format(
            sorted_total_years[0][0], sorted_total_years[0][1]),
    ]

    return summary


def cars_dict_to_table(car_data):
    """Turns the data in car_data into a list of lists."""
    table_data = [["ID", "Car", "Price", "Total Sales"]]
    for item in car_data:
        table_data.append([item["id"], format_car(
            item["car"]), item["price"], item["total_sales"]])
    return table_data


def main(argv):
    """Process the JSON data and generate a full report out of it."""
    data = load_data("car_sales.json")
    summary = process_data(data)
    # print(summary)
    table_data = cars_dict_to_table(data)
    # print(table_data)
    # TODO: turn this into a PDF report

    reports.generate("C:\\Users\\jcste\\googleAutomation\\pyAutomate\\pyCarFigures\\cars.pdf", "A Summary of Cars",
                     "This is summary of the cars.", table_data)

    # reports.generate("/tmp/cars.pdf", "A Summary of Cars",
    #                  "This is summary of the cars.", table_data)

    # TODO: send the PDF report as an email attachment
    # sender = "sender@example.com"
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Sales summary for last month"
    body = str(summary)
    print(body)

    # message = emails.generate(sender, receiver, subject, body, "/tmp/cars.pdf")
    message = emails.generate(sender, receiver, subject, body,
                              "C:\\Users\\jcste\\googleAutomation\\pyAutomate\\pyCarFigures\\cars.pdf")
    # emails.send(message)


if __name__ == "__main__":
    main(sys.argv)

# Optional challenge
# As optional challenges, you could try some of the following functionalities:

# Sort the list of cars in the PDF by total sales.

# Create a pie chart for the total sales of each car made.

# Create a bar chart showing total sales for the top 10 best selling vehicles using the ReportLab Diagra library.
# Put the vehicle name on the X-axis and total revenue (remember, price * total sales!) along the Y-axis.
