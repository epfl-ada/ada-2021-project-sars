# ada-2021-project-sars
ada-2021-project-sars created by GitHub Classroom

**For Sunday**: 
* Simon: Build training data set NYTimes
* Saad: Build the model for topic modelling
* Antoine: Build the external timelines
* Raphael: Try to build different functions for popularity measurements. 

## Introduction & Context

**Write a Small Abstract Here**

## Questions we want to answer and analyse
* **First Part**: Are the topics covered by the media in the years 2015-2020 an accurate representation of the key events that occured within these years (we focus on four topics: Politics, Sports and Technology)?
* **Second Part**: What are the proportions of key events covered in the newspaper related to each topic? Do media tend to cover more one topic over another? 
* **Third Part**: If any bias is found in part 2, what could cause such bias? Can we infer some possible conclusion by looking at external data sets - such as for instance, focusing on the New York Times Newspaper, can we draw a correlation between monthly income and number of topics covered in a month?)

## Additional Datasets

## Methodology
1. **Topic Modeling**: Our first work relates to building an appropriate topic modeling algorithm that will be able to classify each quote in the quotebank dataset into one of the four aforementioned topics. The main challenges of this task are the following: first, finding/building a training data set that will appropriately train our topic modeling classifier. To do so we need to find data that includes distinctive quotes from each of the four topics we are looking for. The second challenge relates to building the model itself. 
   1.1.     
3. 
4.   to find the quotes for the four topics defined.
    *   First metric to determine key events per topic: aggregate the time of quotes in a month. Find the number of quotes in each specific timeframe. This distribution will tell us if something special happened in this month for a certain topic. So the y axis will be the month, the x axis will be the month.
    * This gives us a timeline of key events but does not give us information related to the actual events (we have clusters of quotes for each month but do not know what the cluster refers to). 
    *  Plot/Aggregate the quotes per topics for each specific topic in a single month. That will help us determine if something specific happened in a month - relate big event to the number of quotes clustered in a given timeframe.  

## Hopeful achieved Results










- Topic Modeling (cluster on certain topics) - use all the topics we can find from the parsing (for the baseline) (Simon & Saad)
- After the Topic Modeling: extract relevant information from quotes for each topic (such as context, sentiment, etc) And infer some conclusions based on the infered information. Focuse on the rest of the information in each quotation (Raphael & Antoine)
- Once the topic modeling is done: 


# README - What we need to do
Readme.md file containing the detailed project proposal (up to 1000 words). Your README.md should contain:

    Title
    Abstract: A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?
    Research Questions: A list of research questions you would like to address during the project.
    Proposed additional datasets (if any): List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible.
    Methods
    Proposed timeline
    Organization within the team: A list of internal milestones up until project Milestone 3.
    Questions for TAs (optional): Add here any questions you have for us related to the proposed project.


