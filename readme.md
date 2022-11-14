# Twitter Bot

This twitter bot uses tweepy module which utilizes developer twitter API.

Author: Samridh Girdhar, Arnav Goel, Abhay Chowdhry

## Files:
1. main.py --> includes TwitterBot class
2. twitterKeys.yaml --> includes secretes for dev API

## About the Bot
- Twitter bot class has a getSecrets method which allows us to pull all the API keys from the yaml file. 
- These are then used in authenticating the user.
- Once the user is successfully authenticated, we first fetch some tweets using search_tweets function, 
in which we are passing in the query of getting 'bbc world news' with a count of 2, result type recent which is basically
fetching 2 latest world news
- getMajorHeadlines function then return a string the fetched tweets
- We then utilize this result to update our own status, using update_status function of twitter api. 
Since a tweet can only be maximum of 270 characters, we are slicing the string from the beginning to 270 characters.
and then we return out of the function.
The result ==> we can see our tweet in out profile on twitter!

## How to Run:
Main function is used to run all the code base.
- You can right click on the file to run the code
- You can run python main.py

 
