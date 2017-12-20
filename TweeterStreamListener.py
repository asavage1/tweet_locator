import tweepy

class TweeterStreamListener(tweepy.StreamListener):
    """A class to process the twitter stream"""

    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
        #we open up a file to contain the tweets
        #self.f = open("tweets.txt", "a")
        

    def on_status(self, status):
        
        try:
            #msg = status.text.encode('utf-8')
            #print (msg)
            print (status)
            #write the tweet out to the file. We append a newline character at the end of each tweet
            #self.f.write(msg+'\n')
        except:
            print("An error has occurred")
            #close the file
            #self.f.close()
       
        return True

    def on_error(self, status_code):
        """Run on Error."""
        print("Error received")
        print(status_code)
        return True  # Don't kill the stream

    def on_timeout(self):
        """Handle timeouts."""
        return True  # Don't kill the stream
