
# pip install nltk
# python -m textblob.download_corpora
# pip install newspaper3k
# pip install flask

from flask import Flask, render_template, request, redirect, url_for, flash
from newspaper import Article # pip install newspaper3k
import nltk # pip install nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob # pip install textblob

# import beautifulsoup
from bs4 import BeautifulSoup
import requests
from flask_cors import CORS




nltk.download('vader_lexicon')

app = Flask(__name__)
CORS(app)

app.secret_key = 'super secret key'




@app.route('/sentimentAPI' , methods=['GET', 'POST'])
def index():
# Check if the request is POST

    sendJson = {
            
        }
    
    errorJson = {
            "score:" : "404",
            "error": "Error",
        }

    
    args = request.args
    api_URL = args.get('sentimentURL')
    api_username = args.get('username')
    api_school = args.get('school')
    api_sourceText = args.get('sourceText')

    print(api_URL)

# Check if users requested information is valid
        # Check if URL is valid - (Error 1 - Invalid URL)
    if api_URL == None:
        errorJson['error'] = "Error1"
    
        return errorJson

    # Check if username is valid - (Error 2 - Invalid Username)
    #if api_username == None:
        flash('Error2')
        return "Error2"
    # Check if school is valid - (Error 3 - Invalid School)
    #if api_school == None:
        flash('Error3')
        return "Error3"


#Load data  from database
        # Load username from database
        # Load school from database
        # Load URL from database

#Check if school is in database
        # Check if school is in database - (Error 4 - School not in database)


#Check if the request is POST - (Error 4 - Invalid Request)
    #if request.method == 'POST':
       # return "Error4"


# Send User information to Function 

    sentimentScore = sentimentAnalysis(api_URL,api_sourceText)
    sendJson["score"] = sentimentScore
    sentimentScore = sentimentScore[0:4]
    print(sendJson)

    return sentimentScore 
    




def sentimentAnalysis(URL,api_sourceText):
    # Sentiment analysis

    
# Download the text from the URL if not provided by the user
    if api_sourceText == None:
        # Download the text from the URL
        try:
            article = Article(URL)
            article.download()
            article.parse()
            article.nlp()
            sourceText = article.text
        except:
            try:
                # Download the text from the URL using beautiful soup
                sourceText = BeautifulSoup(requests.get(URL).text, 'html.parser').get_text()

            except:
                # Return Error 5 - could not download text from URL
                flash('Error5')
                return "Error5"
    else:
        sourceText = api_sourceText

    # Sentiment analysis
    


    # TextBlob
    
    try:
        #sentiment analysis from textblob
        blob = TextBlob(sourceText)
        sentimentTEXTBLOB = blob.sentiment.polarity

    except:
        # Error 6 - TextBlob could not analyze text
        flash('Error6')
        return "Error6"
    


    # VADER
    try:
        #sentiment analysis from vader
        sentiment_VADER = SentimentIntensityAnalyzer()
        sentimentVADER = sentiment_VADER.polarity_scores(sourceText)
    except:
        # Error 7 - Vader could not analyze text
        flash('Error7')
        return "Error7"

# average the sentiment scores
    sentimentAverage = (sentimentTEXTBLOB + sentimentVADER['compound'])/2


# Return the sentiment score

    print(sentimentAverage)
    
    return str(sentimentAverage)




        


    




# Run the app


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=2000)


