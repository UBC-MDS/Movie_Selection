# Task
You will create a scenario for your dashboard, which includes choosing the target audience (internal research team, public communication, etc), who you are (part of a company, NGO, research team, student group, etc), and the goal of building the app for your target audience (communicating your research to the public, deriving market insight, driving end user decision making, etc). It is OK if this changes slightly as your are building the app, but try to stay to it as much as possible so that you have a clear direction throughout

# Proposal

## Section 1: Motivation and Purpose

Our role: Data scientist consultancy firm

Target audience: Real estate companies

Real estate valuation is a valuable insight for companies. Learn from past data in 1990
Whether housing age, number of rooms, its proximity to the ocean among others.


## Section 2: Description of the data

* In your proposal, briefly describe the dataset and the variables that you will visualize. If your are planning to visualize a lot of columns, provide a high level descriptor of the variable types rather than listing every single column. 

* This might include brief exploratory data analysis for you to grasp what could be interesting aspects to look at in your data (non-graded)

The data has been processed by removing missing data as well as adding average per household values for `total_rooms`, `total_bedrooms`

{e.g}
We will be visualizing a dataset of approximately 300,000 missed patient appointments. Each appointment has 15 associated variables that describe the patient who made the appointment (patient_id, gender, age), the health status (health_status) of the patient (Hypertension, Diabetes, Alcohol intake, physical disabilities), information about the appointment itself (appointment_id, appointment_date), whether the patient showed up (status), and if a text message was sent to the patient about the appointment (sms_sent). Using this data we will also derive a new variable, which is the predicted probability that a patient will show up for their appointment (prob_show).

## Section 3: Research questions and usage scenarios


* Research question

{e.g}
Mary is a policy maker with the Canadian Ministry of Health and she wants to understand what factors lead to missed appointments in order to devise an intervention that improves attendance numbers. She wants to be able to [explore] a dataset in order to [compare] the effect of different variables on absenteeism and [identify] the most relevant variables around which to frame her intervention policy. 


* Usage scenario

{e.g}
When Mary logs on to the "Missed Appointments app", she will see an overview of all the available variables in her dataset, according to the number of people that did or did not show up to their medical appointment. She can filter out variables for head-to-head comparisons, and/or rank patients according to their predicted probability of missing an appointment. When she does so, Mary may notice that "physical disability" appears to be a strong predictor missing appointments, and in fact patients with a physical disability also have the largest number of missed appointments. She hypothesizes that patients with a physical disability could be having a hard time finding transportation to their appointments, and decides she needs to conduct a follow-on study since transportation information is not captured in her current dataset.


