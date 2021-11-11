# Applied Data Analysis - Semester Project
EPFL Fall Semester 2021-2022
Raphael Bonatti, Simon Spangenberg, Antoine Crettenand, Saad Charkaoui

## Introduction & Context

Does media coverage faithfully represent vote intentions? More specifically, we analyse three main newspapers and their coverage of the 2016 and 2020 US elections. We aim at answering the question whether there exists a correlation between voter intention and the newspaper coverage. That is, can we assert that the higher coverage of newspaper company regarding a presidential candidate (2016: Clinton/Trump, 2020:Biden/Trump), the higher vote intentions will lean towards that covered candidate? 

## Research Questions
* **Question 1**: How can we quantify media coverage? 
* **Question 2**: How can we quantify/parse voting intentions? 
* **Question 3** Can we find a correlation between voting intention and media coverage? Does the sentiment of the quotations have a stronger impact on the voting intention than simply the occurences of mentions (sentiment vs quantity)? 
* **Question 4**: Can be determine similar behaviors in media coverage from 2012, 2016 and 2020 (considering the different outcomes in the elections). Can we determine a difference in the republican media coverage (based on occurences and sentiment) in 2012, 2016 and 2020 (since the arrival and departure of Trump)? 
* **Question 5**: If we find correlation in our study, can we perform statistical tests to see if causality between media coverage and vote intention can be determined? Can we perform Topic Modeling on the quotations to determine whether in the labeled text sentiment analysis data, certain topics are reccurent and may have had an impact in the voting intentions?

## Methods
* **Part 1**: Quantifying Media Coverage ✔️ 
  * Method 1: We parse the Quotebank dataset based on the three newspapers we focus our study on. Once this parsing is done, we parse each quotation based on the occurence of the following keywords in the quotation, urls or speaker columns of the dataset: Obama/Romney for 2012, Clinton/Trump for 2016, Biden/Trump for 2020. We can then aggregate the occurences on a monthly basis from January to November (election day). 
  * Method 2: We perform text sentiment analysis on the quotations retrieved in the first method (on a presidential candidate basis) for each newspaper. **Antoine Add Some More Here**
* **Part 2**: Quantifying/Parsing voting intention data ✔️
  *  We scrape the website given in the Additional Analysis section. This website contains information relating to voting intentions taken from different surveys accross the United States from January 2012/2016/2020 to November 2012/2016/2020. Once the data is scraped, we parse it and aggregate it on a monthly basis and use it as a metric to determine overall national voting intentions in the United States in the months preceding the elections. 
* **Part 3**: Correlation Study :o:
  * We could use several statistical tests to determine whether there is correlation between voting intention and any of the two methods used to quantify media coverage of the three newspapers of interest. These tests may include computing pearson correlation coefficients between the two distributions and computing a statistical test for the null hypothesis that media coverage does not influence voting intentions, and so forth. 
* **Part 4**: Comparing the elections :o:
  * Here too, we would compare the distributions of media coverages and voting intentions accross the years. We aim at finding repeated patterns between the coverage of certain media and the voting intentions that can be observed accross each election. Additionally, we aim at finding whether the arrival of Trump in the 2016 elections has altered the way media have covered the elections (this may be done by comparing the media coverage between the 2012 and 2016 elections, we believe that text sentiment analysis may give us interesting results here). This can be done by visually comparing the data processed in previous parts for each elections on  a monthly basis. We can further expand our comparison analysis by performing null hypothesis tests and regression analysis.
*  **Part 5**: Do media coverage forecast vote intentions ? :o:
  * We are interested in determining whether either of the media coverage methods proposed (occurence & text sentiment analysis) can be used to determine causality between certains topics of media coverage and the voting intentions. This can be determined through Granger causality tests i.e if media coverage forecasts vote intentions.
  * Secondly, we develop a topic modeling analysis. Once we have divided our quotations of interest into different topics, we can use these topics to perform matching our data.... **TO FINISH BY FRIDAY**


Of course this observational study would require us to perform some sensitivity analysis on the media coverage methods described above to determine whether causality exists (for instances, by finding ways of matching different examples of media coverage). 

## Current Analysis Performed
We do not have enough data for 2020, so we decided to focus on 2012 instead. Also BBC dataset may not be enough...
There are three notebooks: sentiment analysis, occurence analysis, scrapping polls. 
* data_occurences.ipynb: describe work done 
* Antoine describe notebook and work done
* Saad describe notebook and work done. 

What do we see so far? In the occurence analysis


## Additional Datasets
* Polls for the 2020 elections January-November: https://www.realclearpolitics.com/epolls/2020/president/us/general_election_trump_vs_biden-6247.html#polls
* Polls for the 2016 elections January-November: https://www.realclearpolitics.com/epolls/2016/president/us/general_election_trump_vs_clinton-5491.html
* Polls for the 2012 elections January-November: https://www.realclearpolitics.com/epolls/2012/president/us/general_election_romney_vs_obama-1171.html#!


## Proposed timeline

## Organization within the team
* Raphael: Correlation study & visualization. Causality Testing
* Simon: Works on parsing the data from the quotebank database for each newspaper of interest & building the occurences timeline. Causality Testing
* Antoine: Works on the text sentiment anaxtlysis model. Causality Testing
* Saad: Works on the web scraping and voting intention aggregation. Causility Testing

## Questions for the TAs
Is it ok to use the 2012 Quotebank dataset?


## Additional Note
https://www.researchgate.net/publication/335908711_What_matters_context_or_sentiment_Analysing_the_influence_of_news_in_US_elections_using_Natural_Language_Processing
