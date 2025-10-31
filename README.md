# ![HR image](https://github.com/illusio666/employee_attrition_analysis/blob/main/hero.png)

## Employee Attrition Analysis

The following analysis looks at a total of 1400 employee records for 'Fallon Pharmaceuticals', some of whom have left the organisation. The intent is to improve our understanding of those departing employees, understand if there might be any common factors causing their departure, and to be able to predict future potential departures. This will allow the organisation to do two things:

- to address any underlying factors that have a significant relationship to employee departure, and
- identify those employees at highest risk of departure and focus on their retention as a priority.

## Project Objective 📊

The business has asked that the Data Analysis team review the data and identify actions that management may consider to improve staff retention. These recommendations should be clear and supported with easily-understood charts and visualisations for those team members who are not data analysts.

## Executive Summary

Key findings: of the 4 hypotheses, two are proven and two are rejected (see below). Of one of the rejected hypotheses, one has been proven to actually be the opposite (job 'stagnation' does not lead to attrition, short tenure employees are more likely to leave).

When applying machine learning to our data, we find that we can predict attrition with a 90% accuracy, to enable future prediction of employee attrition.

When we look at leaving employees, there are three key areas that stand out:

1) good pay rise but disengaged
2) young and mobile

- Additionally long commutes (independent of the two groups above).

For groups 1) and 2), tactics to improve engagement are suggested in the notebooks, including structured and agreed career paths, skills enhancements, improved managerial engagement and, for the 'young and mobile', improved team social engagement.

Actual areas would need to be validated with qualitiative feedback (employee surveys) as these are based on the limited dataset and 'possible' causes of job mobility.

For long commutes, while this doesn't help to predict attrition in our employee segmentation, it is nevertheless related to elevated attrition levels when commutes exceed 10 miles. So consideration should be given to reviewing the 'return to work' mandate with a priority for employees with a long commute.

## Hypotheses and validation approach

There are 4 hypotheses that the business has asked to be validated as part of this analysis:

1) Attrition is spread evenly across all departments, with no single department having a statistically-significant higher attrition.
2) Role stagnation contributes to employees leaving; average (mean) duration in current (or final) role is higher for those departing than the company average.
3) Younger employees are more likely to be 'job hoppers' and so hiring and retention needs to consider if this may be mitigated
4) Commute distances can impact attrition - those employees with longer to travel are more likely to leave.

These four hypotheses will be tested, to allow the business to develop actions plans to address any root causes.

Additionally, the data will be analysed to see if any other correlations can be found between employee attrition and other factors, either individually or combined, to allow the business to determine if there are other actions that may be beneficial.

Employees will then be clustered based on their risk profile to allow the business to tailor their retention approaches.

## Conclusions

### Hypothesis 1 - No department has greater attrition than the others

This hypothesis is rejected.

While sales and HR have similar attrition, Research & Development have a statistically significant lower attrition, so further qualitative research should be done to compare R&D staff sentiment to other depts.

### Hypothesis 2 - Job stagnation leads to attrition

This hypothesis is rejected.

Employees who leave the organisation have significantly shorter tenure both in role and in the company than those who have left. Recommendation for exit interviews to seek feedback on whether jobs met expectations for those who leave within 12months of starting.

### Hypothesis 3 - Attrition is greater for younger employees

This hypothesis is proven.

With the exception of potential retirees (relevant flag is not present in the data), attrition %s are higher in the 20-35yrs groups. It can also be seen that single employees are more likely to leave.

Perhaps we need a company-wide dating app?

### Hypothesis 4 - Commute distance has an impact on retention

This hypothesis is proven.

Employees with a commute of 10+ miles are more likely to leave and so return-to-work policies should be reviewed if retention is a priority.

---

## Approach

## Dataset Content & Overview 📁

This publicly-available  data set has been sourced from HuggingFace <https://huggingface.co/datasets/Redsmoothy/HR_Attrition>.

Data is also synthesised as part of the logistic attrition modelling due to the imbalace of Attrition to non-attrition staff.

## Data Preparation Summary 🧹

For the ETL notebook, the initial use of ydata-profiling indicated areas for data clean up and any 1:1 correlations between columns. This identified several data fields that could be dropped as they added no value to analysis (unique, constants).

In anticiation of future analysis, some numeric field that represented ordinal sequences were adapted accordingly and 'ratio' fields were added to give an indication of how pay, time in company and time in role related to each other in case that highlighted any themes during the ML modelling.

## Project Approach 🧠

To ensure a robust set of tasks, the 5 key stages of the activity (ETL, visualisations, ML, PowerBI dashboard, overall management) were broken down into key steps and sequenced across a 5 day period.

Those tasks were added to a CSV file in standard User Story format and allocated labels, milestones and an Assignee.

The User Story CSV was then uploaded to Github via a .py issues uploader (see csv-to-github-upload folder and credits for original creator).

Contingency time was allocated, to ensure there was leeway in the event unanticipated issues, with Day 5 tasks being minimal management tasks only.


## Main data analysis libraries

To conduct the analyses, the following libraries were used:

- pandas
- numpy
- ydata-profiling
- SciKit-Learn
- matplotlib
- seaborn
- plotly
- scipy, and
- imbalance-learn

## Analysis techniques used



## Dashboard design

## Unfixed bugs

There were no unfixed bugs.

## Conclusions & recommendations

## Folder structure

## Ethical & Accessibility Considerations ✅

ALT data has been added to the image to assist screen readers.

The dataset contained no personally identifiable data and so that did not need to be anonymised. In the event that this same data were taken from a live HR system, there would be a preparatory exercise to remove any personally identifiable data (name, staff number,address, phone number, etc) to conduct analysis, albeit those details would be needed when running the model at a later date to identify staff at risk of attrition.

## Credits

The repo template was provide by Code Institute.
Sections of code have been taken from the Code Institute LMS lessons and adapted to this scenario.
The content of these workbooks was informed by training material on the Code Insitute Learning Management System.
Data was obtained from HuggingFace.com from <https://huggingface.co/datasets/Redsmoothy/HR_Attrition>.
CSV-to-Github uploader utility was forked from FaraiB/csv-to-github and adapted to include extra array fields.
Copilot was a very able assistant throughout the whole of the process, from the initial analysis of data and hypotheses suggestions, to coding, debugging and helping interpret the results. Copilot is possibly my new best friend, albeit not the most reliable nor always truthful.

## Content

## Project Media 🖼️

The banner image for the readme/Notebook 1 was created by Copilot to represent HR and Collaboration.

## Acknowledgements

Thanks to fellow students and tutors at Code Institute for their assistance in pulling together this project and fixing the inevitable issues.
Thanks to the various dog-sitters who looked after the mutts while I was head-down at times.
Thanks to coffee for the boost.
