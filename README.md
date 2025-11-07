# Employee Attrition Analysis

<img src="jupyter_notebooks/hero.png" alt="Image of individuals shaking hands and another sat on a pile of books working on a laptop, with the words Employee Analysis Engagement Retention">

The following analysis looks at a total of 1470 employee records for 'Fallon Pharmaceuticals' (made-up company), including both current and former employees. The intent is to improve our understanding of those departing employees, understand if there might be any common factors causing their departure, and to be able to predict future attrition risk. This will allow the organisation to do two things:

- to address any underlying factors that have a significant relationship to employee departure (retention strategy), and
- identify those employees at highest risk of departure and focus on their retention as a priority.

Attrition is both a cost and risk to the business, with the cost to rectruit and train replacement employees being higher than merely continuing to train existing employees; the risk is the loss of expertise can hamper product development if we are unable to replace with equally skilled staff.

## Project Objective 📊

The business has asked that the Data Analysis team review the data and identify actions that management may consider to improve staff retention. These recommendations should be clear and supported with intuitive visuals and plain-language insights for those team members who are not data analysts.

## Executive Summary

Key findings: of the 4 hypotheses that the team was asked to assess, two are proven and two are rejected (see below). Interestingly, one rejected hypothesis revealed the opposite trend: attrition is more prevalent in early tenure rather than due to role stagnation.

When applying machine learning to our data, we find that we can predict attrition with a 90% accuracy, to enable future identification of at-risk employee attrition.

When we look at leaving employees, there are three key areas that stand out, for development of retention strategies:

1) received significant pay increases but show signs of disengagement
2) young and mobile

- Additionally long commutes (independent of the two groups above).

For groups 1) and 2), tactics to improve engagement are suggested in the notebooks, including structured and agreed career paths, skills enhancements, improved managerial engagement and, for the 'young and mobile', improved team social engagement.

Actual areas would need to be validated with qualitiative feedback (employee surveys) as these are based on the limited dataset and 'possible' causes of job mobility.

For long commutes, while this doesn't help to predict attrition in our employee segmentation, it is nevertheless related to elevated attrition levels when commutes exceed 10 miles. So consideration should be given to reviewing the 'return to work' mandate with a priority for employees with a long commute (but see Ethics section regarding bias and treating employees fairly).

For future analysis, especially to test if any future retentions strategy is effective, there needs to be additional 'date' data captured/included in the analysis (date of resignation, date of exit, possibly date of hire). This will allow trends and responses to company policy/external market changes to be analysed.

## Hypotheses and validation approach

There are 4 hypotheses that the business has asked to be validated as part of this analysis:

1) Attrition is spread evenly across all departments, with no single department having a statistically-significant higher attrition.
2) Role stagnation contributes to employees leaving; average tenure in current or final role is higher for those departing than the company average.
3) Younger employees are more likely to be 'job hoppers' and so hiring and retention needs to consider if this may be mitigated
4) Commute distances can impact attrition - those employees with longer to travel are more likely to leave.

These four hypotheses will be tested, to allow the business to develop action plans to address any root causes.

Additionally, the data will be analysed to see if any other correlations can be found between employee attrition and other factors, either individually or combined, to allow the business to determine if there are other actions that may be beneficial.

Employees will then be clustered based on their risk profile to allow the business to tailor their retention approaches.

## Conclusions

### Hypothesis 1 - No department has greater attrition than the others

This hypothesis is rejected.

While sales and HR have similar attrition, Research & Development have a statistically significant lower attrition, so further qualitative research should be done to compare R&D staff sentiment to other depts.

### Hypothesis 2 - Job stagnation leads to attrition

This hypothesis is rejected.

Employees who leave the organisation have significantly shorter tenure both in role and in the company than those who have stayed. Recommendation for exit interviews to seek feedback on whether jobs met expectations for those who leave within 12months of starting.

### Hypothesis 3 - Attrition is greater for younger employees

This hypothesis is proven.

With the exception of potential retirees (relevant flag is not present in the data), attrition %s are higher in the 20-35yrs groups. It can also be seen that single employees are more likely to leave.

Perhaps we need a company-wide dating app?

### Hypothesis 4 - Commute distance has an impact on retention

This hypothesis is proven.

Employees with a commute of 10+ miles are more likely to leave and so return-to-work policies should be reviewed if retention is a priority.

### Segmentation strategy

Two groups of employees have been identified with above-average attrition:

- Young, mobile employees (30% attrition)
- High salary increase but low engagement (17% attrition).

Priority focus should be on the former group by virtue of its highest %, especially if the company wishes to ensure that investment in training younger employees is retained in the company.

---
---
---

## Approach

## Dataset Content & Overview 📁

This publicly-available  data set has been sourced from HuggingFace <https://huggingface.co/datasets/Redsmoothy/HR_Attrition>.

Data is also synthesised as part of the logistic attrition modelling due to the imbalance of Attrition to non-attrition staff.

## Data Preparation Summary 🧹

For the ETL notebook, the initial use of ydata-profiling indicated areas for data clean up and any 1:1 correlations between columns. This identified several data fields that could be dropped as they added no value to analysis (unique, constants). There were no empty values that needed to be imputed and the '0' values were valid and therefore left.

In anticiation of future analysis, some numeric fields representing ordinal categories were recoded appropriately and 'ratio' fields were added to give an indication of how pay, time in company and time in role related to each other in case that highlighted any themes during the ML modelling. As those created non-numeric values (infinites and non-numeric values) those were changed for the purpose of analysis but marked accordingly in case they needed to be omitted later on.

## Project Approach 🧠

To ensure a robust set of tasks, the 5 key stages of the activity (ETL, visualisations, ML, PowerBI dashboard, overall management) were broken down into key steps and sequenced across a 5 day period.

Those tasks were added to a CSV file in standard User Story format and allocated labels, milestones and an Assignee.

The User Story CSV was then uploaded to a Github project board via a .py issues uploader (see csv-to-github-upload folder and credits for original creator).

Github project board can be found here - <https://github.com/users/illusio666/projects/8/views/1>

Contingency time was allocated, to ensure there was leeway in the event unanticipated issues, with Day 5 tasks being reserved for light tasks.

Tasks were monitored each day to a) ensure workload at start of day was known b) progress was on track midway through the day and c) any slippage at end of day was updated and adjustments made for the next day(s).

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
- imbalanced-learn

## Analysis techniques used

For each of the four hypotheses, the relevant data was visualised in order to detect any potential patterns/causes. Where visualisations indicated a possible relationship, mathematical significance was tested to see whether results showed statistically significant relationships warranting further attention  (Chi-squared to test relationships between categorical data, Mann-Whitney for non-normal numerical data across Attrition:Yes and Attrition:No groups).

For the machine learning model, RandomForest was used to build a prediction model for attrition. As the initial results from the full data set were fairly weak, I used logistic regression to identify those features that were most pertinent for attrition, and then limited the model to those top 20 features. Then, due to the imbalance of data (leavers are only 16% of the dataset), SMOTE was used to create synthetic data for the attrition group. The end result was a 90% accuracy rate.

While certain models would warrant a higher accuracy rate e.g. medical diagnoses, for staff retention strategy this is a sound outcome.

## Dashboard design

The dashboard is intended to simulate a managerial 'People' dashboard for which Tabs 1 & 2 are designed for automatic refresh upon data update. As such, no embedded commentary is included, as these tabs are intended for independent exploration.

Tab 3 provides dynamic insights tailored to each refresh cycle.

None of the tabs are intended to replicate the attrition prediction/retention strategy in the notebook, as those would be strategic HR outputs for assessment by a small team of stakeholders, and not public-facing.

As the dataset lacks any timestamps (see Exec Summary and Findings & Recommendations in notebook 4.), it was not possible to analyse attrition over any time period/determine if it's increasing or decreasing. This would be something strongly recommended if any retention strategy needed to be monitored for effectiveness.

## Limitations ⚠️

- The dataset lacks timestamp fields, preventing longitudinal analysis of attrition trends.
- Certain demographic flags (e.g. retirement eligibility) are absent, limiting segmentation granularity.
- Synthetic data was used to balance the attrition class, which may not fully reflect real-world distributions.

## Unfixed bugs

There were no unfixed bugs.

## Folder structure

The ETL, visualisations and machine learning are all located in the jupyter_notebooks folder, as are any images displayed in the notebooks and the final machine learning model .pkl file.

The original and cleaned data CSVs can be found in the Data files folder.

The Power BI dashboard is in the folder Dashboard files, and can also be accessed online (until Pro subscription expires in Apr '26) at the following link https://app.powerbi.com/links/LCrmSPCrFy?ctid=c233c072-135b-431d-af59-35e05babf941&pbi_source=linkShare

Files relating to the User Stories and their automated upload to GitHub can be found in the csv-to-github-upload folder.

## Ethical Considerations ✅

The dataset contained no personally identifiable data and so that did not need to be anonymised/GDPR is not a consideration in this case. In the event that this same data were taken from a live HR system, there would be a preparatory exercise to remove any personally identifiable data (name, staff number, address, phone number, etc) to conduct analysis, albeit those details would be needed when running the model at a later date to identify staff at risk of attrition.

As the dataset is factual data on employees, rather than a dataset with subjective content, there is no expectation of bias in the data itself.

There would be a real-world consideration when it comes to identifying potential leavers and deploying a retention strategy aimed at those groups:

- potential preferential treatment of subsets of employees (training plans, pay reviews, relaxing of 'work-from'home policies for long commuters, etc)
- tailoring activity towards certain attrition influencers (e.g. marital status) may be inappropriate and seen as 'judgemental'.
- retention strategy may not be in line with the employee's best interest
- retention strategy for some individuals may not be in line with the company's best interest e.g. staff with performance issues.

Development and deployment of any strategies would need to be considered in terms of fairness to all employees and what exceptions might be legitimately (and legally) made to those strategies.

Where employees are demonstrably below market rate, this is a valid reason to conduct a review and adjustment. However, such activity based on more subjective evaluations (e.g. manager discretion) is subject to bias and therefore risk.

## Accessibility considerations ✅

ALT data has been added to the image to assist screen readers.

Colour palettes have been chosen to be colourblind-safe i.e. no red/green combinations despite the typical bad/good connotations that might be inferred from doing so.

## Credits

The repo template was provided by Code Institute.

Sections of code have been taken from the Code Institute LMS lessons and adapted to this scenario.

The content of these workbooks was informed by training material on the Code Insitute Learning Management System.

Data was obtained from HuggingFace.com from <https://huggingface.co/datasets/Redsmoothy/HR_Attrition>.

CSV-to-Github uploader utility was forked from FaraiB/csv-to-github and adapted to include extra array fields.

Copilot provided extensive support throughout the project — from hypothesis refinement to code debugging and narrative generation. While not infallible, it proved a valuable collaborator.

## Project Media 🖼️

The banner image for the readme/Notebook 1 was created by Copilot to represent HR and Collaboration.

## Acknowledgements

Thanks to fellow students and tutors at Code Institute for their assistance in pulling together this project and fixing the inevitable issues.

Thanks to the various dog-sitters who looked after the mutts while I was head-down at times.

Thanks to coffee for its unwavering support.
