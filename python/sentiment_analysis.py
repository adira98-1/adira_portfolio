from snowflake.snowpark import Session
from textblob import TextBlob

connection_parameters = {
    "account": "xzjpsrg-ix57642",
    "user": "ADIRA",
    "password": "Chinnu@30111998",
    "warehouse": "COMPUTE_WH",
    "database": "SMARTBUY_DEV",
    "schema": "MART",
    "role": "ACCOUNTADMIN"
}

session = Session.builder.configs(connection_parameters).create()

rows = session.sql("""
SELECT REVIEW_ID,
       REVIEW_TEXT
FROM SMARTBUY_DEV.MART.STG_REVIEWS
""").collect()

for row in rows:

    review = row["REVIEW_TEXT"]

    sentiment_score = TextBlob(review).sentiment.polarity

    if sentiment_score > 0:
        sentiment = "Positive"
    elif sentiment_score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print(f"Review: {review}")
    print(f"Sentiment: {sentiment}")
    print("-" * 50)


session.close()

