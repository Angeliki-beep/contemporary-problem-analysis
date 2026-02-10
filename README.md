# contemporary-problem-analysis
# Automated Customer Feedback Analysis

## Project Overview
This project uses **AI and Natural Language Processing (NLP)** to analyze customer feedback automatically.  
The system detects whether feedback is **positive, negative or neutral** and calculates a confidence score for each entry.



## Features
- Reads customer feedback from a CSV file  
- Detects sentiment (positive/negative) using a pre-trained AI model  
- Saves results with sentiment labels and confidence scores  
- Measures the time taken for analysis  



## Dataset
The project uses a CSV file called `customer_feedback.csv` with one column:

feedback 

"The service was excellent and very fast." 
"I am unhappy with the product quality." 
"It was okay, nothing special." 
"The support team was very helpful." 
"This was a terrible experience." 



## Installation

1. Install Python 3.x  
2. Install required libraries:

```bash
pip install pandas transformers torch

```
Usage

Place customer_feedback.csv in the project folder

Run the main script:

python main.py


The program will create a file called feedback_results.csv with the results



# Weekly Log – Automated Customer Feedback Analysis

This log documents the weekly progress, tasks, and development activities for the project **Automated Customer Feedback Analysis Using NLP**. All work was tracked using GitHub commits.



## Week 1 – Topic Selection & Proposal
- Selected the project topic: Automated Customer Feedback Analysis  
- Wrote initial project proposal  
- Submitted proposal to instructor for approval  
- Created GitHub repository and initialized version control  

## Week 2 – Literature Review
- Conducted a literature review on NLP, sentiment analysis, and automation  
- Collected academic papers, online tutorials, and industry references  
- Documented sources for Harvard-style reference list  
- Identified tools and technologies for the project (Python, spaCy, HuggingFace, Power BI)  

## Week 3 – Research Question & Objectives
- Defined the research question:  
  *“Can NLP reduce the time required to analyze customer feedback by more than 50% without significantly reducing accuracy?”*  
- Set project objectives:  
  - Investigate NLP techniques for feedback analysis  
  - Design automated analysis system  
  - Implement and evaluate sentiment analysis  
- Planned evaluation metrics (time reduction, accuracy, visualization)  

## Week 4 – Dataset Selection & Exploration
- Found publicly available customer feedback dataset  
- Cleaned and explored the dataset using Python and Pandas  
- Checked data for missing values, duplicates, and formatting issues  
- Documented dataset characteristics for reproducibility  

## Week 5 – System Design
- Designed system architecture for automated sentiment analysis  
- Planned the main pipeline:  
  1. Load dataset  
  2. Preprocess text  
  3. Sentiment analysis using AI model  
  4. Save results  
  5. Visualize using Power BI  
- Created initial diagrams for report documentation  

## Week 6 – Implementation: Text Processing
- Wrote Python code for reading CSV files  
- Implemented beginner-friendly sentiment analysis pipeline  
- Tested text input to ensure correct reading and basic cleaning  

## Week 7 – Implementation: Sentiment Analysis
- Integrated HuggingFace transformer model for sentiment detection  
- Created `sentiment_analysis.py` module  
- Tested model with sample customer feedback  
- Recorded outputs for accuracy and confidence scores  

## Week 8 – Experiments
- Conducted manual sentiment analysis on sample dataset  
- Ran automated sentiment analysis for comparison  
- Recorded time taken for manual vs automated processes  
- Stored results for evaluation and visualization  

## Week 9 – Evaluation & Visualization
- Compared manual and automated results to check accuracy  
- Calculated percentage time reduction  
- Created Power BI dashboards to visualize sentiment trends  
- Documented insights and limitations for report  

## Week 10 – Finalization & Reporting
- Wrote final 3000-word report  
- Added methodology, solution, experiments, evaluation, and conclusion sections  
- Included references in Harvard format  
- Updated GitHub repository with all files: code, dataset, results, README, weekly log  
- Prepared presentation slides and supporting materials  
