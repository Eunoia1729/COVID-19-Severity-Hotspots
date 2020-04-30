# COVID-19-Severity-Hotspots
Identification of most severly affected regions due to COVID-19 using Twitter Data

## Data Collection
For the collection of data, we have used the Tweepy API, using which we can retrieve a limited set of tweets according to user, topics or other attributes.     
Since we have tried to identify the affected places using two different approaches, as will be mentioned later, so we collected the data in two different forms:    
In first approach, we mined for the recent 1000 tweets that are related with COVID-19 and got the information of its text and the named location of the user. The issue that we faced here was that the named location was not following a definite format, as for a place, let say “New Delhi, India”, different users had location as “Delhi”, “New Delhi”, ”New Delhi, India”, and other forms. In this method for every 1000 tweets we were able to get around 80% tweets that had all the required data. The data hence received is in the file “tweet_data_1.csv”.  The code hence used can be seen in the script named **“tweet_collection_to_dataset_1.py”**.    

In the second approach, we mined for tweets that had text and the geo-location of the user. Since the availability of geo-location is based upon the preference of user, hence for every 1000 tweets we only were able to get around 10 tweets that had the information. The data hence received is in the file “tweet_data_2.csv”. The code hence used can be seen in the script named **“tweet_collection_to_dataset_2.py”**.   

Link to DataSets : https://drive.google.com/drive/folders/1zqKDZG-9FeX6EKI7OMplwLfH8tpBFOgp?usp=sharing   
   
## Pre-processing   
In the pre-processing part we performed two steps, namely, replacing the emoticon with a word equivalent, and second to replace the slangs and acronyms by their appropriate meanings.   
Emojis and Emticons play an important role in sentiment analysis, since they give clear relation of the user’s state of mind, but that is not recognised by the Model, which works only with words. Hence we replaced them with appropriate words, whose output can be seen in the file “Emoticon.png”. The code used to perform the task can be seen in “emoticon_removal.py” and the respective outputs for the two data forms can be seen in **“tweet_data_no_emoticon_1.csv”** and **“tweet_data_no_emoticon_2.csv”** respectively.   
Acronyms and slangs that are used in conversation are not directly recognised by the Model, hence we used to convert them to appropriate full-forms using “slang.txt”, where we had stored all the slangs and their replacements. The respective code to perform the task can be seen in “acronym_removal.py” outputs for the two data forms can be seen in “tweet_data_no_emoticon_no_slang_1.csv” and **“tweet_data_no_emoticon_no_slang_2.csv”** respectively.   

## Classification and Sentiment Analysis
Here, our objective is to classify tweets as negative tweets or positive tweets based on the text of the tweet. An example of a positive tweet is “Have a great day” and an example of a negative tweet is “you are a horrible woman”.
To classify the tweets as positive/negative, we need to first convert the text tokens into a value using vectorization techniques and then apply classification techniques on these vectors.   

Coming to the vectorization, term frequency–inverse document frequency is used which weight of a term that occurs in a tweet is simply proportional to the term frequency in the whole set of tweets.    
The vectors output by the vectorizer can be classified using various classification techniques like Support Vector Classification(SVC), Naive Bayes Classification , Logistic Regression etc...   
According to literature review, SVC is the most recommended classifier for sentiment analysis but as there are millions of tweets in “tweet_data.csv”, it is very time-taking and thus poses a problem.    

Hence, we use MultiNomial Naive Bayes method to classify the data. This model was trained using “training.1600000.csv” which is a labelled tweets dataset which contains 1,600,000 tweets.   
The trained classification model and vectorizer are stored as “finalised_model.sav” and “finalised_tfv.sav” using pickle to run it again in no-time.       

## Clustering Analysis
Using the tweets and the respective data, we perform Sentiment Analysis to get the sentiment of the user, which will be later for identification of COVID-19 affected places as follows:  

In the first approach, we used the set of data indexed by 1 above, with the named location. We clubbed the tweets according to the named location, such that all tweets from one location are together. Then we receive the sentiment of each tweet and for each tweet we perform the following task :
Negative Tweet : +2 to Location score
Positive Tweet : -1 to Location score  

Hence now the location with the most number of negative tweets can be perceived as the location most affected by COVID-19, which will be reflected in its score being high. We hence filter the 5 places with highest scores and output them as the five most affected locations. The code hence can be seen as **“Main_Code_1.ipynb”** and output as output.jpg.   

In the second approach, we used the set of data indexed as 2 above, with the geo-location data. Here we perform Sentiment Analysis to set the sentiment related to each tweet, and then use Agglomerative Clustering to cluster the places and identify a localized region affected by the pandemic. The code hence can be seen as **“Main_Code_2.ipynb”** and the output image as clusters_2.png and clusters_4.png.
The clusters_2.png file shows when the regions are clustered into 2 parts and the clusters_4.png shows when the regions are clustered into 4 parts.
