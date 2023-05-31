#!/usr/bin/python3
'''
Entrypoint for the visualization package.
'''
import ast
import codecs
import os
import sys

import pandas as pd
import json
# import yaml

from visualization import (generate_salary_estimate_plot, plot_salary_estimate, 
                           plot_box_adjusted_by_state, plot_average_rating_by_state,
                           plot_average_rating_by_industry, plot_average_salary_by_state,
                           plot_average_salary_by_industry, plot_average_adjusted_salary_by_state,
                           plot_average_adjusted_salary_by_industry)

# def print_output(data: dict):
#     """
#     Creates a marked section in the standard output
#     of the container in order for Brane to isolate the result.

#     Parameters
#     ----------
#     data: `dict`
#     Any valid Python dictionary that is YAML serializable.
#     """
#     print("--> START CAPTURE")
#     print(yaml.dump(data))
#     print("--> END CAPTURE")

def visualization_action(
    filepath_data_analyst_jobs: str,
) -> int:
    """
    Create an Html that contains all the plots based on the test
    and submission datasets.

    Parameters
    ----------
    filepath_test_dataset: `str`
    CSV file containing the test dataset.

    filepath_sub_dataset: `str`
    CSV file containing the submission dataset.

    filepath_bigrams_dataset: `str`
    CSV file containing the bigrams information dataset.
    filepath_train_dataset: `str`
    CSV file containing the training dataset.

    Returns
    -------
    `int` Error code.
    """
    # print("Visualization action")
    data_analyst_jobs = pd.read_csv(filepath_data_analyst_jobs,
                           converters={"tokens": ast.literal_eval})


    salary_estimate_img = plot_salary_estimate(data_analyst_jobs)
    adjusted_salary_img = plot_box_adjusted_by_state(data_analyst_jobs)
    average_rating_by_state_img = plot_average_rating_by_state(data_analyst_jobs)
    average_rating_by_industry_img = plot_average_rating_by_industry(data_analyst_jobs)
    average_salary_by_state_img = plot_average_salary_by_state(data_analyst_jobs)
    average_salary_by_industry_img = plot_average_salary_by_industry(data_analyst_jobs)
    average_adjusted_salary_by_state_img = plot_average_adjusted_salary_by_state(data_analyst_jobs)
    average_adjusted_salary_by_industry_img = plot_average_adjusted_salary_by_industry(data_analyst_jobs)
    template_html = codecs.open("packages/visualization/result.html", "r", "utf-8")

    result = template_html.read().format(
        salary_estimate=salary_estimate_img,
        adjusted_by_state=adjusted_salary_img,
        average_rating_by_state=average_rating_by_state_img,
        average_rating_by_industry=average_rating_by_industry_img,
        average_salary_by_state=average_salary_by_state_img,
        average_salary_by_industry=average_salary_by_industry_img,
        average_adjusted_salary_by_state=average_adjusted_salary_by_state_img,
        average_adjusted_salary_by_industry=average_adjusted_salary_by_industry_img)

    try:
        with open("packages/visualization/result.html", "w") as f:
            f.write(result)
        return "packages/visualization/result.html"
    except IOError as e:
        return ""


def main():
    command = sys.argv[1]

    if command == "visualization_action":
        filepath_data_analyst_jobs = f"data/jobs/data/cleaned_data.csv"

        output = visualization_action(
            filepath_data_analyst_jobs)
        # print_output({"output": output})
        return

    if command == "generate_prediction_plot":
        filepath_data_analyst_jobs = f"{json.loads(os.environ['FILEPATH'])}/cleaned_data.csv"
        output = generate_salary_estimate_plot(
            filepath_data_analyst_jobs)
        # print_output({"output": output})
        return
    
if __name__ == '__main__':
    main()
