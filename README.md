# ![HR image](https://github.com/illusio666/employee_attrition_analysis/blob/main/hero.png)

## Employee Attrition Analysis

The following analysis looks at a total of 1400 employee records for 'Fallon Pharmaceuticals', some of whom have left the organisation. The intent is to improve our understanding of those departing employees, understand if there might be any common factors causing their departure, and to be able to predict future potential departures. This will allow the organisation to do two things:
- to address any underlying factors that have a significant relationship to employee departure, and
- identify those employees at highest risk of departure and focus on their retention as a priority.

## Project Objective 📊

The business has asked that the Data Analysis team review the data and identify actions that management may consider to improve staff retention. These recommendations should be clear and supported with easily-understood charts and visualisations for those team members who are not data analysts.

## Executive Summary

Key findings: of the 4 hypotheses, two are proven and two are rejected (see below). Of one of the rejected hypotheses, one has been proven to actually be the opposite (job 'stagnation' does not lead to attrition, short tenure employees are more likely to leave).

When applying machine learning to our data, we find that XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

## Dataset Content & Overview 📁

This publicly-available  data set has been sourced from HuggingFace <https://huggingface.co/datasets/Redsmoothy/HR_Attrition>

## Data Preparation Summary 🧹



## Project Approach 🧠



## Hypotheses and validation approach 

There are 4 hypotheses that the business has asked to be validated as part of this analysis:

1) Attrition is spread evenly across all departments, with no single department having a statistically-significant higher attrition.
2) Role stagnation contributes to employees leaving; average (mean) duration in current (or final) role is higher for those departing than the company average.
3) Younger employees are more likely to be 'job hoppers' and so hiring and retention needs to consider if this may be mitigated
4) Commute distances can impact attrition - those employees with longer to travel are more likely to leave.

These four hypotheses will be tested, to allow the business to develop actions plans to address any root causes.

Additionally, the data will be analysed to see if any other correlations can be found between employee attrition and other factors, either individually or combined, to allow the business to determine if there are other actions that may be beneficial.

Employees will then be clustered based on their risk profile to allow the business to tailor their retention approaches.

## Conclusions:

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

## Main data analysis libraries


## Analysis techniques used


## Dashboard design


## Unfixed bugs

There were no unfixed bugs.

## Conclusions & recommendations 



## Folder structure



## Ethical & Accessibility Considerations ✅



## Credits

The repo template was provide by Code Institute.
Sections of code have been taken from the Code Institute LMS lessons and adapted to this scenario.
The content of these workbooks was informed by training material on the Code Insitute Learning Management System.
Data was obtained from HuggingFace.com from .
CSV-to-Github uploader utility was forked from FaraiB/csv-to-github and adapted to include extra array fields.

## Content


## Project Media 🖼️



## Acknowledgements

Thanks to fellow students and tutors at Code Institute for their assistance in pulling together this project and fixing the inevitable issues.
