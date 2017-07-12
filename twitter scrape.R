#install packages
install.packages("twitteR")
install.packages("ROAuth")
library("twitteR")
library("ROAuth")
# Download "cacert.pem" file
download.file(url="http://curl.haxx.se/ca/cacert.pem",destfile="C:\\Users\\Nick\\Desktop\\ISA401\\project1\\cacert.pem")
#establish credentials
cred <- OAuthFactory$new(consumerKey='vsyuJFpJ4tPJ2inHfs0V0BUrR',
                         consumerSecret='EKkFsJriLowri4blYmlULID0Iotlwk5ONshHGR1eT7pJTSxwEB',
                         requestURL='https://api.twitter.com/oauth/request_token',
                         accessURL='https://api.twitter.com/oauth/access_token',
                         authURL='https://api.twitter.com/oauth/authorize')
# Executing the next step generates an output --> Note:  You only need to do this part once
cred$handshake(cainfo="cacert.pem")

#save for later use for Windows
save(cred, file="twitter authentication.Rdata")

load("twitter authentication.Rdata")
registerTwitterOAuth(cred)

install.packages(c("devtools", "rjson", "bit64", "httr"))
#RESTART R session!
library(devtools)
install.packages('twitteR')
library(twitteR)

#Twitter Authentication with R

Consumer_key<- "vsyuJFpJ4tPJ2inHfs0V0BUrR"
Consumer_secret <- "EKkFsJriLowri4blYmlULID0Iotlwk5ONshHGR1eT7pJTSxwEB"
access_token <- "746320405-LnHEzc4OP6citqes0j3ETFBvIwqVYkXPId8z113k"
access_token_secret <- "4YMuFrg9KEYcpqmLWVAedoDbtNsnEI0Ua19DNYT42tb8x"
setup_twitter_oauth(Consumer_key,Consumer_secret,access_token,access_token_secret)

#Search testing
searchTwitter("#WT20")
userTimeline('nick_barry_', n=20,maxID=NULL, sinceID=NULL, includeRts=FALSE, 
             excludeReplies=FALSE)
tweets = userTimeline('nick_barry_', n=20,maxID=NULL, sinceID=NULL, includeRts=FALSE, 
                      excludeReplies=FALSE)
install.packages('xlsx')
library(xlsx) #load the package


fivethreetweets=userTimeline('FifthThird', n=3200,maxID=NULL, sinceID=NULL, includeRts=FALSE, 
                              excludeReplies=FALSE)
fivethreeDF = twListToDF(fivethreetweets)
write.csv(fivethreeDF, "C:\\Users\\Nick\\Desktop\\ISA401\\project1\\fivethree.csv")

tweets53 <- searchTwitter("Fifth Third OR 5/3 OR 'Fifth Third Bank' OR #53 OR #FifthThird OR #53Bank OR 'fifththird' OR 'fifth third' OR 'Fifththird'
                          OR #fifththird OR #53bank or '5/3 Bank'", n=3200, 
                          lang="en", since="2015-01-01")
tweets53DF = twListToDF(tweets53)
write.csv(tweets53DF, "C:\\Users\\Nick\\Desktop\\ISA401\\project1\\mentions.csv")




