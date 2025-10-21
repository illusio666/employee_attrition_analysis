# ![AI logo](https://media.licdn.com/dms/image/v2/D4E16AQGhs_RRie8XAw/profile-displaybackgroundimage-shrink_350_1400/B4EZhg5by7GcAY-/0/1753972326982?e=1762387200&v=beta&t=YZKH32qYFaO_mb401qru40kGNmlCB7pe0w43oRAXxng)

## Employee Attrition Analysis

The following analysis looks at a total of 1400 employee records, some of whom have left the organisation. The intent is to improve our understanding of those departing employees, understand if there might be any common factors causing their departure, and to be able to predict future potential departures. This will allow the organisation to do two things:
- to address any underlying factors that have a significant relationship to employee departure, and
- identify those employees at highest risk of departure and focus on their retention as a priority.

## Project Objective 📊

The business has asked that the Data Analysis team review the data and identify actions that management may consider to improve staff retention. These recommendations should be clear and supported with easily-understood charts and visualisations for those team members who are not data analysts.

## Dataset Content & Overview 📁

This publicly-available  data set has been sourced from HuggingFace <https://huggingface.co/datasets/Redsmoothy/HR_Attrition>

## Data Preparation Summary 🧹



## Project Approach 🧠



## Hypotheses and validation approach 

There are 4 hypotheses that the business has asked to be addressed as part of this analysis:

1) Attrition is spread evenly across all departments, with no single department having a statistically-significant higher attrition.
2) Employees living further away from work are more inclined to leave, as commute times are a factor in work:life balance
3) Younger employees are more likely to be 'job hoppers' and so hiring and retention needs to consider how this may be mitigated
4) Job stagnation (years in the same role) causes attrition

These four hypotheses will be tested, to allow the business to develop actions plans to address any root causes.

Additionally, the data will be analysed to see if any other correlations can be found between employee attrition and other factors, either individually or combined, to allow the business to determine if there are other actions that may be beneficial.

Employees will then be clustered based on their risk profile to allow the business to tailor their retention approaches.

## Hypothesis 1 - No department has greater attrition than the others


## Main data analysis libraries (Diana)


## Analysis techniques used


## Dashboard design


## Unfixed bugs

There were no unfixed bugs.

## Conclusions & recommendations (Diana & Matt)

Additional data sets would have also allowed us to move into both Predictive and Prescriptive analysis, looking more towards the options and campaigns for our clients. For example, we discussed whether our goal was to improve client health, profits, or a measure of both. Both positions, however, are difficult to explore without both a broader context of health in the regions and the associated costs to those of charges. A company, for example, wanting to maximise profits in the short term may well be perfectly content to have customers smoke at an early stage of their life, knowing that they can charge significantly higher amounts, yet do not take on many, if any of the associated costs that may result in their care later in life. This, put against a company that takes a long-term client-focused approach, may well offer lower costs and monthly premiums for customers who engage in health behaviour, so lowering their BMI and stopping smoking, and as a result both interact and charge their customers in radically different ways.
In short, given the nature of the data and with limited external context, we took time to address possible different business conditions, and this was presented in both our visualisations and dashboards to reflect potential campaigns to look at addressing both regional and broader trends in health and cost analysis, but where ultimately limited by the scope and depth of the data we had available.

## Folder structure

The Jupyter notebook visualisations of the data can be found within the jupyter_notebook folder, along with the data cleaning and transformation .ipynb.

The original and cleaned data sets can be found in the datasets folder.

The Power BI dashboard, Github user stories csv and the import_issues.py (csv_to_github upload utility) can be found in the main folder.

## Ethical Considerations ✅

- No personally identifiable data was present; GDPR compliance was not required
- The dataset used binary sex labels; these were retained as categorical fields to allow future expansion to broader gender constructs

## Credits

The repo template was provide by Code Institute.
The content of these workbooks was informed by training material on the Code Insitute Learning Management System.
Data was obtained from Kaggle.com.
CSV-to-Github uploader utility was forked from FaraiB/csv-to-github and adapted to include extra array fields.

## Content

Data is sourced from Kaggle.com, and is a publicly-available dataset.
Header image is an AI creation from Copilot
BMI ranges provided by NHS.UK website

## Project Media 🖼️

The header image was created by Copilot to represent human–AI collaboration. It is hosted on Rachel Fallon’s LinkedIn profile.

## Acknowledgements

Thanks to fellow students and tutors at Code Institute for their assistance in pulling together this project and fixing the inevitable issues.
