import time

from textblob import TextBlob
import pandas as pd

# Preprocess imports and static variables
import re
import nltk
import string

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

nltk.download('stopwords')
nltk.download('wordnet')

punctuation_string = string.punctuation
punctuation_string = punctuation_string.translate({ord(i): None for i in '@'})

replaced_words = [("hmmyou", ""), ("sry", "sorry"), ("inlove", "in love"), ("thats", ""), ("wanna", ""),
                  ("soo", "so"), ("inlove", "in love"), ("amazingwell", "amazing well"),
                  ("messagesorry", "message sorry"), ("½", ""), ("tomorrowneed", "tomorrow need"),
                  ("tomorrowis", "tomorrow is"), ("amusedtime", "amused time"), ("weekendor", "weekend or"),
                  ("competitionhope", "competition hope"), ("partypicnic", "party picnic"),
                  ("ahmazing", "amazing"), ("wont", "will not"), ("didnt", "did not"), ("dont", "do not"),
                  ("lookin", "looking"), ("u", "you"), ("youre", "you are"), ("nite", "night"), ("isnt", "is not"),
                  ("k", ""), ("is", ""), ("doesnt", "does not"), ("l", ""), ("x", ""), ("c", ""), ("ur", "your"),
                  ("e", ""), ("yall", "you all"), ("he", ""), ("us", ""), ("okim", "ok i am"), ("jealousi", "jealous"),
                  ("srry", "sorry"), ("itll", "it will"), ("vs", ""), ("weeknend", "weekend"), ("w", ""),
                  ("yr", "year"), ("youve", "you have"), ("havent", "have not"), ("iï", ""), ("gonna", "going to"),
                  ("gimme", "give me"), ("ti", ""), ("ta", ""), ("thru", "through"), ("th", ""),
                  ("imma", "i am going to"),
                  ("wasnt", "was not"), ("arent", "are not"), ("bff", "best friend forever"),
                  ("sometimesdid", "sometimes did"),
                  ("waitt", "wait"), ("bday", "birthday"), ("toobut", "too but"), ("showerand", "shower and"),
                  ("innit", "is not it"), ("surgury", "surgery"), ("soproudofyo", "so proud of you"), ("p", ""),
                  ("couldnt", "could not"), ("dohforgot", "forgot"), ("rih", "right"), ("b", ""), ("bmovie", "movie"),
                  ("pleaseyour", "please your"), ("tonite", "tonight"), ("grea", "great"), ("se", ""),
                  ("soonso", "soon so"),
                  ("gettin", "getting"), ("blowin", "blowing"), ("coz", "because"), ("thanks", "thank"), ("st", ""),
                  ("rd", ""),
                  ("gtta", "have got to"), ("gotta", "have got to"), ("anythingwondering", "anything wondering"),
                  ("annoyedy", "annoyed"), ("p", ""), ("beatiful", "beautiful"), ("multitaskin", "multitasking"),
                  ("nightmornin", "night morning"), ("thankyou", "thank you"), ("iloveyoutwoooo", "i love you two"),
                  ("tmwr", "tomorrow"), ("wordslooks", "words looks"), ("ima", "i am going to"), ("liek", "like"),
                  ("mr", ""),
                  ("allnighter", "all nighter"), ("tho", "though"), ("ed", ""), ("fyou", ""), ("footlong", "foot long"),
                  ("placepiggy", "place piggy"), ("semiflaky", "semi flaky"), ("gona", "going to"), ("tmr", "tomorrow"),
                  ("ppl", "people"), ("n", ""), ("dis", "this"), ("dun", "done"), ("houseee", "house"),
                  ("havee", "have"),
                  ("studyingwhew", "studying whew"), ("awwyoure", "aww you are"), ("softyi", "softy"),
                  ("weddingyou", "wedding you"), ("hassnt", "has not"), ("lowerleft", "lower left"),
                  ("anywayss", "anyway"),
                  ("adoarble", "adorable"), ("blogyeahhhh", "blog yeahhhh"), ("billsim", "bills i am"), ("ps", ""),
                  ("cheescake", "cheesecake"), ("morningafternoonnight", "morning after noon night"),
                  ("allstudying", "all studying"), ("ofcoooursee", "of course"), ("jst", "just"), ("shes", "she is"),
                  ("sonicswhich", "sonics which"), ("ouchwaited", "ouch waited"), ("itll", "it will"),
                  ("orreply", "or reply"),
                  ("somethin", "something"), ("fridayand", "friday and"), ("outta", "out of"),
                  ("herenever", "here never"), ("weve", "we have")
                  ]

stopword = nltk.corpus.stopwords.words('english')
ps = nltk.PorterStemmer()
wn = nltk.WordNetLemmatizer()


def preprocess_data_for_sentiment_analysis(df: pd.DataFrame, tags=[]):
    """Preprocess dataframe for sentiment analysis by applying successive functions:
    Quotes -> Remove Punctuation -> Tokenization -> Stemmed -> Lemmatization

    Args:
        df (pd.DataFrame): Dataframe which contains quotes in 'quotation' column.
        tags (list, optional): Specify the stages of preprocessing which will be appended to the original dataframe. Defaults to [].

    Returns:
        pd.DataFrame: Original df with the specified added columns.
    """
    kvmap = {}
    quotes_punc = df['quotation'].apply(lambda x: remove_punct(x, punctuation_string))
    quotes_tokenized = quotes_punc.apply(lambda x: tokenization(x.lower()))
    quotes_tokenized = quotes_tokenized.apply(lambda x: replace_words(x, replaced_words))
    quotes_nonstop = quotes_tokenized.apply(lambda x: remove_stopwords(x, stopword))
    quotes_stemmed = quotes_nonstop.apply(lambda x: stemming(x))
    quotes_lemmatized = quotes_nonstop.apply(lambda x: lemmatizer(x))
    quotes_conc_lemmatized = quotes_lemmatized.apply(lambda x: ' '.join(str(e) for e in x))

    kvmap.update({'quotation_tokenized': quotes_tokenized})
    kvmap.update({'quotation_stemmed': quotes_stemmed})
    kvmap.update({'quotation_lemmatized': quotes_lemmatized})
    kvmap.update({'quotation_conc_lemmatized': quotes_conc_lemmatized})

    for tag in kvmap:
        if tag in tags:
            df[tag] = kvmap[tag]

    print(f'[process_sa] Prepared for sentiment analysis with tags: {tags}')
    return df


def remove_punct(text: str, punctuation_string: str):
    text = "".join([char for char in text if char not in punctuation_string])
    text = re.sub('[0-9]+', '', text)
    return text


def tokenization(text: str):
    text = re.split('\W+', text)
    return text


def replace_words(text: str, replaced_words: list):
    ind = -1
    for word in text:
        ind += 1
        for k in range(len(replaced_words)):
            if word == replaced_words[k][0]:
                text[ind] = replaced_words[k][1]
            elif "http" in word:
                text[ind] = ""
            elif "@" in word:
                text[ind] = ""
            elif "www." in word:
                text[ind] = ""
            elif "Â" in word:
                text[ind] = ""
            elif "Ã" in word:
                text[ind] = ""
            elif "½" in word:
                text[ind] = ""
            elif "[" in word:
                text[ind] = ""
            elif "]" in word:
                text[ind] = ""
            elif "b" in word:
                text[ind] = ""
    return text


def remove_stopwords(text, stopword):
    text = [word for word in text if word not in stopword]
    return text


def stemming(text):
    text = [ps.stem(word) for word in text]
    return text


def lemmatizer(text):
    text = [wn.lemmatize(word) for word in text]
    return text


def expand_quotations_with_polarity_subjectivity(df: pd.DataFrame, column: str = 'quotation', model: str="TextBlob"):
    """Sentiment Analysis implementation using a specified model. Default is TextBlob

    Args:
        :param df (pd.DataFrame): DataFrame containing the quotations.
        :param column (str, optional): Specify the column name where the quotations are stored. Defaults to 'quotation'.
        :param model: Name of the model to use for analysis
    Returns:
        pd.DataFrame: Original dataframe with appended polarity and subjectivity.
    """
    start = time.time()
    if model == "TextBlob":
        df['quotation_polarity'] = df[f'{column}'].map(lambda x: TextBlob(x).sentiment.polarity)
        df['quotation_subjectivity'] = df[f'{column}'].map(lambda x: TextBlob(x).sentiment.subjectivity)
    elif model == "Vader":
        analyzer = SentimentIntensityAnalyzer()
        df['quotation_polarity'] = df[f'{column}'].map(lambda x: float(analyzer.polarity_scores(x)['compound']))
        # map to [-1, 1]
        nmin = df['quotation_polarity'].min()
        nmax = df['quotation_polarity'].max()
        df['quotation_polarity'] = df['quotation_polarity'].map(lambda x: (x - nmin) / nmax)

        df['quotation_subjectivity'] = df[f'{column}'].map(lambda x: 0)
    else:
        raise NameError(f'{model} is not a possible model. Choose from : TextBlob & Vader')
    end = time.time() - start
    print(f"Processed dataset {df.shape} with {model} in {end} seconds.")

    return df
