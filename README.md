# Applied Data Analysis - Semester Project
EPFL Fall Semester 2021-2022
Raphael Bonatti, Simon Spangenberg, Antoine Crettenand, Saad Charkaoui

**For Sunday**: 
* Simon: Build training data set NYTimes
* Saad: Build the model for topic modelling
* Antoine: Build the external timelines
* Raphael: Try to build different functions for popularity measurements. 

## Introduction & Context

A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?

## Research Questions
* **First Part**: Are the topics covered by the media in the years 2015-2020 an accurate representation of the key events that occured within these years (we focus on four topics: Politics, Sports and Technology)?
* **Second Part**: What are the proportions of key events covered in the newspaper related to each topic? Do media tend to cover more one topic over another? 
* **Third Part**: If any bias is found in part 2, what could cause such bias? Can we infer some possible conclusion by looking at external data sets - such as for instance, focusing on the New York Times Newspaper, can we draw a correlation between monthly income and number of topics covered in a month?)

## Additional Datasets

## Methods
1. **Topic Modeling**: Our first work relates to building an appropriate topic modeling algorithm that will be able to classify each quote in the quotebank dataset into one of the four aforementioned topics. The main challenges of this task are the following: first, finding/building a training data set that will appropriately train our topic modeling classifier. To do so we need to find data that includes distinctive quotes from each of the four topics we are looking for. The second challenge relates to building the model itself. To solve the first challenge, we have parsed all the quotations coming from the NYTimes as they include distinctive topic descriptions in their provenance urls (See notebook NYTimes_Parsing.ipynb). Once the parsing is done, we build a training dataset of 20,000 quotations including only quotes coming from the topics sports, politics, technology and media. The second task involved building a model **Saad expand here**
2. In parallel to topic modeling, we also retrieved information related to key historical events in each of the four targeted topics from the following external sources: **Antoine add sources here**. In essence, we are building a timeline of known key events from data retrieved externally. This timeline will allow easy comparison with the information retrieved from topic modeling. 
3. Building the popularity timeline to compare whether the topics covered by the media in the years 2015-2020 are an accurate representation of the key events that occured within these years **Raphael**. (Do we see spikes at key events? How many occurences in total do we have in each category? Do spikes match expected key events?)
4. Dig deeper into each observed spike to determine that actual event that may have occured. We may return a list of possible words quandidates based on their occurences in each quote and determine if the event itself is present in this list with high overall occurence). Are some major events barely covered in the media? 
5. Analysis on part 2: how can we related each topic to another? Is one topic way more covered than another? 
6. Explanatory part: if we find some bias in part 2, how can we explain it? Do we do some additional analysis on a subset of the data (such as NYTimes articles?) 

## Additional Datasets & Sources
**Antoine**: Sources used for building the external time line? 
**Simon**: I can mention that I use the new york times data set. 
List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible.

## Proposed timeline

## Organization within the team
A list of internal milestones up until project Milestone 3.
* Raphael: 
* Simon: 
* Antoine:
* Saad:

## Questions for the TAs



