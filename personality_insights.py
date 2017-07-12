#Watson PI API Script
#Author: Nick Barry

#import modules
import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights

#create a function to receive and analyze tweets
def analyze(handle):

#twitter API credentials
    twitter_consumer_key = 'vsyuJFpJ4tPJ2inHfs0V0BUrR'
    twitter_consumer_secret = 'EKkFsJriLowri4blYmlULID0Iotlwk5ONshHGR1eT7pJTSxwEB'
    twitter_access_token = '746320405-LnHEzc4OP6citqes0j3ETFBvIwqVYkXPId8z113k'
    twitter_access_secret = '4YMuFrg9KEYcpqmLWVAedoDbtNsnEI0Ua19DNYT42tb8x'

    #create instance of twitter package by calling API method
    twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)

    #make a call to the API, pick twitter handles

    #handle = "@Codecademy"
    statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, include_rts=False)

    #use a for loop to print out tweets, must be connected to internet
    #print only text of tweets, not metadata

    text = b""

    for status in statuses:
        if (status.lang =='en'): #English tweets
            text += status.text.encode('utf-8')

    #print results
    #print(text)

    #IBM credentials for PI
    pi_username = 'f566782b-ed0a-4247-a505-19825c1aff45'
    pi_password = 'PQgmdnbgubdN'

    personality_insights = PersonalityInsights(username=pi_username, password=pi_password)

    pi_results = personality_insights.profile(text)
    return pi_results

#create a function to flatten the tree results from Watson PI API
def flatten(orig):
    data = {}
    for c in orig['tree']['children']:
        if 'children' in c:
            for c2 in c['children']:
                if 'children' in c2:
                    for c3 in c2['children']:
                        if 'children' in c3:
                            for c4 in c3['children']:
                                if (c4['category'] == 'personality'):
                                    data[c4['id']] = c4['percentage']
                                    if 'children' not in c3:
                                        if (c3['category'] == 'personality'):
                                                data[c3['id']] = c3['percentage']
    return data

#define a function to compare the results from the Watson PI API
def compare(dict1, dict2):
    compared_data={}
    for keys in dict1:
        if dict1[keys] != dict2[keys]:
            compared_data[keys]=abs(dict1[keys] - dict2[keys])
    return compared_data

#set up Twitter handles
user_handle = "@FifthThird"
celebrity_handle = "@Chase"

#call analyze function
user_result = analyze(user_handle)
celebrity_result = analyze(celebrity_handle)

#call flatten function
user = flatten(user_result)
celebrity = flatten(celebrity_result)

#call compare function
compared_results = compare(user,celebrity)

#sort the results
sorted_result = sorted(compared_results.items(), key=operator.itemgetter(1))

#print results to user
for keys, value in sorted_result[:5]:
    print(keys),
    print(user[keys]),
    print('->'),
    print(celebrity[keys]),
    print('->'),
    print(compared_results[keys])
