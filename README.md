# Applied Data Analysis - Semester Project
EPFL Fall Semester 2021-2022
Raphael Bonatti, Simon Spangenberg, Antoine Crettenand, Saad Charkaoui

## Abstract

It is often argued that former US president Donald Trump's upset victory in the 2016 elections significantly relates to his ability to monopolize the attention of mass media outlets [[1]](https://www.politico.com/magazine/story/2016/11/2016-election-trump-media-takeover-coverage-214419/). Although former president's polemical nature granted him a front row seat at almost every national newspaper in the months preceding the election [[2]](https://www.bbc.co.uk/news/36429660.amp), how can we precisely assess the influence that such incessant media coverage has had on the outcome of the elections? This it the question that we aim to answer in our study. We aim at using the quotebank corpus to analyse possible correlations and causations between the media coverage of three different major outlets with notoriously distinct political inclinations (CNN, BBC, NYTimes) and voting intentions in the months preceding each elections.

## Research Questions
* **Question 1**: How can we quantify media coverage? 
* **Question 2**: How can we quantify/parse voting intentions? 
* **Question 3** Can we find a correlation between voting intention and media coverage? Does the sentiment of the quotations have a stronger impact on the voting intention than the occurences of mentions (sentiment vs quantity)? 
* **Question 4**: Can we determine similar behaviors in media coverage from 2012, 2016 and 2020 (considering the different outcomes in the elections). Can we determine a difference in the republican media coverage (based on occurences and sentiment) in 2012, 2016 and 2020 (since the arrival and departure of Trump)? 
* **Question 5**: Can we perform Topic Modeling on the quotations to determine whether in the labeled text sentiment analysis data, certain topics are reccurent and may have had an impact in the voting intentions?
* **Further Optional Analysis**: If we find correlation in our study, can we perform statistical tests to see if causality between media coverage and vote intention can be determined? 

## Methods
✔️ - Done\
:o: - To do
* **Part 1**: Quantifying Media Coverage ✔️ 
  * Method 1: We parse the Quotebank dataset based on the three newspapers we focus our study on(CNN, BBC, NYTimes). Once this parsing is done, we parse each quotation based on the occurence of the following keywords in the quotation, urls or speaker columns of the dataset. See [Notebook](media_coverage_occurences.ipynb):green_book: for detailed information.
  * Method 2: We perform text sentiment analysis on the quotations retrieved in the first method (on a presidential candidate basis) for each newspaper. See [Notebook](sentiment_analysis.ipynb):blue_book: for detailed information.
* **Part 2**: Quantifying/Parsing voting intention data ✔️
  *  We scrape the website given in the Additional Analysis section. This website contains information relating to voting intentions taken from different surveys accross the United States from January 2012/2016/2020 to November 2012/2016/2020. See [Notebook](votes_intention.ipynb):orange_book: for detailed information.
* **Part 3**: Correlation Study :o:
  * We could use several statistical tests to determine whether there is correlation between voting intention and any of the two methods used to quantify media coverage of the three newspapers of interest. These tests may include computing pearson correlation coefficients between the two distributions and computing a statistical test for the null hypothesis that media coverage does not influence voting intentions, and so forth. 
* **Part 4**: Comparing the elections :o:
  * Here too, we would compare the distributions of media coverages and voting intentions accross the years. We aim at finding repeated patterns between the coverage of certain media and the voting intentions that can be observed accross each election. Additionally, we aim at finding whether the arrival of Trump in the 2016 elections has altered the way media have covered the elections (this may be done by comparing the media coverage between the 2012 and 2016 elections, we believe that text sentiment analysis may give us interesting results here). This can be done by visually comparing the data processed in previous parts for each elections on  a monthly basis. We can further expand our comparison analysis by performing null hypothesis tests and regression analysis.
* **Part 5**: Topic Modeling :o:
  * We develop a topic modeling analysis to cluster the quotations per candidate. We then compare the topics retrieved for each candidate with voting intentions for a specific month prior to the election. We may have to use the Article-Centric version of Quotebank for better results. 
* **Further Optional Analysis**: :o:
  * We are interested in determining whether either of the media coverage methods proposed (occurence & text sentiment analysis) can be used to determine causality between certains topics of media coverage and the voting intentions. This can be determined through Granger causality tests i.e if media coverage forecasts vote intentions.


Of course this observational study would require us to perform some sensitivity analysis on the media coverage methods described above to determine whether causality exists (for instances, by finding ways of matching different examples of media coverage). 

## Current Analysis Performed
We have noted in our current analysis that the quotations for 2020 stops in April. This means that we will most likely have to eliminate 2020 from our study. Concerning 2016, we've notice that some of the months contain very little quotations (most likely due to the unbalanced nature of the quotebank dataset). We will decide in the upcoming days how we want to process this lack of data (i.e if we can find a suitable way to augment the data). 
There are three notebooks: sentiment analysis, occurence analysis, scrapping polls. 
* :green_book:[media_coverage_occurences.ipynb](media_coverage_occurences.ipynb): includes parsing the data from quotebank dataset and quantitative study of candidate name occurence per newspaper. See notebook for detailed information.
* :blue_book:[sentiment_analysis.ipynb](sentiment_analysis.ipynb): includes exploratory sentiment analysis with baseline implementation on the parsed [dataset](Data/). See notebook for detailed information.
* :orange_book:[votes_intention.ipyng](votes_intention.ipynb): includes the scraping of polls in 2012/20216/2020 (below the Additional Datsets), data cleaning and preprocessing, aggregating the polls by month to plot the timeseries per each candidate. See notebook for detailed information.

## Additional Datasets
* :chart_with_upwards_trend:[Polls 2020 elections January-November](https://www.realclearpolitics.com/epolls/2020/president/us/general_election_trump_vs_biden-6247.html#polls)
* :chart_with_upwards_trend:[Polls 2016 elections January-November](https://www.realclearpolitics.com/epolls/2016/president/us/general_election_trump_vs_clinton-5491.html)
* :chart_with_upwards_trend:[Polls 2012 elections January-November](https://www.realclearpolitics.com/epolls/2012/president/us/general_election_romney_vs_obama-1171.html#!)

## Project overview
![Optional Text](Visualizations/project_diagram.jpg)

## Proposed Timeline & Team Organization
* Raphael: Correlation study & visualization. 
* Simon: Works on parsing the data from the quotebank database for each newspaper of interest & building the occurences timeline. Causality Testing
* Antoine: Works on the text sentiment anaxtlysis model.
* Saad: Works on the web scraping and voting intention aggregation.

![Optional Text](Visualizations/gant.JPG)

## Questions for the TAs
Do you have any advice on how we may handle the 2016 missing data? 


## Additional Note
Original idea taking from the [following study](https://www.researchgate.net/publication/335908711_What_matters_context_or_sentiment_Analysing_the_influence_of_news_in_US_elections_using_Natural_Language_Processing). Our research aims to reproducing and expanding this study with the quotebank dataset. We believed that this research was ideal for ADA's semester project since it involves many of the topics covered in class: web scrapping/data retrieval, visualization, topic modeling, text sentiment analysis, correlation and causation study, etc.
