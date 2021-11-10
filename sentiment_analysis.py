from textblob import TextBlob
import pandas as pd

# Preprocess imports and static variables
import re
import nltk
import string
nltk.download('stopwords')
nltk.download('wordnet')

punctuation_string = string.punctuation
punctuation_string = punctuation_string.translate({ord(i): None for i in '@'})

replaced_words = [("hmmyou",""),("sry","sorry"),("inlove","in love"),("thats",""),("wanna",""),
                  ("soo","so"),("inlove","in love"),("amazingwell","amazing well"),
                  ("messagesorry","message sorry"),("½",""),("tomorrowneed","tomorrow need"),
                  ("tomorrowis","tomorrow is"),("amusedtime","amused time"),("weekendor","weekend or"),
                  ("competitionhope","competition hope"),("partypicnic","party picnic"),
                  ("ahmazing","amazing"),("wont","will not"),("didnt","did not"),("dont","do not"),
                  ("lookin","looking"),("u","you"),("youre","you are"),("nite","night"),("isnt","is not"),
                  ("k",""),("is",""),("doesnt","does not"),("l",""),("x",""),("c",""),("ur","your"),
                  ("e",""),("yall","you all"),("he",""),("us",""),("okim","ok i am"),("jealousi","jealous"),
                  ("srry","sorry"),("itll","it will"),("vs",""),("weeknend","weekend"),("w",""),
                  ("yr","year"),("youve","you have"),("havent","have not"),("iï",""),("gonna","going to"),
                  ("gimme","give me"),("ti",""),("ta",""),("thru","through"),("th",""),("imma","i am going to"),
                  ("wasnt","was not"),("arent","are not"), ("bff","best friend forever"),("sometimesdid","sometimes did"),
                  ("waitt","wait"),("bday","birthday"),("toobut","too but"),("showerand","shower and"),
                  ("innit","is not it"),("surgury","surgery"),("soproudofyo","so proud of you"),("p",""),
                  ("couldnt","could not"),("dohforgot","forgot"),("rih","right"),("b",""),("bmovie","movie"),
                  ("pleaseyour","please your"),("tonite","tonight"),("grea","great"),("se",""),("soonso","soon so"),
                  ("gettin","getting"),("blowin","blowing"),("coz","because"),("thanks","thank"),("st",""),("rd",""),
                  ("gtta","have got to"),("gotta","have got to"),("anythingwondering","anything wondering"),
                  ("annoyedy","annoyed"),("p",""),("beatiful","beautiful"),("multitaskin","multitasking"),
                  ("nightmornin","night morning"),("thankyou","thank you"),("iloveyoutwoooo","i love you two"),
                  ("tmwr","tomorrow"),("wordslooks","words looks"),("ima","i am going to"),("liek","like"),("mr",""),
                  ("allnighter","all nighter"),("tho","though"),("ed",""),("fyou",""),("footlong","foot long"),
                  ("placepiggy","place piggy"),("semiflaky","semi flaky"),("gona","going to"),("tmr","tomorrow"),
                  ("ppl","people"),("n",""),("dis","this"),("dun","done"),("houseee","house"),("havee","have"),
                  ("studyingwhew","studying whew"),("awwyoure","aww you are"),("softyi","softy"),
                  ("weddingyou","wedding you"),("hassnt","has not"),("lowerleft","lower left"),("anywayss","anyway"),
                  ("adoarble","adorable"),("blogyeahhhh","blog yeahhhh"),("billsim","bills i am"),("ps",""),
                  ("cheescake","cheesecake"),("morningafternoonnight","morning after noon night"),
                  ("allstudying","all studying"),("ofcoooursee","of course"),("jst","just"),("shes","she is"),
                  ("sonicswhich","sonics which"),("ouchwaited","ouch waited"),("itll","it will"),("orreply","or reply"),
                  ("somethin","something"),("fridayand","friday and"),("outta","out of"),("herenever","here never"),("weve","we have")
                 ] 

stopword = nltk.corpus.stopwords.words('english')
ps = nltk.PorterStemmer()
wn = nltk.WordNetLemmatizer()

'''
Preprocess the data for sentiment analysis.
Helper functions below
'''
def preprocess_data_for_sentiment_analysis(df):
    quotes_punc = df['quotation'].apply(lambda x: remove_punct(x,punctuation_string))
    quotes_tokenized = quotes_punc.apply(lambda x: tokenization(x.lower()))
    quotes_tokenized = quotes_tokenized.apply(lambda x: replace_words(x,replaced_words))
    quotes_nonstop = quotes_tokenized.apply(lambda x: remove_stopwords(x,stopword))
    quotes_lemmatized = quotes_nonstop.apply(lambda x: lemmatizer(x))
    df['quotation'] = quotes_lemmatized.apply(lambda x: ' '.join(str(e) for e in x))
    return df

def remove_punct(text,punctuation_string):
    text  = "".join([char for char in text if char not in punctuation_string])
    text = re.sub('[0-9]+', '', text)
    return text    

def tokenization(text):
    text = re.split('\W+', text)
    return text    

def replace_words(text,replaced_words):
    ind = -1 
    for word in text:
        ind +=1
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
            elif "[" in word :
                text[ind] = ""
            elif "]" in word :
                text[ind] = ""
            elif "b" in word :
                text[ind] = ""
    return text    

def remove_stopwords(text,stopword):
    text = [word for word in text if word not in stopword]
    return text    

def stemming(text):
    text = [ps.stem(word) for word in text]
    return text

def lemmatizer(text):
    text = [wn.lemmatize(word) for word in text]
    return text    

'''
Sentiment Analysis implementations.
Helper functions below.
'''
def sa_compute_polarity_and_subjectivity_textblob(filepath: str, chunk_size: int, max_chunks: int, rawdata=True):
    ret_df = pd.DataFrame()
    with pd.read_csv(filepath, compression='zip', chunksize=chunk_size) as df_reader:
        it = 0
        for chunk in df_reader:
            if it >= max_chunks:
                break
            df = chunk
            if rawdata:
                df['quotation'] = df['quotation'].map(lambda x: x.replace('[ ', '').replace(' ] ', ''))
            df['quotation_polarity'] = df['quotation'].map(lambda x: TextBlob(x).sentiment.polarity)
            df['quotation_subjectivity'] = df['quotation'].map(lambda x: TextBlob(x).sentiment.subjectivity)
#            temp_df = df[['quotation', 'quotation_polarity', 'quotation_subjectivity']]
            ret_df = pd.concat([ret_df, df], ignore_index=True)
            it += 1
    return ret_df

def expand_quotations_with_polarity_subjectivity(df: pd.DataFrame):
    df['quotation_polarity'] = df['quotation'].map(lambda x: TextBlob(x).sentiment.polarity)
    df['quotation_subjectivity'] = df['quotation'].map(lambda x: TextBlob(x).sentiment.subjectivity)
    return df