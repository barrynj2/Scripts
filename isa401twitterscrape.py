# -*- coding: utf-8 -*-

"""
Objective: This file is intended to use Python to Import Datasets from Twitter.
 This File Works Better on Python(x,y). If you are an IDLE user, please comment
 the OS clearing steps. Thank you

Instructions:
-------------
A] In order for this file to work correctly, make sure that you have 
   installed the Tweepy Library (see https://github.com/tweepy/tweepy)
   The re, time and OS libraries should be already installed on your computer.
   

B] Go to http://dev.twitter.com and create an app. 
   The consumer key and secret will be generated for you after
   After the step above, you will be redirected to your app's page.
   Create an access token under the the [Your access token] section
   For additional details on authentication, see:
   http://pythonhosted.org/tweepy/html/auth_tutorial.html#auth-tutorial


Credits:
--------
The Printing of the Twitter Stream to the Console is based on code originally 
written by Prof. Justin Yates, Texas A&M and edited by Jason Olson and Chase
Murray, University at Buffalo. Jason's code was designed to store the tweet's 
(text, created_at, id, and setTerms) in a text file. Our code stores additional
variables (e.g. coordinates of the tweet) which into an excel file. We parse 
all important fields in the Excel file to reduce the amount of post processing
needed for analysis.


How the Search Terms Were Selected:
----------------------------------
Search Terms for the Superobowl Ads were decided based on these websites:
   a] http://goo.gl/HaF74M
   b] http://goo.gl/wikEIl
   c] http://goo.gl/FDzuJD


Main Developers for this File:
-----------------------------
W. Murphy [a graduate of Auburn University]
F. Megahed [Miami University; Affiliate of Auburn University]

   """

#________________________Importing Needed Libraries____________________________
# You are Expected to Make Sure that all these packages are Installed on your
# Computer [Use Pip Command in CMD]
import tweepy # Main Package to Stream Twitter Data
import os     # Package Used to Clear the Python Console
import re     # Python Used to Ensure Proper Encoding Prior to Printing
import time   # Package Used for Debugging Purposes in System Sleep
import json
#______________________________________________________________________________



#_______________ Selecting Search Terms and Language for Twitter Search________
# Change the Search Terms Below to Something that you are Interested In.
setTerms = ['NFL','Concussion'] # add other flu_related terms here 
setLang = ['en'] # Feel Free to Change the Lang if your Terms are not English
print "Starting the code" # Notification to the User that the Code is Starting
#_____________________________________________________________________________



# _______________ OAAuth Step Needed to Connect to Twitter API________________
# Information on Authorization with Tweepy is based on:
# http://pythonhosted.org/tweepy/html/auth_tutorial.html#auth-tutorial
# Please Enter your Keys, Secret and Access Token/Secret Below
consumer_key = 'vsyuJFpJ4tPJ2inHfs0V0BUrR'       # --> PLEASE INSERT YOUR KEY HERE
consumer_secret = 'EKkFsJriLowri4blYmlULID0Iotlwk5ONshHGR1eT7pJTSxwEB'    # --> PLEASE INSERT YOUR SECRET HERE
access_token = '746320405-LnHEzc4OP6citqes0j3ETFBvIwqVYkXPId8z113k'       # --> PLEASE INSERT YOUR TOKEN HERE
access_token_secret = '4YMuFrg9KEYcpqmLWVAedoDbtNsnEI0Ua19DNYT42tb8x'# --> PLEASE INSERT YOUR TOKEN SECRET HERE
auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth1.set_access_token(access_token, access_token_secret)
print " Success" # Notification that the Authorization Worked
#______________________________________________________________________________



#___________________Specifying Output File Location____________________________
# Make Sure that the Name of the File is YourLastName_MainIdea.txt
# Change the Location of the File Based on Your Own Computer
fileName = "barry_test2.txt"
fileOut = open("C:\\Users\\megahefm\\Desktop\\Nick\\" 
               + fileName, "w") 
# Note that the double \\ prevents Python from Interpreting a \Letter as a 
# Specific Command
# For Mac/Linux, uncomment the following line:
#fileOut = open("/Users/binweng/Dropbox/BUAlCollaborative/SB/" + fileName, "w")  
# Change this to Your Pass
#______________________________________________________________________________



#__________ Defining a New Class (Modifying the Tweepy StreamListner Class)____
# For the purposes of outputing to the command window and storing the twitter
# attributes of interest in a location of our choice. 
class StreamListener(tweepy.StreamListener):
    
    def on_status(self,tweet):
        
        thisText = tweet.text
        thisText = re.sub('[^\\s!-~]','', thisText)
        thisText = str(thisText)
        print thisText
        
        thisCreated_at = str(tweet.created_at)
        print thisCreated_at
        
        thisId = tweet.id
        print thisId

        thisScreen_name =  tweet.author.screen_name
        thisScreen_name =  re.sub('[^\\s!-~]','', thisScreen_name)
        print thisScreen_name
        thisScreen_name = str(thisScreen_name)
        
        thisUsers_time_zone = tweet.user.time_zone # User's Timezone
        if thisUsers_time_zone is not None:
            thisUsers_time_zone=re.sub('[^\\s!-~]','', thisUsers_time_zone)
        # The use of re was to make sure we do not have any issues here
        print thisUsers_time_zone # Printing the time zone
        
        thisSource = tweet.source # Twitter Source, e.g. Twitter for iPhone
        if thisSource is not None:        
            thisSource=re.sub('[^\\s!-~]','', thisSource) # To remove any ™ signs
            thisSource = str(thisSource)
        print thisSource
        
        thisUsersLocation = tweet.user.location # User Input e.g. On My Couch
        if thisUsersLocation is not None:
            thisUsersLocation=re.sub('[^\\s!-~]', ' ', thisUsersLocation)    
        print thisUsersLocation    
        
        
        if tweet.coordinates is not None:
            # Coordinates is like a dictionary in a dictionary
            # Below is how we can pull the Long and Lat. Note Twitter Uses
            # a GEOJSON Type of Formatting
            pointLong= tweet.coordinates[u'coordinates'][0] 
            pointLat = tweet.coordinates[u'coordinates'][1] 
            pointLong = str(pointLong) # Changing that to String
            pointLat = str(pointLat)   # Changing that to String        
        else:
            pointLong="NA" # Writing That it was not provided by the user
            pointLat = "NA" # Writing that it was not provided by the user
        
        thisUsersCoordinates = [pointLong, pointLat] # see above
        print pointLong # print to console
        print pointLat # print to console
        
         # Comment all three lines below when you run your program 
        time.sleep(1)      # So you can reed the Tweets (Comment in Real-run)  
        os.system('cls')    # If using Linux, please replace cls by clear 
        time.sleep (1)     # Sleep for 1 second to allow user to see cld screen
        
        fileOut.write(thisText + "\t" + thisCreated_at + "\t" + str(thisId) + "\t" +
                      str(thisScreen_name) + "\t" + 
                      str(thisUsers_time_zone) + "\t" + 
                      str(thisSource) + "\t" + 
                      str(thisUsersLocation) + "\t" + 
                      pointLong + "\t" + 
                      pointLat + "\t" +
                      str(thisUsersCoordinates) + "\t" +
        "\n")
        
#______________________________________________________________________________        



#____________________Using the Class and Tweepy to Get Tweets__________________
l = StreamListener()
streamer = tweepy.Stream(auth=auth1, listener=l)
streamer.filter(track = setTerms, languages = setLang)