from textblob import TextBlob
import nltk
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
nltk.download('punkt')

sid = SentimentIntensityAnalyzer()


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
