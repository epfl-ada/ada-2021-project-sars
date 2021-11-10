# Applied Data Analysis - Semester Project
EPFL Fall Semester 2021-2022
Raphael Bonatti, Simon Spangenberg, Antoine Crettenand, Saad Charkaoui

## For Wednesday:
* Raphael: ...
* Simon: Works on parsing the data from the quotebank database for each newspaper of interest. 
* Antoine: Works on the text sentiment analysis model. 
* Saad: Works on the web scraping and voting intention aggregation. 

## Introduction & Context

A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?

Does media coverage faithfully represent vote intentions? More specifically, we analyse three main newspapers and their coverage of the 2016 and 2020 US elections. We aim at answering the question whether there exists a correlation between voter intention and the newspaper coverage. That is, can we assert that the higher coverage of newspaper company regarding a presidential candidate (2016: Clinton/Trump, 2020:Biden/Trump), the higher vote intentions will lean towards that covered candidate? 

## Research Questions
* **Question 1**: How can we quantify media coverage? We propose two methods to quatify media coverage. We will conduct our study on these two methods. 
  * Focus on the number of occurences of a candidates' name in the quotes and url of the quotebank dataset for the years 2012, 2016 and 2020. 
  * Perform a text sentiment analysis on the quotations where the candidate's name occurs in the quotations or the url for the years 2012, 2016 and 2020 (negative vs positive feedback). 
* **Question 2**: For the two media coverage methods mentioned above, can we find correlation between the retrieved coverage and the vote intentions for 2016 and 2020 for the following newspapers: BBC, FoxNews and New York Times? 
  * To do this, we will need to quantify the vote intentions. This will be done by scraping/parsing the following website: https://www.realclearpolitics.com/ (See Additional Datasets section) for 2012, 2016 and 2020 elections. Once the data is parsed, we aggregate it to build voting monthly based voting intentions for each elections. 
* **Question 3**: Comparing the two elections - can be determine similar behavior in media coverage from 2012, 2016 and 2020 (considering the different outcomes in the elections). Can we determine a difference in the republican media coverage in 2012, 2016 and 2020 (since the arrival and departure of Trump)? 
* **Question 4**: If we find correlation in our study, can we perform statistical tests to see if causality between media coverage and vote intention can be determined? Of course this observational study would require us to perform some sensitivity analysis on the media coverage methods described above to determine whether causality exists (for instances, by finding ways of matching different examples of media coverage). 

## Methods
* **Part 1**: Quantifying Media Coverage
  * Method 1: We parse the Quotebank dataset based on the three newspapers we focus our study on. Once this parsing is done, we parse each quotation based on the occurence of the following keywords in the quotation or in the urls: Clinton/Trump for 2016, Biden/Trump for 2020. We can then aggregate the occurences on a monthly basis. 
  * Method 2: We perform text sentiment analysis on the quotations retrieved in the first method (on a presidential candidate basis) for each newspaper. **Antoine Add Some More Here**
* **Part 2**: Parsing the voting intention data & finding correlation
  *  We would scrape the website given in the Additional Analysis section. This website contains information relating to voting intentions taken from different surveys accross the United States from January 2012/2016/2020 to November 2012/2016/2020. Once the data is scraped, we parse it and aggregate it on a monthly basis and use it as a metric to determine overall national voting intentions in the United States in the months preceding the elections. 
  * We would compute the Pearson correlation coefficient between the media coverage for each method proposed and the voting intention computed in the previous step. 
*  **Part 3**: Comparing the two elections
  *  We can visually compare the two elections by analysing the distributions of media coverage occurences on a monthly basis. A similar study can be performed for the text sentiment analysis done. We can further expand our comparison by performing null hypothesis tests and regression analysis. 
*  **Part 4**: Causality tests
  * We are interested in determining whether either of the media coverage methods proposed (occurence & text sentiment analysis) can be used to determine causality between certains topics of media coverage and the voting intentions. To do so, we first need to develop a topic modeling analysis. Once we have divided our quotations of interest into different topics, we can use these topics to perform matching our data.... **TO FINISH BY FRIDAY**

## Current Analysis Performed
We do not have enough data for 2020, so we decided to focus on 2012 instead. Also BBC dataset may not be enough...
There are three notebooks: sentiment analysis, occurence analysis, scrapping polls. 
* data_occurences.ipynb: describe work done 
* Antoine describe notebook and work done
* Saad describe notebook and work done. 

What do we see so far? In the occurence analysis


## Additional Datasets
* Polls for the 2020 elections from January 2020 to November 2020: https://www.realclearpolitics.com/epolls/2020/president/us/general_election_trump_vs_biden-6247.html#polls
* Polls for the 2016 elections from January 2016 to November 2016: https://www.realclearpolitics.com/epolls/2016/president/us/general_election_trump_vs_clinton-5491.html
* Polls for the 2012 elections from January 2012 to November 2012: https://www.realclearpolitics.com/epolls/2012/president/us/general_election_romney_vs_obama-1171.html#!


## Proposed timeline

## Organization within the team
A list of internal milestones up until project Milestone 3.
* Raphael: Correlation study & visualization. Causality Testing
* Simon: Works on parsing the data from the quotebank database for each newspaper of interest & building the occurences timeline. Causality Testing
* Antoine: Works on the text sentiment anaxtlysis model. Causality Testing
* Saad: Works on the web scraping and voting intention aggregation. Causility Testing

## Questions for the TAs
Is it ok to use the 2012 Quotebank dataset?


## Additional Note
https://www.researchgate.net/publication/335908711_What_matters_context_or_sentiment_Analysing_the_influence_of_news_in_US_elections_using_Natural_Language_Processing
